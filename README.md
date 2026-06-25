🤖 AI Resume Analyzer
  An AI-powered Resume Analyzer built using Streamlit and Groq LLM. It identifies strengths and weaknesses, and receive actionable suggestions for improvement.

✨ Features

  Upload PDF resumes
  AI-powered resume analysis
  Skill assessment
  Resume improvement suggestions
  ATS-friendly feedback
  Fast analysis using Groq 
  Simple and interactive Streamlit interface

⚙️ How It Works
1️⃣ Upload Resume
2️⃣ Extract Resume Content
3️⃣ Send Data to AI
4️⃣ AI Analysis
5️⃣ Generate Feedback  
6️⃣ Display Results

🛠️ Tech Stack
    Python
    Streamlit
    Groq API
    PyPDF
    Python Dotenv

📦 Installation

Clone Repository

git clone https://github.com/yourusername/resumeanalyzer.git
cd resumeanalyzer
Create Virtual Environment
python -m venv .venv

Activate Environment
Windows:
.venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Configure API Key

Create a .env file:

GROQ_API_KEY=your_api_key

Run Application
streamlit run main.py

Project Structure
resumeanalyzer/
├── main.py
├── requirements.txt
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
└── .env.example    

👨‍💻 Author
Deepa Yadav