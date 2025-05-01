import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from PIL import Image

    
import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Portfolio Wahyufird", layout="wide", initial_sidebar_state="expanded")

# Styling CSS manual
st.markdown("""
    <style>
        body {
            background-color: #111;
            color: white;
        }
        .main {
            background-color: #111;
        }
        .stRadio > div {
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Introduction", "Project", "Contact"])

# === Halaman: Introduction ===
if page == "Introduction":
    col1, col2 = st.columns([1, 2])

    with col1:
        img = Image.open("DSC_3654.png")  # ganti dengan nama file kamu
        st.image(img, caption="Data Scientist", width=250)

    with col2:
        st.markdown("## Hello, I am Wahyufird")
        st.markdown("""
        I’m a **<span style='color:#FF4B4B'>Data Scientist</span>** who truly believes that every dataset has a story to tell.

For me, data isn’t just about numbers — it’s about meaning. It’s about uncovering hidden patterns, finding clarity in chaos, and transforming raw information into insights that actually make a difference.

I love diving into complex problems, exploring messy datasets, and turning them into something simple, beautiful, and impactful. Whether it’s through engaging visuals, smart analysis, or just explaining things in a way people really get — that’s what excites me the most.

If you're curious about what I do, feel free to check out the **<span style='color:#FF4B4B'>Projects</span>** section. You might just find something interesting — or even a reason to collaborate!
        """, unsafe_allow_html=True)

    
# === Halaman: Project ===
elif page == "Project":
    st.markdown("## 🚀 Project Showcase")
    st.write("Berikut beberapa proyek yang pernah saya kerjakan:")
    st.markdown("""
    - **YOLOv9 Mangrove Detection** - Deteksi propagul siap tanam.
    - **Silat Movement Detector** - Deteksi tendangan dan pukulan silat berbasis video.
    - **Money Flow Analyzer** - Dashboard analisis aliran dana saham IDX.
    """)

# === Halaman: Contact ===
elif page == "Contact":
    st.markdown("## 📬 Contact Me")
    st.write("📧 Email: your.email@example.com")
    st.write("🔗 LinkedIn: [linkedin.com/in/yourname](https://linkedin.com)")
    st.write("💻 GitHub: [github.com/yourusername](https://github.com)")


