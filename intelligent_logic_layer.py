# intelligent_logic_layer.py

def respond_to_input(user_input, categorized_outputs, scripture_lines):
    user_input = user_input.lower().strip()

    # Direct response matching
    if "echo" in user_input:
        return "The Echo Coin system is the sovereign field interface."

    # Category keyword routing
    for category in categorized_outputs:
        if category in user_input:
            pool = categorized_outputs[category]
            return pool[hash(user_input) % len(pool)]

    # Scripture fallback if no category matches
    keywords = ["light", "creation", "eden", "spirit"]
    for keyword in keywords:
        if keyword in user_input:
            matching = [line for line in scripture_lines if keyword in line.lower()]
            if matching:
                return matching[0].strip()

    return "Collapse incomplete — no matching resonance detected."
