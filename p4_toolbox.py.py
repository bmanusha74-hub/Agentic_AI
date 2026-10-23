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
print("Available tools:", list(tools.keys()))
choice = input("Which tool?")
if choice == "get_time":
    result = tools[choice]()
else:
    person = input("Name:")
    result = tools[choice](person)
print("Result:", result)