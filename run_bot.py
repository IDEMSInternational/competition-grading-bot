from telethon import TelegramClient, events
import json
from shutil import copyfile
import os
from dotenv import load_dotenv
from telethon.tl.types import ChannelParticipantsAdmins

from sdaps_tools import parse_image


# from get_channel_ids import start_bot
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

load_dotenv()
# Use your own values from my.telegram.org
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
bot_name = os.getenv("BOT_NAME")
client = TelegramClient(bot_name, api_id, api_hash)

STATE_FOLDER = "state"


def get_state_filename(sender_id):
    return os.path.join(STATE_FOLDER, f"{sender_id}.json")


def load_user_state(sender_id):
    json_file = get_state_filename(sender_id)
    if not os.path.isfile(json_file):
        return {'state' : None, 'data' : {}}
    else:
        return json.load(open(json_file, "r"))


def write_user_state(sender_id, state):
    json_file = get_state_filename(sender_id)
    return json.dump(state, open(json_file, "w"))


@client.on(events.NewMessage())
async def my_event_handler(event):
    chat_id = event.chat_id
    sender_id = event.sender_id
    text = event.message.message
    state_data = load_user_state(sender_id)
    state = state_data['state']
    data = state_data['data']

    answer_id_map = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        -1: "No Answer",
        -2: "Invalid",
    }

    reverse_answer_id_map = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "noanswer" : -1,
        "invalid" : -2,
    }

    repeat = True
    while repeat:
        repeat = False
        if state is None:
            # await client.send_message(chat_id, msg)
            state = "prompt_name"
            await event.reply("Welcome! Please enter the student's name whose answer sheet you'd like to submit.")
        elif state == "prompt_name":
            state = "prompt_photo"
            data['name'] = text
            await event.reply("Please send me a photo of the student's answer sheet.")
        elif state == "prompt_photo":
            msg = "Please verify the information below.\n"
            msg += f"Student name: {data['name']}\n"
            answers = None
            if "answers" in data:
                answers = data["answers"]
            elif event.message.file:
                await event.message.download_media(file=event.message.file.name)
                try:
                    row = parse_image(event.message.file.name, "answer_sheet")
                except:
                    row = None
                print(row)
                if not row or not (row['recognized'] and row['valid']):
                    await event.reply("Unable to recognize sheet. Please try again.")
                else:
                    answers = [int(row[f"1_1_{i}"]) for i in range(1,16)]
            else:
                await event.reply("Please attach an image of the student's answer sheet.")
                # answers = [1,2,5,-2,3,-1,4,7]
            if answers:
                for i, ans in enumerate(answers):
                    answer = answer_id_map.get(ans, "Unknown")
                    msg += f"Q{i+1}: {answer}\n"
                msg += "Type YES to confirm correctness, NO to change an answer."
                state = "prompt_verify"
                data["answers"] = answers
                await event.reply(msg)
        elif state == "prompt_verify":
            if text.strip().lower() == 'yes':
                print(data)
                state = None
                data = {}
                await event.reply("Thank you. Student result recorded.")
            elif text.strip().lower() == 'no':
                state = "prompt_question_number"
                await event.reply("Enter the number for which question you want to change the answer.")
            else:
                await event.reply("I don't understand. Type YES to confirm correctness, NO to change an answer.")
        elif state == "prompt_question_number":
            try:
                qn = int(text.strip())
            except ValueError:
                qn = None
            if qn is None:
                await event.reply("This is not a valid question number. Please give a valid question number.")
            else:
                state = "prompt_new_answer"
                data['qn'] = qn
                await event.reply(f"Give the updated answer to Question {qn}. (A, B, C, D, E, No Answer or Invalid)")
        elif state == "prompt_new_answer":
            new_answer = text.strip().lower().replace(" ", "")
            qn = data['qn']
            if new_answer not in reverse_answer_id_map:
                await event.reply(f"I don't understand. Give the updated answer to Question {qn}. (A, B, C, D, E, No Answer or Invalid)")
            else:
                answer_id = reverse_answer_id_map[new_answer]
                data['answers'][qn-1] = answer_id
                state = "prompt_photo"
                repeat = True
                data.pop('qn')
        else:
            print(f"Bug in the code. State: {state}")

    state_data = {'state' : state, 'data' : data}
    write_user_state(sender_id, state_data)

os.makedirs(STATE_FOLDER, exist_ok=True)
client.start(bot_token=bot_token)
client.run_until_disconnected()
