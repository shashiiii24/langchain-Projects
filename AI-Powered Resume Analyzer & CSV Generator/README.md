# 📄 AI-Powered Resume Analyzer & CSV Generator using LangChain

An AI-powered application that extracts structured information from multiple PDF resumes and converts them into a single CSV file. The system processes resumes in bulk by accepting a ZIP file and uses a Large Language Model (LLM) via LangChain to transform unstructured resume text into structured data.

---

## 🚀 Features

- Upload a ZIP file containing multiple PDF resumes  
- Extract text from PDF resumes using PyMuPDF  
- Convert unstructured resume text into structured data using LangChain + Gemini  
- Extract key candidate details such as:
  - Professional summary  
  - Skills  
  - Experience (if available)  
  - Email address  
  - Mobile number  
  - Links (GitHub, LinkedIn, portfolio)  
- Export all extracted data into a downloadable CSV file  
- Interactive web interface built with Streamlit  

---

## 🧠 How It Works

1. User uploads a ZIP file containing PDF resumes  
2. Each PDF is extracted and converted into plain text  
3. The extracted text is passed to a Gemini LLM using LangChain  
4. The model structures the resume content into predefined fields  
5. All resumes are consolidated into a single CSV file  

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – Web interface  
- **LangChain** – LLM orchestration  
- **Gemini API** – Resume data extraction  
- **PyMuPDF** – PDF text extraction  
- **Pandas** – CSV generation  
- **ZIP handling** – Batch resume processing  

---

## 📂 Project Structure

```bash
resume_to_csv/
│── main.py
│── requirements.txt
│── assets/
│ └── background.png
│── README.md
```


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/resume-to-csv.
```
---
## 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

##3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
---
## 🔐 Environment Variables

### Create a .env file in the project root:
```bash
GOOGLE_API_KEY=your_gemini_api_key
```
---
## ▶️ Run the Application 
```bash
streamlit run main.py
```
### Then open the URL shown in the terminal (usually http://localhost:8501).
---
## 📊 Output

- Extracted resume data is displayed in a table

- A CSV file containing structured resume information can be downloaded directly

## 🎯 Use Cases

- Resume data extraction

- HR data preparation

- Candidate information analysis

- Resume parsing automation

## 🚧 Future Enhancements

- Job description-based resume ranking

- Skill normalization and validation

- Support for additional file formats

- Cloud deployment

## 🤝 Contributing

- Contributions, suggestions, and improvements are welcome.
- Feel free to fork the repository and submit a pull request.

## 📬 Contact

#### If you’d like to discuss this project or collaborate, feel free to connect on LinkedIn or GitHub.



# 📺 sample Images
!img["C:\Users\Shashi Kiran T\OneDrive\画像\Screenshots\Screenshot 2025-12-23 232237.png"]





  







