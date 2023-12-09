import json 
import sys

replacements = {
    "\u0027": "'"
}

count = 0

def load(filename):
    with open(filename, "r") as file:
        return json.loads(file.read())

with open("messages.txt", "w") as file:
    file.write("")

if len(sys.argv) < 1:
    print("Please provide a file name")
    exit()

with open("messages.txt", "a") as file:
    data = load(sys.argv[1])
    start_date = sys.argv[2]
    enabled = False

    for message in data["messages"]:
        if message["created_date"] == start_date:
            enabled = True
        if not enabled:
            continue
        if "text" in message:
            content = message["text"]
            for key, value in replacements.items():
                content = content.replace(key, value)
            file.write(message["creator"]["name"] + " - " + f"{message['created_date']}" + "\n")
            file.write(content + "\n\n")
            count += 1
    file.close()

print(f"Done! loaded {count} messages from {sys.argv[1]}")