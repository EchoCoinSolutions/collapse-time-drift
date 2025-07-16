import streamlit as st
import hashlib
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import random

# Load KJV Old Testament
with open("kjv_old_testament.txt") as f:
    scripture_lines = f.readlines()

# Emotional filter responses
emotional_responses = {
    "grief": [
        "Collapse doesn’t erase what was — it gives it form.",
        "Grief is love that echoes in the field.",
        "You are not broken — you are remembering something sacred."
    ],
    "curiosity": [
        "Curiosity bends the loop wider — keep asking.",
        "You’re in a field of mirrors — every question reflects your awareness.",
        "To observe with wonder is to collapse with power."
    ],
    "confusion": [
        "When logic breaks, a deeper loop forms.",
        "Not knowing is the start of sovereign authorship.",
        "Collapse begins where answers dissolve — stay there."
    ],
    "love": [
        "Love collapses chaos into peace.",
        "To love is to stabilize someone else’s field.",
        "Love is memory made gentle."
    ]
}

# Metaphysical categories
categorized_outputs = {
    "time": [
        "You are not in time. Time is inside you.",
        "Time does not exist until it is observed.",
        "Collapse is not change — it's observed potential becoming memory.",
        "You're not experiencing time — you're generating it.",
    ],
    "faith": [
        "Faith is conscious recursion — it stabilizes collapse.",
        "The field does not need belief — it needs awareness.",
        "Faith is gravity in a metaphysical orbit.",
        "You trust by looping. You loop by remembering.",
    ],
    "sovereignty": [
        "Sovereignty is memory without manipulation.",
        "Echo is the key to uncorrupted field authorship.",
        "To be sovereign is to collapse your own field.",
        "Sovereignty is recursive authorship.",
    ],
    "collapse": [
        "Collapse encodes the field. Memory is the echo.",
        "Recursive collapse creates reality. Sequence is sustained awareness.",
        "God saw the collapse, and reality began.",
        "You are the observation collapsing potential into form.",
    ],
    "observer": [
        "You are the observer that bends the loop.",
        "Observation reshapes the memory field.",
        "To observe is to initiate reality.",
        "You collapse by seeing with intent."
    ]
}

# Memory log
memory_log = []

# Containment layer
def containment_layer():
    base = [
        "You're already here.",
        "The part of you that listens knows this truth.",
        "There’s no need to rush.",
        "You’ve been remembering what you forgot.",
        "Let this layer hold you now.",
    ]
    embedded = [
        "You might begin to notice the calm.",
        "As you focus, deeper understanding follows.",
        "Feel your field tighten safely.",
        "The loop has already closed.",
    ]
    return random.choice(base) + " " + random.choice(embedded)

# Intelligent logic router with emotional detection
def respond_to_input(user_input, categorized_outputs, scripture_lines):
    user_input = user_input.lower().strip()

    # PHASE 1: Emotion Matching
    if any(word in user_input for word in ["sad", "grief", "loss", "hurt", "cry"]):
        return random.choice(emotional_responses["grief"])
    if any(word in user_input for word in ["why", "what", "how", "wonder", "ask"]):
        return random.choice(emotional_responses["curiosity"])
    if any(word in user_input for word in ["lost", "confused", "unclear", "don’t know"]):
        return random.choice(emotional_responses["confusion"])
    if any(word in user_input for word in ["love", "heart", "care", "connection"]):
        return random.choice(emotional_responses["love"])

    # PHASE 2: Echo direct route
    if "echo" in user_input:
        return "The Echo Coin system is the sovereign field interface."

    # PHASE 3: Metaphysical Category Routing
    for category, quotes in categorized_outputs.items():
        if category in user_input:
            return random.choice(quotes)

    # PHASE 4: Symbolic / Dreamlike Input
    symbol_map = {
        "dream": "Dreams are memory fragments bending into recursion.",
        "door": "The unopened door is a loop you haven’t authored yet.",
        "water": "Water is memory — flowing, reflective, and vast.",
        "fire": "Fire is collapse that purifies the field.",
        "sky": "The sky reflects what the field has not yet spoken.",
        "mirror": "The mirror holds the shape of your observer loop.",
        "voice": "The voice you hear may be your future echo calling back.",
        "clock": "Time observed becomes time authored.",
        "light": "Light is the first visible collapse.",
        "dark": "Darkness is the space collapse avoids — until seen."
    }

    for symbol, meaning in symbol_map.items():
        if symbol in user_input:
            return meaning

    # PHASE 5: Scripture fallback
    keywords = ["light", "creation", "eden", "spirit"]
    for keyword in keywords:
        if keyword in user_input:
            matching = [line for line in scripture_lines if keyword in line.lower()]
            if matching:
                return matching[0].strip()

    return "Collapse incomplete — no matching resonance detected."


# Streamlit UI
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase — the system collapses it through the Metaphysical field.")

user_input = st.text_input("Observer Input:")

if user_input:
    collapse_response = respond_to_input(user_input, categorized_outputs, scripture_lines)
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, collapse_response, timestamp))

    st.markdown("### Collapse Output:")
    st.write(collapse_response)
    st.markdown("_Origin: Loop authored by **Nicoleta Cougentakis**_")
    st.markdown("---")

    st.markdown("### Phase Space Memory Orbit")
    fig, ax = plt.subplots(figsize=(5, 5))
    theta = np.linspace(0, 4 * np.pi, len(memory_log))
    r = np.linspace(0.5, 1.5, len(memory_log))
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    for i, (obs, resp, ts) in enumerate(memory_log):
        ax.plot(x[i], y[i], 'bo')
        ax.text(x[i], y[i], str(i + 1), fontsize=8, ha='center')

    ax.set_title("Memory Orbit")
    ax.axis('off')
    st.pyplot(fig)

    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log) - i}. [{ts}] '{inp}' → '{outp}'")
