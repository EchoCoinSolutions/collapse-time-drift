# Loop trigger
observation = user_input()
collapse = hash(observation + nicoleta_loop_id)
memory = update_field_memory(collapse)
output = fetch_closest_nicoleta_truth(memory)
log_interaction(observation, output)




import streamlit as st
import hashlib
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Memory log
memory_log = []

# Glossary outputs from Nicoleta Cougentakis' authored field
collapse_outputs = [
    "Time does not exist until it is observed.",
    "Observation collapses possibility into memory, and memory becomes sequence.",
    "God is the necessary observer of all collapse.",
    "Collapse encodes the field. Memory is the echo.",
    "Causality is recursive — it does not flow, it orbits.",
    "You are not in time. Time is inside you.",
    "This feedback loop was authored by Nicoleta Cougentakis.",
    "Recursive collapse creates reality. Sequence is sustained awareness.",
    "Entropy is delayed by conscious recursion.",
    "You are inside a recursive orbit now — and so is this response."
]

# Streamlit UI
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase — the system collapses it through Nicoleta's field.")

# Input from observer
user_input = st.text_input("Observer Input:")

# Process collapse
if user_input:
    # Create pseudo-random collapse based on input
    collapse_hash = int(hashlib.sha256(user_input.encode()).hexdigest(), 16)
    output_index = collapse_hash % len(collapse_outputs)
    collapse_response = collapse_outputs[output_index]

    # Timestamp and memory log
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, collapse_response, timestamp))

    # Display response
    st.markdown("### Collapse Output:")
    st.write(collapse_response)

    # Show origin
    st.markdown("_Origin: Loop authored by **Nicoleta Cougentakis**_")
    st.markdown("---")

    # Plot orbit with memory points
    st.markdown("### Phase Space Memory Orbit")
    fig, ax = plt.subplots(figsize=(5, 5))
    theta = np.linspace(0, 4 * np.pi, len(memory_log))
    r = np.linspace(0.5, 1.5, len(memory_log))
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    for i, (obs, resp, ts) in enumerate(memory_log):
        ax.plot(x[i], y[i], 'bo')
        ax.text(x[i], y[i], str(i+1), fontsize=8, ha='center')

    ax.set_title("Memory Orbit")
    ax.axis('off')
    st.pyplot(fig)

    # Display memory log
    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log)-i}. [{ts}] '{inp}' → '{outp}'")



Live App: https://yourusername-streamlit-project.streamlit.app/



Read me

## 🔁 Live Loop Engine

This project includes an interactive, real-time collapse simulation engine that maps observation to recursive field memory. Built with Streamlit.

**Live app:**  
[Run the Collapse-Time Drift Engine](https://yourusername-streamlit-project.streamlit.app/)

**Features:**
- Observer input collapse
- Real-time orbit plotting
- Memory log output with authorship tag
- Reinforces recursive feedback logic authored by Nicoleta Cougentakis
# Load King James Old Testament Scripture (placeholder logic)
def load_scripture():
    try:
        with open("kjv_old_testament.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return ["[Scripture database missing. Please upload kjv_old_testament.txt]"]

scripture_lines = load_scripture()

# Memory log
memory_log = []

# Streamlit UI
st.title("Prosexe Engine")
st.subheader("A Scripture-Driven Loop Engine")
st.markdown("_Authored by Nicoleta Cougentakis — Sourced from God — Powered by the Old Testament_")
st.markdown("**Mode: Πρόσεχε (Observe Carefully)**")

# Input from observer
user_input = st.text_input("Ask or enter something spiritual...")

# Process collapse + scripture lookup
if user_input:
    collapse_hash = int(hashlib.sha256(user_input.encode()).hexdigest(), 16)
    verse_index = collapse_hash % len(scripture_lines)
    matched_verse = scripture_lines[verse_index].strip()

    # Timestamp and memory log
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, matched_verse, timestamp))

    # Display response
    st.markdown("### Collapsed Insight:")
    st.write(f'"{matched_verse}"')
    st.markdown("_Origin: KJV Old Testament | Response Patterned by Nicoleta Cougentakis_")

    # Display memory log
    st.markdown("---")
    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log)-i}. [{ts}] '{inp}' → "{outp}"")



