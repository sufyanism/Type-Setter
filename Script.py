import streamlit as st
import subprocess
import os
from docx import Document
import re
import tempfile
import shutil

# Typst template path
TEMPLATE = "templates/scholarly.typ"


# -----------------------------
# Check if Typst is installed
# -----------------------------
def check_typst():
    if shutil.which("typst") is None:
        st.error("Typst is not installed on this server.")
        st.stop()


# -----------------------------
# Parse DOCX file
# -----------------------------
def parse_docx(file):
    doc = Document(file)
    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text.strip())

    return "\n\n".join(text)


# -----------------------------
# Clean characters for Typst
# -----------------------------
def sanitize_text(text):
    text = re.sub(r'#', r'\\#', text)
    text = re.sub(r'\{', r'\\{', text)
    text = re.sub(r'\}', r'\\}', text)
    return text


# -----------------------------
# Inject manuscript into template
# -----------------------------
def inject_template(manuscript, temp_typ):

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    final = template.replace("{{MANUSCRIPT_CONTENT}}", manuscript)

    with open(temp_typ, "w", encoding="utf-8") as f:
        f.write(final)


# -----------------------------
# Compile Typst → PDF
# -----------------------------
def compile_pdf(temp_typ, temp_pdf):

    result = subprocess.run(
        ["typst", "compile", temp_typ, temp_pdf],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        st.error(result.stderr)
        return False

    return True


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Automated Typesetter")
st.write("Upload a DOCX manuscript and generate a print-ready PDF.")

check_typst()

uploaded_file = st.file_uploader("Upload DOCX File", type=["docx"])


if uploaded_file:

    if st.button("Generate PDF"):

        st.info("Processing manuscript...")

        # parse docx
        text = parse_docx(uploaded_file)

        # clean characters
        clean_text = sanitize_text(text)

        # create temporary working folder
        with tempfile.TemporaryDirectory() as temp_dir:

            temp_typ = os.path.join(temp_dir, "book.typ")
            temp_pdf = os.path.join(temp_dir, "book.pdf")

            # create typst file
            inject_template(clean_text, temp_typ)

            # compile pdf
            success = compile_pdf(temp_typ, temp_pdf)

            if success and os.path.exists(temp_pdf):

                st.success("PDF generated successfully!")

                with open(temp_pdf, "rb") as f:

                    st.download_button(
                        label="Download Typeset PDF",
                        data=f,
                        file_name="typeset_output.pdf",
                        mime="application/pdf"
                    )

            else:
                st.error("PDF generation failed.")
