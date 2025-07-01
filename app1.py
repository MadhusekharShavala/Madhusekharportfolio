import streamlit as st

# Load resume file as bytes
with open("MADHU_SEKHAR'S_Resume.pdf", "rb") as file:
    resume_bytes = file.read()

# Page configuration
st.set_page_config(page_title="Madhu Sekhar | AI/ML Engineer", layout="wide")

# Sidebar (optional)
with st.sidebar:
    st.title("📞 Contact")
    st.markdown("**📍 Location:** Hyderabad, India")
    st.markdown("**📧 Email:** [madhusekhar.shavala21@gmail.com](mailto:madhusekhar.shavala21@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [linkedin.com/in/madhusekharshavala](https://linkedin.com/in/madhusekharshavala)")

# Title section with Resume Download
st.title("👨‍💻 SHAVALA MADHU SEKHAR")
st.subheader("AI/ML Engineer | Software Developer | Data Science Enthusiast")

st.download_button(
    label="📄 Download Resume",
    data=resume_bytes,
    file_name="MADHU_SEKHAR_Resume.pdf",
    mime="application/pdf"
)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧑‍💼 Summary", "🛠 Skills", "📂 Projects", "🏢 Experience", "🎓 Education", "📬 Contact Me"
])

# Summary Tab
with tab1:
    st.header("Professional Summary")
    st.write("""
    I’m a passionate Software Engineer with a strong focus on Artificial Intelligence, Machine Learning, Web Development, and Scalable System Design.
I Thrive on transforming complex problems into elegant, data-driven solutions — whether it's crafting intelligent ML models, designing responsive Streamlit dashboards, or developing robust end-to-end applications. With a blend of creativity and precision, I turn ideas into impactful, production-ready systems that solve real-world challenges.
Driven by curiosity and continuous learning, I specialize in building smart, user-centric solutions that bridge the gap between cutting-edge technology and practical implementation.
    """)

# Skills Tab
with tab2:
    st.header("Technical Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👨‍💻 Programming Languages & ML")
        st.markdown("- 🐍 **Python**")
        st.markdown("- 🤖 **Machine Learning**")
        st.markdown("- 📊 **Scikit-learn**")
        st.markdown("- 📉 **Linear & Logistic Regression**")
        st.markdown("- 🌲 **Decision Tree, Random Forest**")

        st.markdown("### 📊 Data Science Tools")
        st.markdown("- 🧮 **NumPy**")
        st.markdown("- 🧱 **Pandas**")
        st.markdown("- 📈 **Matplotlib**")
        st.markdown("- 📊 **Seaborn**")

    with col2:
        st.markdown("### 🧰 Tools & Platforms")
        st.markdown("- 🐳 **Docker**")
        st.markdown("- 🐙 **GitHub**")
        st.markdown("- 📦 **Streamlit**")
        st.markdown("- 🧪 **Flask**")
        st.markdown("- ☁️ **Kubernetes**")

        st.markdown("### 🌐 Web & UI")
        st.markdown("- 🌐 **HTML/CSS**")
        st.markdown("- 🎨 **Basic UI/UX**")

        st.markdown("### 💡 Soft Skills")
        st.markdown("- 🤝 **Teamwork**")
        st.markdown("- 🧠 **Problem Solving**")
        st.markdown("- 🗣 **Communication**")

# Projects Tab
with tab3:
    st.header("Highlighted Projects")

    st.subheader("📊 Zomato Restaurant Rating Prediction")
    st.write("""
    - Full ML pipeline with Pandas, Seaborn, Scikit-learn.
    - Achieved 85%+ accuracy using Random Forest and Linear Regression.
    """)

    st.subheader("🎓 Student Grading System")
    st.write("""
    - Python Tkinter GUI to manage internal grades with validation, modular OOP, and login roles.
    """)

    st.subheader("📈 Student Performance Prediction")
    st.write("""
    - Streamlit app to predict student scores using multiple regression models.
    - Features batch predictions, CSV export, and responsive UI.
    """)

    # Tax Calculator Project Dropdown
with st.expander("💰 Income Tax Calculator (India)"):
    st.markdown("### 📌 Project Title")
    st.write("Income Tax Calculator Web App")

    st.markdown("### 🧾 Description")
    st.write("An interactive web-based calculator to estimate personal income tax based on the Indian Old and New Tax Regimes.")

    st.markdown("### 📋 Project Summary")
    st.write("""
    - 📥 Takes user input: **Name, Age, Annual Income**, and **Regime Type**.
    - 🔢 Implements **Indian tax slab logic** for different age groups and regimes.
    - 📈 Visualizes results with:
        - **Pie Chart** for income breakdown.
        - **Bar Chart** comparing income, tax, and net income.
    - 🚨 Handles missing input cases with warnings.
    - 🔁 Realtime tax computation with dynamic UI using Streamlit.
    - 🧠 Built using Python, Streamlit, and Matplotlib for data visualization.
    - 💡 Suitable for individuals, financial advisors, or learning projects.
""")


# Experience Tab
with tab4:
    st.header("Professional Experience")
    st.subheader("Software Engineer | Lyros Technologies Pvt. Ltd.")
    st.markdown("**Feb 2025 – Present | Hyderabad, India**")
    st.write("""
    - Built and deployed AI/ML models for real-time apps.
    - Used Streamlit, Docker, GitHub for collaborative development.
    - Practiced Agile and full SDLC involvement.
    """)

# Education Tab
with tab5:
    st.header("Education")

    st.subheader("🎓 B.Tech – ECE")
    st.write("**G. Pullaiah College of Engineering & Technology, Kurnool**")
    st.write("Graduated: April 2024 | CGPA: 5.8")

    st.subheader("🏫 Intermediate – MPC")
    st.write("**Sri Chaitanya Junior College, Kurnool** | Grade: 77.4%")

    st.subheader("🏫 SSC – High School")
    st.write("**Bala Bharathi High School, Kurnool** | CGPA: 8.7")

# Contact Me Tab (Custom Layout)
with tab6:
    st.title("📬 Contact Me")
    
    st.markdown("""
    If you'd like to get in touch, feel free to reach out via:

    - 📧 Email: [mailto:madhusekhar.shavala21@gmail.com](mailto:madhusekhar.shavala21@gmail.com)
    - 💼 LinkedIn: [linkedin.com/in/madhu](https://linkedin.com/in/madhusekharshavala)
    - 💻 GitHub: [github.com/madhu](https://github.com/MadhusekharShavala)
    """)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Send")
