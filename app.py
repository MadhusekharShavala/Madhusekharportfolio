import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Page Configuration
st.set_page_config(
    page_title="Madhu Sekhar | AI/ML Engineer",
    page_icon="🤖",
    layout="wide"
)

# ===== Sidebar =====
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/placeholder", width=150)  # Optional: your image
    st.title("Madhu Sekhar")
    st.markdown("**AI/ML Engineer**")

    # Resume download
    with open("MADHU_SEKHAR'S_Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name="MADHU_SEKHAR'S_Resume.pdf",
        mime='application/pdf'
    )

    st.markdown("---")
    selected_tab = option_menu(
        menu_title="Navigation",
        options=["About", "Skills", "Projects", "Contact"],
        icons=["person", "graph-up", "folder", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# ===== Main Content Area =====
if selected_tab == "About":
    st.title("👋 About Me")
    st.write("""
    I'm **Madhu Sekhar**, an AI/ML Engineer passionate about building scalable models and intelligent applications. 
    I specialize in machine learning, deep learning, data preprocessing, and end-to-end model deployment.
    """)

elif selected_tab == "Skills":
    st.title("🛠️ Skills")
    cols = st.columns(3)
    skills = {
        "Python 🐍": 90,
        "Machine Learning 📊": 85,
        "Deep Learning 🧠": 80,
        "NLP 📚": 75,
        "Computer Vision 👁️": 70,
        "Streamlit ⚙️": 85,
        "SQL 🗃️": 80,
        "Git/GitHub 🔧": 80,
        "Data Visualization 📈": 85
    }

    for idx, (skill, percent) in enumerate(skills.items()):
        with cols[idx % 3]:
            st.progress(percent)
            st.write(f"**{skill}**")

elif selected_tab == "Projects":
    st.title("📂 Projects")
    st.write("### 🧠 AI/ML Projects")
    st.markdown("""
    - **Resume Parser** – Extract and analyze content from resumes using NLP.
    - **Face Mask Detector** – Real-time face mask detection using computer vision.
    - **Stock Price Predictor** – Time series forecasting using LSTM.
    - **Movie Recommendation System** – Content-based filtering recommendation engine.
    """)

elif selected_tab == "Contact":
    st.title("📬 Contact Me")
    st.markdown("""
    If you'd like to get in touch, feel free to reach out via:

    - 📧 Email: [madhu@example.com](mailto:madhu@example.com)
    - 💼 LinkedIn: [linkedin.com/in/madhu](https://linkedin.com/in/madhu)
    - 💻 GitHub: [github.com/madhu](https://github.com/madhu)
    """)
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Send")
