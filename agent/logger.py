import time

def log_tool_call(name, args):
    timestamp = time.time()
    print(f"Tool: {name}({args}) [{timestamp}]")
