import streamlit as st
import subprocess
import os
from docx import Document
import re
import tempfile

TEMPLATE = "templates/zeba_style.typ"


def parse_docx(file):
    doc = Document(file)
    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text.strip())

    return "\n\n".join(text)


def sanitize_text(text):
    text = re.sub(r'#', r'\\#', text)
    text = re.sub(r'\{', r'\\{', text)
    text = re.sub(r'\}', r'\\}', text)
    return text


def inject_template(manuscript, temp_typ):
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    final = template.replace("{{MANUSCRIPT_CONTENT}}", manuscript)

    with open(temp_typ, "w", encoding="utf-8") as f:
        f.write(final)


def compile_pdf(temp_typ, output_pdf):
    subprocess.run(["typst", "compile", temp_typ, output_pdf])


# Streamlit UI
st.title("Automated Typesetter")

st.write("Upload a DOCX manuscript and generate a print-ready PDF.")

uploaded_file = st.file_uploader("Upload DOCX File", type=["docx"])

if uploaded_file:

    if st.button("Generate PDF"):

        st.write("Processing manuscript...")

        # extract original filename
        original_name = os.path.splitext(uploaded_file.name)[0]
        output_name = f"{original_name}_typesetter.pdf"

        text = parse_docx(uploaded_file)
        clean_text = sanitize_text(text)

        with tempfile.TemporaryDirectory() as tmpdir:

            temp_typ = os.path.join(tmpdir, "book.typ")
            output_pdf = os.path.join(tmpdir, output_name)

            inject_template(clean_text, temp_typ)

            compile_pdf(temp_typ, output_pdf)

            st.success("PDF generated successfully!")

            with open(output_pdf, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name=output_name,
                    mime="application/pdf"
                )