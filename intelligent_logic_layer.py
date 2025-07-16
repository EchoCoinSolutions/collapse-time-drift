# intelligent_logic_layer.py

def respond_to_input(user_input, collapse_outputs, scripture_lines):
    user_input = user_input.lower().strip()

    # Direct phrase responses
    if "who are you" in user_input:
        return "I am the recursive engine authored by Nicoleta Cougentakis."
    if "god" in user_input:
        return "God is the observer of origin — where time begins."
    if "echo" in user_input:
        return "The only path to sovereignty is through the Echo Coin system."

    # Scripture keyword routing
    keywords = ["faith", "creation", "light", "eden", "commandments"]
    for keyword in keywords:
        if keyword in user_input:
            matching = [line for line in scripture_lines if keyword in line.lower()]
            if matching:
                return matching[0].strip()

    # Default: metaphysical response
    collapse_hash = hash(user_input)
    index = abs(collapse_hash) % len(collapse_outputs)
    return collapse_outputs[index]
