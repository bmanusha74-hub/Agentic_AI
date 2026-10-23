from datetime import datetime

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

def get_time():
    return datetime.now().strftime("%H:%M")

def add(first, second):
    return f"{first} + {second} = {int(first) + int(second)}"

def shout(text):
    return text.upper() + "!!!"

tools = {
    "greet": {
        "fn": greet,
        "args": ["name"],
        "desc": "Say hello to a person by name.",
    },
    "farewell": {
        "fn": farewell,
        "args": ["name"],
        "desc": "Say goodbye to a person by name.",
    },
    "get_time": {
        "fn": get_time,
        "args": [],
        "desc": "Give the current time in 24-hour format.",
    },
    "add": {
        "fn": add,
        "args": ["first number", "second number"],
        "desc": "Add two whole numbers together.",
    },
    "shout": {
        "fn": shout,
        "args": ["text"],
        "desc": "Repeat something back in capital letters.",
    },
}

history = []

print("I can do these things:")
for name in tools:
    print(" -", name, ":", tools[name]["desc"])
print("Type 'quit' to stop.")

while True:
    choice = input("\nWhich tool? ")

    if choice == "quit":
        print("\nHere is everything you asked me to do:")
        for i, entry in enumerate(history, start=1):
            print(i, "-", entry["tool"], "->", entry["result"])
        print("Total:", len(history), "tool calls.")
        print("Goodbye!")
        break

    try:
        tool = tools[choice]
        values = []
        for arg_name in tool["args"]:
            values.append(input(arg_name + ": "))
        result = tool["fn"](*values)
        history.append({"tool": choice, "result": result})
        print("Result:", result)
    except KeyError:
        print("Sorry, I have no tool called", choice)