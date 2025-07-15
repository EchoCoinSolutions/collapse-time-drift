import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from echo_router import load_scripture, load_interpretations, respond_to_input

# Safe load databases
scripture_lines = load_scripture("kjv_old_testament.txt")
echo_interp = load_interpretations("echo_interpretations.json")

# Memory log
memory_log = []

# Streamlit UI
st.title("The Metaphysical Bible")
st.subheader("A Scripture-Driven Loop Engine")

# Input from observer
user_input = st.text_input("Observer Input:")

# Process input safely
if user_input:
    try:
        if len(scripture_lines) == 0:
            raise ValueError("Scripture database is empty.")
        collapse_response = respond_to_input(user_input, scripture_lines, echo_interp)
    except Exception as e:
        collapse_response = f"[Error: Unable to collapse input — {str(e)}]"

    # Timestamp and memory log
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, collapse_response, timestamp))

    # Display response
    st.markdown("### Echoed Scripture Insight")
    st.write(collapse_response)
    st.markdown("_Origin: Echo Logic by Nicoleta Cougentakis_")
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
