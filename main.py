import streamlit as st
import pypdf
import io
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")


st.set_page_config(page_title="AI Resume critiquer", page_icon="📃", layout="centered")
st.markdown("""
<style>

/* Background */
.stApp {
    background: #F5FEFD;
}

  h1 {
    font-size: 3.2rem !important;  
}

p, label {
    font-size: 18px !important;
}

/* Main container */
.block-container {
    max-width: 700px;
    padding-top: 5rem;
    padding-bottom: 2rem;
}
/* Button */
.stButton > button {
    width:100%;
    height:50px;
    border-radius:14px;
    font-size:18px;
    font-weight:700;
}

.stButton > button:hover {
    transform:scale(1.02);
    transition:0.2s;
}
</style>
""", unsafe_allow_html=True)

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")


uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf","txt"])
job_role = st.text_input("🎯 Enter the job role you are targeting (optional)", placeholder="e.g. Data Analyst, ML Engineer, Software Developer")

analyze = st.button("🚀 Analyze Resume")



def extract_text_from_pdf(uploaded_file):
    pdf_reader = pypdf.PdfReader(uploaded_file)
    text=""
    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text+"\n"
    return text  

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        prompt=f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills Presentation
        3. Experience description
        4. Specific improvements for {job_role if job_role else 'general job applications'}   

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations."""
   
        with st.spinner("🔍 Analyzing your resume..."):
          client = Groq(api_key=GROQ_API_KEY)
          response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages=[
                {"role": "system","content":"You are an expert resume reviewer with years of experience."},
                {"role":"user","content":prompt}
                ],
                temperature=0.7,
                max_tokens=1000
          )
        st.success("Analysis Complete ✅")

      
        st.markdown("### 📊 Analysis Results")
        st.markdown(response.choices[0].message.content)
        


    except Exception as e:
        st.error(f"An error occured: {str(e)}")

       

