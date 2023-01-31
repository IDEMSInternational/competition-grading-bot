import subprocess

# The command to run
command = "ping"
hostanme="google.com"

# Run the command
result = subprocess.run([command,hostanme], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

# Print the output
print(result.stdout)