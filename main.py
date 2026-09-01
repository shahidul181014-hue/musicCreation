import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import io
import wave

# Configure page layout
st.set_page_config(page_title="SynthWave Studio AI", layout="wide")

# Sidebar - User Inputs
with st.sidebar:
    prompt = st.text_input("Enter a prompt (e.g., Upbeat 80s synthwave for a driving scene)", "Upbeat 80s synthwave for a driving scene")
    track_length = st.slider("Track Length (seconds)", 30, 120, 60)
    temperature = st.selectbox(
        "Model Creativity (Temperature)", 
        ["Low (Consistent)", "Medium (Balanced)", "High (Experimental)"], 
        index=1
    )
    generate_btn = st.button("Generate Track", type="primary")

# Main Content Area
st.title("SynthWave Studio AI: Generate Your Vibe")
st.markdown("Generative AI for Music Creation")

# Initial State
if not generate_btn and 'generated' not in st.session_state:
    st.info("Welcome to SynthWave Studio AI: Generate Your Vibe.\n\nConfigure the parameters in the sidebar and click 'Generate Track' to create your unique AI composition.")

# Post-Generation State
if generate_btn or 'generated' in st.session_state:
    st.session_state['generated'] = True
    
    if generate_btn:
        with st.spinner("Synthesizing your track... This may take a moment."):
            time.sleep(2) # Simulates latent space traversal and decoding delay

    # Header for generated output
    st.markdown(f"**Generated Track: [{prompt}]**")
    
    # Generate dummy audio signal (440Hz sine wave layered with noise to simulate data)
    sample_rate = 44100
    duration = 2 
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio_signal = 0.5 * np.sin(2 * np.pi * 440 * t) + np.random.normal(0, 0.1, t.shape)
    
    # Audio Player
    st.audio(audio_signal, sample_rate=sample_rate)
    st.download_button(label="Download track (WAV)", data="dummy_wav_byte_stream", file_name="generated_track.wav")
    
    # Spectrogram Visualization
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.specgram(audio_signal, Fs=sample_rate, cmap='jet')
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Time')
    st.pyplot(fig)
    
    # Latent Attribute Refinement Hooks
    st.markdown("**Refine and Iterate**")
    style_adjustment = st.radio("Adjust generated style?", ["Keep original", "Slower tempo", "Add more bass"], index=2)
    variation_intensity = st.slider("Variation Intensity", 0.1, 1.0, 0.5)
    
    if st.button("Regenerate with adjustments"):
        st.success("Track successfully adjusted based on refined conditioning parameters!")