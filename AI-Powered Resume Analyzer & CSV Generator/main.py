import streamlit as st
import os
import zipfile
import pandas as pd
import pymupdf
from dotenv import load_dotenv
from typing import TypedDict, Optional, Annotated
from langchain_google_genai import ChatGoogleGenerativeAI

# BACKGROUND IMAGE ----------------
import base64

def add_bg_from_local(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local(r"C:\Users\Shashi Kiran T\Downloads\Gemini_Generated_Image_2gexmi2gexmi2gex.png")


# LOAD ENV
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("api")

# UI 
st.set_page_config(page_title="Resume ZIP to CSV Converter", layout="wide")
st.title(":rainbow[AI-Powered Resume Analyzer & CSV Generator]")
st.subheader("📄 :red[Resume ZIP → CSV Converter]")

 # File uploader 
st.write("Upload a ZIP file containing multiple resume PDFs.")
uploaded_file = st.file_uploader("Upload ZIP file", type=["zip"])

# PDF TEXT EXTRACTION 
def extract_text_from_pdf(uploaded_zip):
    texts = []
    with zipfile.ZipFile(uploaded_zip) as z:
        for filename in z.namelist():
            if filename.lower().endswith(".pdf"):
                with z.open(filename) as f:
                    doc = pymupdf.open(stream=f.read(), filetype="pdf")
                    text = ""
                    for page in doc:
                        text += page.get_text()
                    texts.append(text)
    return texts

# STRUCTURED OUTPUT ----------------
class DataFormat(TypedDict):
    Name: str
    Mobile_number: Optional[int]
    email: str
    experince: Optional[int]
    skills: list[str]
    links: Annotated[list[str], "Extract any links if present"]
    summary: str

# MODEL ----------------
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
structured_model = model.with_structured_output(DataFormat)

# PROCESS ----------------
if uploaded_file:
    texts = extract_text_from_pdf(uploaded_file)

    results = []

    for text in texts:
        prompt = f"""
        Extract the following details from this resume text:

        Resume Text:
        {text}
        """
        response = structured_model.invoke(prompt)
        results.append(response)

        print(response)

    # Convert to DataFrame
    df = pd.DataFrame(results)

    st.dataframe(df)

    st.download_button(
        "⬇ Download CSV",
        data=df.to_csv(index=False),
        file_name="resumes.csv",
        mime="text/csv"
    )

