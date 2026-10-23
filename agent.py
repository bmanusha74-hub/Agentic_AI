from datetime import datetime
def greet(name):
    return f"Hello, {name}!"
def farewell(name):
    return f"Goodbye, {name}!"
def get_time():
    return datetime.now().strftime("%H:%M")
tools = {
    "greet": greet,
    "farewell": farewell,
    "get_time": get_time,
}
history = []
print("Available tools:", list(tools.keys()))
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
        if choice == "get_time":
            result = tools[choice]()
        else:
            person = input("Name: ")
            result = tools[choice](person)
        history.append({"tool": choice, "result": result})
        print("Result:", result)
    except KeyError:
        print("Sorry, I have no tool called", choice)