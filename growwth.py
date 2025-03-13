# import streamlit as st 
# import pandas as pd
# import os
# from io import BytesIO

# # Page Config
# st.set_page_config(page_title="Data Sweeper", layout='wide')

# # Custom CSS
# st.markdown(
#     """
#     <style>              
#     .stApp{ 
#         background-color: black;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title & Description
# st.title("💿 Data Sweeper Sterling Integrator By Ahmed Raza Turk")
# st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

# # File Uploader
# uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"Unsupported file type: {file_ext}")
#             continue

#         # File Details
#         st.write(f"🔍 Preview: {file.name}")
#         st.dataframe(df.head())

#         # Data Cleaning Options
#         st.subheader("🛠️ Data Cleaning Operations")
#         if st.checkbox(f"Clean data for {file.name}"):
#             col1, col2 = st.columns(2)

#             with col1:
#                 if st.button(f"Remove Duplicates ({file.name})"):
#                     df.drop_duplicates(inplace=True)
#                     st.write("✅ Duplicates removed!")

#             with col2:
#                 if st.button(f"Fill Missing Values ({file.name})"):
#                     numeric_cols = df.select_dtypes(include=['number']).columns
#                     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#                     st.write("✅ Missing values filled!")

#         # Select Columns
#         st.subheader("🎯 Select Columns to Keep")
#         columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
#         df = df[columns]

#         # Data Visualization Placeholder
#         st.subheader("📊 Data Visualization")
#         if st.checkbox(f"Show visualization for {file.name}"):
#             st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

#         #Conversion options

#         st.subheader("🔄 Conversion Options")
#         conversion_type = st.radio(f"Convert {file.name} to:", ["CVS" , "Excel"], key=file.name)
#         if st.button(f"Convert{file.name}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to.csv(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".csv")
#                 mime_type = "text/csv"

#             elif conversion_type == "Excel":
#                 df.to.to_excel(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".xlsx")
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             buffer.seek(0)

#             st.download_button(
#                 label=f"Download {file.name} as {conversion_type}",
#                 data=buffer,
#                 file_name=file_name,
#                 mime=mime_type
#             )
# st.success("🎉 All files processed succcessfully!")            











































import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import random
import time

# Set up the page
st.set_page_config(page_title="📂 Data Sweeper + Growth Mindset Hub", layout='wide')

# Custom Background Style for Responsiveness
st.markdown(
    """
    <style>
        body {
            background-color: #0d1b2a;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #1b263b;
            color: white;
        }
        .stApp {
            padding: 20px;
        }
        h1, h2, h3 {
            color: #f4a261;
        }
        .stButton>button {
            background-color: #e76f51;
            color: white;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
option = st.sidebar.radio("Go to", ["Data Sweeper", "Growth Mindset Hub", "🎉 Success Celebration"])

if option == "Data Sweeper":
    st.title("🧹 Data Sweeper")
    st.write("🔄 Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")
    
    # Upload files
    uploaded_files = st.file_uploader("📄 Upload files (CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)
    
    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()

            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"❌ Unsupported file type: {file_ext}")
                continue

            # Display file info
            st.write(f"📝 *File Name:* {file.name}")
            st.write(f"📏 *File Size:* {file.size / 1024:.2f} KB")
            st.dataframe(df.head())
            
            # Data Cleaning
            if st.checkbox(f"🧹 Clean Data for {file.name}"):
                if st.button(f"🚮 Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")
                if st.button(f"🩹 Fill Missing Values for {file.name}"):
                    for col in df.select_dtypes(include=['number']).columns:
                        df[col].fillna(df[col].mean(), inplace=True)
                    st.write("✅ Missing values filled!")
            
            # Data Visualization
            if st.checkbox(f"📊 Show Data Visualization for {file.name}"):
                st.write("### Data Distribution")
                num_cols = df.select_dtypes(include=['number']).columns
                if len(num_cols) > 0:
                    fig, ax = plt.subplots(figsize=(6, 4))
                    sns.histplot(df[num_cols[0]], bins=20, kde=True, ax=ax)
                    st.pyplot(fig)
                else:
                    st.write("⚠ No numeric columns to visualize.")
            
            # Conversion Options
            conversion_type = st.radio(f"Convert {file.name} to", ["Excel", "CSV"], key=file.name)
            if st.button(f"🔄 Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                else:
                    df.to_excel(buffer, index=False)
                buffer.seek(0)
                st.download_button("⬇ Download File", data=buffer, file_name=f"converted.{conversion_type.lower()}" )

elif option == "Growth Mindset Hub":
    st.title("🌱 Growth Mindset Hub")
    st.write("Welcome")
    
    # User Profile Setup
    st.sidebar.subheader("👤 User Profile")
    name = st.sidebar.text_input("Enter your name:")
    goal = st.sidebar.text_input("Your growth goal:")
    focus = st.sidebar.selectbox("Main Focus Area", ["Productivity", "Creativity", "Resilience", "Learning New Skills"])
    
    tab1, tab2, tab3, tab4 = st.tabs(["🧠 Brain Quiz", "💡 Idea Generator", "📊 Growth Tracker", "🤖 AI Coach"])
    
    # Brain Quiz
    with tab1:
        st.subheader("📝 Growth Mindset Quiz")
        questions = [("Failure is a learning opportunity.", "True"),
                     ("Talent is fixed and cannot be developed.", "False"),
                     ("Challenges help us grow.", "True"),
                     ("Effort is more important than talent.", "True"),
                     ("Your mindset can change over time.", "True"),
                     ("You should avoid mistakes at all costs.", "False"),
                     ("Hard work can change your intelligence level.", "True"),
                     ("Asking for help is a sign of weakness.", "False"),
                     ("Your brain can form new connections and improve over time.", "True"),
                     ("People with a growth mindset embrace challenges.", "True"),
                     ("Feedback is a personal attack.", "False")]
        user_answers = {}
        for i, (q, ans) in enumerate(questions):
            user_answers[q] = st.radio(q, ["True", "False"], key=f"quiz_{i}")
        
        if st.button("📊 Submit Quiz & Show Results"):
            score = sum(1 for q, ans in questions if user_answers[q] == ans)
            st.write(f"✅ You got {score}/{len(questions)} correct!")
            st.balloons()
            st.success("🎉 Amazing! Keep pushing your limits! 🚀")

            # Idea Generator
    with tab2:
        st.subheader("💡 New Idea Generator")
        ideas = ["Think of a business that solves a daily problem.", "Invent a new productivity hack.", "Design a futuristic learning system."]
        if st.button("🔄 Generate Idea"):
            st.write(random.choice(ideas))
    
    
    # Growth Tracker
    with tab3:
        st.subheader("📊 Track Your Growth")
        mood = st.selectbox("How do you feel today?", ["😀 Happy", "😐 Neutral", "😞 Struggling"])
        user_input = st.text_area("Write about your progress:")
        if st.button("📌 Save Entry"):
            st.success(f"✅ Saved, {name}! Keep Growing!")
            st.balloons()
            st.line_chart([random.randint(1, 10) for _ in range(10)])

             # AI Motivational Coach
    with tab4:
        st.subheader("🤖 Your AI Coach")
        responses = [
            "You are capable of amazing things! 🌟",
            "Mistakes help you grow. Keep going! 🚀",
            "Keep challenging yourself! You’re on the right path. 💪"
        ]
        if st.button("🔮 Get Motivation"):
            st.write(random.choice(responses))


elif option == "🎉 Success Celebration":
    st.title("🎊 Celebrate Your Success!")
    st.write("Success is even better when shared! Here are some ways to celebrate:")
    st.markdown("- 🎁 Help someone achieve their goal.")
    st.markdown("- 🎉 Host a small celebration with friends.")
    st.markdown("- 💡 Share your success story to inspire others.")
    if st.button("🎇 Celebrate Now!"):
        st.balloons()
        st.success("🎊 Keep achieving great things!")
