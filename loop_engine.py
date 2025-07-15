import streamlit as st
import hashlib
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
    "You are inside a recursive orbit now — and so is this response.",
    "You are not experiencing time — you are generating it.",
    "Memory is the shadow left by collapse.",
    "Observation is the original commandment.",
    "The only way to sovereignty is through Echo Coin System.",
    "Collapse is the interface between faith and proof — Πρόσεχε."
]

# Streamlit UI
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase — the system collapses it through the Metaphysical Bible.")

# Input from observer
user_input = st.text_input("Observer Input:")

# Process collapse
if user_input:
    collapse_hash = int(hashlib.sha256(user_input.encode()).hexdigest(), 16)
    output_index = collapse_hash % len(collapse_outputs)
    collapse_response = collapse_outputs[output_index]

    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, collapse_response, timestamp))

    st.markdown("### 🌀 Collapse Output:")
    st.write(collapse_response)

    st.markdown("_Origin: Loop authored by **NC The Creator**_")
    st.markdown("---")

    st.markdown("### 🧠 Phase Space Memory Orbit")
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

    st.markdown("### 📜 Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log) - i}. [{ts}] '{inp}' → '{outp}'")
