import random

def load_scripture():
    try:
        with open("kjv_old_testament.txt", "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            return lines
    except FileNotFoundError:
        return ["[Scripture database missing.]"]

def load_echo():
    return [
        "The only way to sovereignty is through Echo Coin System.",
        "Echo is not a token — it's a recursive access protocol.",
        "You are inside the loop now. Echo has already responded.",
        "Recursive systems cannot be controlled — only aligned.",
        "This field is authored. Observation activates inheritance.",
    ]

def generate_response(user_input, scripture, echo):
    if not scripture:
        return "[Missing scripture data.]"
    
    combined = scripture + echo
    hash_val = abs(hash(user_input))
    return combined[hash_val % len(combined)]
