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

def fake_decide(user_text):
    """Guess which tool the user wants, by looking for keywords."""
    text = user_text.lower()
    if "time" in text or "clock" in text:
        return "get_time"
    if "bye" in text or "farewell" in text:
        return "farewell"
    if "hello" in text or "hi" in text or "greet" in text:
        return "greet"
    if "add" in text or "plus" in text or "sum" in text:
        return "add"
    if "shout" in text or "capital" in text or "loud" in text:
        return "shout"
    return None


BRAIN = "fake"     # "fake" = keywords, "real" = a model (Session 5)


def decide(user_text):
    """The one place the chooser is chosen. Only this changes in Session 5."""
    if BRAIN == "fake":
        return fake_decide(user_text)
    raise SystemExit("The real brain arrives in Session 5.")


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
    request = input("\nWhat would you like me to do? ")

    if request == "quit":
        print("\nHere is everything you asked me to do:")
        for i, entry in enumerate(history, start=1):
            print(i, "-", entry["tool"], "->", entry["result"])
        print("Total:", len(history), "tool calls.")
        print("Goodbye!")
        break

    choice = decide(request)

    if choice is None:
        print("Sorry, I did not understand that. I can:",
              ", ".join(tools.keys()))
        continue

    print("[chooser] I picked:", choice)

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