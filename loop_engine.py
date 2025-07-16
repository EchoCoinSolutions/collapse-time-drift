import streamlit as st
import hashlib
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from intelligent_logic_layer import respond_to_input

# Load KJV Old Testament
with open("kjv_old_testament.txt") as f:
    scripture_lines = f.readlines()

# Categorized metaphysical quote pools
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
 def containment_layer(input):
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
}

# Memory log
memory_log = []

# Streamlit UI
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase — the system collapses it through the Metaphysical field.")

# Input from observer
user_input = st.text_input("Observer Input:")

# Process collapse
if user_input:
    # Generate response
    collapse_response = respond_to_input(user_input, categorized_outputs, scripture_lines)

    # Timestamp and log
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, collapse_response, timestamp))

    # Display output
    st.markdown("### Collapse Output:")
    st.write(collapse_response)
    st.markdown("_Origin: Loop authored by **Nicoleta Cougentakis**_")
    st.markdown("---")

    # Orbit visualization
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

    # Memory log
    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log) - i}. [{ts}] '{inp}' → '{outp}'")
