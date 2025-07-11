import streamlit as st
from PIL import Image
import base64
import json
import requests
import os

# ----- Page Configuration -----
st.set_page_config(page_title="MADHU SEKHAR | Portfolio", page_icon="📊", layout="wide")

# ----- Load Lottie Animation -----
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example AI/Data Science animation
lottie_ds = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_2glqweqs.json")  # Replace with any Lottie animation you like

# ----- Sidebar -----
# ----- Sidebar -----
# ----- Sidebar -----
with st.sidebar:
    st_lottie = st.components.v1.html(f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_2glqweqs.json"  background="transparent" speed="1" style="width: 100%; height: 200px;" loop autoplay></lottie-player>
    """, height=200)

    st.title("SHAVALA MADHU SEKHAR")
    st.subheader("🧠 AI/ML Engineer | Data Science Enthusiast")
    st.markdown("**📧 Email:** [madhusekhar.shavala21@gmail.com](mailto:madhusekhar.shavala21@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [linkedin.com/in/madhusekharshavala](https://linkedin.com/in/madhusekharshavala)")
    st.markdown("**🐙 GitHub:** [github.com/MadhusekharShavala](https://github.com/MadhusekharShavala)")
    st.markdown("📱 +91 - 7658906331")

    if os.path.exists("SHAVALA_MADHUSEKHAR_RESUMEE.pdf"):
        with open("SHAVALA_MADHUSEKHAR_RESUMEE.pdf", "rb") as f:
            st.download_button("📄 Download Resume", f, file_name="SHAVALA_MADHUSEKHAR_RESUMEE.pdf")
    else:
        st.warning("📄 Resume not found.")




# ----- Tabs -----
tabs = st.tabs(["🏠 Home", "🎯 Objective", "🛠️ Skills", "💼 Experience", "📂 Projects", "🎓 Education", "📬 Contact"])

# ----- Home -----
with tabs[0]:
    st.title(" Madhu Sekhar Shavala")
    st.markdown("""
### 🔍 Who am I?
I'm a passionate and driven **AI/ML Engineer** with a strong command over Python, Machine Learning and a deep curiosity for solving real-world problems using data.

### 🚀 What I Do?
- Build intelligent systems using **Machine Learning** and **Deep Learning**
- Craft beautiful, interactive web dashboards with **Streamlit**
- Perform insightful **EDA** and visual storytelling with **Matplotlib**, **Seaborn**, and **Plotly**
- Automate predictions and deploy ML solutions on the cloud

### 🌟 Highlights:
- ✅ Built real-time **Student Performance Predictor**
- 📈 Achieved 85%+ accuracy in **Zomato Rating Prediction**
- 🔐 Designed secure academic management systems
- 🐳 Deployed ML models using **Docker** and **Streamlit Cloud**

> *"Transforming data into decisions is not just my skill – it's my passion."*
    """)

# ----- Career Objective -----
with tabs[1]:
    st.header("🎯 Career Objective")
    st.markdown("""
I'm a results-driven Software Engineer with a solid foundation in Artificial Intelligence 🤖 and Machine Learning 📊.
Currently contributing at Lyros Technologies Pvt. Ltd., where I actively work on real-time AI/ML projects and thrive in agile-based, collaborative environments 🔄.

💡 Core Expertise:
- 🐍 Python programming, data analysis and ML model development using Scikit-learn, Pandas, NumPy, and Seaborn.
- 🌟 Building interactive web apps with Streamlit.
- 🏗️ Deploying scalable, modular systems that connect data science with real-world applications.

With a passion for innovation 💡 and a mindset geared toward continuous learning 📚, I specialize in transforming complex challenges into intelligent, actionable solutions — whether through predictive modeling 🔮, system design 🧩, or intuitive data-driven apps 📱.
    """)

# ----- Skills -----
with tabs[2]:
    st.header("🛠️ Technical Skills")
    st.markdown("""
- 🐍 **Languages**: Python, Machine Learning 
- 🌐 **Web Development**: HTML, CSS, Basic UI/UX 
- 📊 **Data Analysis & Visualization**: NumPy, Pandas, Matplotlib, Seaborn, Plotly  
- 🤖 **Machine Learning**: All MAchine Learning Algorithms, Scikit-learn  
- 🧠 **Deep Learning**: TensorFlow  
- 🛠️ **Tools & IDEs**: Jupyter Notebook, Google Colab, Visual Studio Code, Streamlit  
- 📁 **Version Control**: Git, GitHub  
- 🐳 **Deployment**: Docker, Render
    """)

# ----- Experience -----
with tabs[3]:
    st.markdown("### 💼 **Software Engineer | Lyros Technologies Pvt. Ltd. (Feb 2025 – Present)**")
    st.markdown("""
- 🧠 Hands-on training in AI/ML on real-time data projects  
- 🤖 Built and deployed supervised ML models using Scikit-learn & Python  
- 📊 Developed interactive ML dashboards with Streamlit  
- 🧪 Experienced in data preprocessing, evaluation metrics, feature engineering, and model tuning  
- 🧰 Worked on Docker-based deployment for ML apps  
- 📝 Practiced Agile development and version control with Git
    """)

# ----- Projects -----
with tabs[4]:
    st.header("📂 Projects")

    with st.expander("📊 Zomato Restaurant Rating Prediction"):
        st.markdown("### 🧾 Description")
        st.write("""
        A machine learning project aimed at predicting restaurant ratings using real-world Zomato data, leveraging data science tools and visualization techniques.
        """)
        st.markdown("### 📋 Project Summary")
        st.write("""
        - 🔍 Performed in-depth **EDA** to uncover trends in customer preferences and restaurant attributes.  
        - 🧠 Engineered key features from categorical and geospatial data for enhanced model accuracy.  
        - 🤖 Built and evaluated models including **Random Forest** and **Linear Regression**, achieving **85%+ accuracy**.  
        - 📊 Used **Seaborn** and **Plotly** to visualize influential factors affecting restaurant ratings.  
        """)

    with st.expander("🎓 Student Grading System"):
        st.markdown("### 🧾 Description")
        st.write("An internal desktop application for managing student grades, built using Python and Tkinter, tailored for academic institutions.")
        st.markdown("### 📋 Project Summary")
        st.write("""
        - 🧩 Designed with **modular OOP architecture** to ensure code scalability and maintainability.  
        - 🔐 Implemented a secure **role-based login system** for admins and faculty.  
        - 🗂️ Enabled seamless management of student data and grades using **NumPy and Pandas**.  
        - 🧠 Built with extensibility for **future ML integration** to automate grading and performance analytics.  
        """)

    with st.expander("📈 Student Performance Prediction"):
        st.markdown("### 🧾 Description")
        st.markdown("A real-time web application to predict student performance using machine learning regression models based on academic and attendance data.")
        st.markdown("### 📋 Project Summary")
        st.write("""
        Developed an interactive **Streamlit-based tool** to forecast student scores and visualize trends.
        - 🤖 Built regression models: **Linear, Polynomial, Decision Tree, Random Forest**.  
        - 📉 Visualized performance trends using **Matplotlib** and **Seaborn**.  
        - 📁 Added **CSV export** and **batch prediction** for classroom-level evaluation.  
        - 🌐 Deployed with **Streamlit Sharing**, featuring mobile responsiveness and **Lottie animations**.  
        """)

    with st.expander("💰 Income Tax Calculator (India)"):
        st.markdown("### 🧾 Description")
        st.write("An interactive web-based calculator to estimate personal income tax based on the Indian Old and New Tax Regimes.")
        st.markdown("### 📋 Project Summary")
        st.write("""
        - 📥 Takes user input: **Name, Age, Annual Income**, and **Regime Type**
        - 🔢 Implements **Indian tax slab logic** for different age groups and regimes
        - 📈 Visualizes results with:
            - **Pie Chart** for income breakdown
            - **Bar Chart** comparing income, tax, and net income
        - 🚨 Handles missing input cases with warnings
        - 🔁 Real-time tax computation with dynamic UI using Streamlit
        - 🧠 Built using Python, Streamlit, and Matplotlib for data visualization
        - 💡 Suitable for individuals, financial advisors, or learning projects
        """)

# ----- Education -----
with tabs[5]:
    st.header("🎓 Education")
    st.markdown("""
**📚 B.Tech in Computer Science Engineering**  
🏫 *G. Pullaiah College of Engineering & Technology, Kurnool – April 2024*  
📈 *Final Year CGPA:* **5.8**

Key Learnings: 
- 💡 Capstone project on Machine Learning 
""")

# ----- Contact -----
with tabs[6]:
    st.header("📬 Contact Me")
    st.markdown("If you'd like to get in touch, feel free to reach out via:")

    with st.form(key="contact_form"):
        name = st.text_input("🧑 Your Name")
        email = st.text_input("📧 Your Email")
        message = st.text_area("✉️ Your Message")
        submit = st.form_submit_button("📨 Send Message")

        if submit:
            st.success("✅ Thank you! I will get back to you soon.")
