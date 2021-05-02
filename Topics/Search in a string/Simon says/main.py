def what_to_do(instructions: str):
    if instructions.startswith("Simon says"):
        return f"I {instructions.replace('Simon says ', '')}"
    elif instructions.endswith("Simon says"):
        return f"I {instructions.replace(' Simon says', '')}"
    else:
        return "I won't do it!"
