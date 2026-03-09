# 🖨️ Zeba Type-Setter
**Zeba Type-Setter** is a specialized automation tool designed to transform raw manuscripts into print-ready PDFs. By leveraging the power of **Typst**, it provides a modern, fast, and high-precision alternative to traditional typesetting tools like LaTeX or Adobe InDesign.

This project is part of the Zeba publishing suite, aimed at simplifying the technical workflow for authors and independent publishers.

## 🚀 Features
* **DOCX to PDF**: Seamlessly convert Microsoft Word manuscripts into professional book layouts.
* **Typst Engine**: Built on the ultra-fast Typst compiler for near-instant PDF generation.
* **Auto-Sanitization**: Automatically escapes special characters (`#`, `$`, `@`, `_`) to ensure smooth compilation.
* **Integrated Metadata**: (Optional) Pairs with the Zeba Metadata Forge to ensure your book's interior matches its digital identifiers.
* **Web-Ready Interface**: Powered by Streamlit for a clean, browser-based drag-and-drop experience.

## 🛠️ Tech Stack
* **Language**: Python 3.10+
* **UI Framework**: [Streamlit](https://streamlit.io/)
* **Document Parsing**: `python-docx`
* **Typesetting Engine**: [Typst](https://typst.app/) (via `typst-bin`)

## 📂 Project Structure

```text
Type-Setter/
├── app.py                 # Core application logic and UI
├── requirements.txt       # Python dependencies
├── railway.json           # Cloud deployment configuration
├── assets/                # Branding and icons
└── README.md              # Documentation

```

## ⚙️ Installation & Usage

### Local Development

1. **Clone the repository**:
```bash
git clone https://github.com/sufyanism/Type-Setter.git
cd Type-Setter

```

2. **Install dependencies**:
The project requires the Typst binary, which is included in the `typst-bin` Python package for easy setup.
```bash
pip install -r requirements.txt

```


3. **Run the application**:
```bash
streamlit run app.py

```

### Using the Tool
1. Upload your manuscript in `.docx` format.
2. Review the automated cleanup logs.
3. Click **Generate PDF** to forge a print-ready A5/A4 document.

## ☁️ Deployment
This repository is optimized for **Railway.app**. It includes a `railway.json` file that automatically handles the Nixpacks build process and exposes the correct port for the Streamlit server.

1. Connect your GitHub account to Railway.
2. Select the `Type-Setter` repository.
3. Deploy. No manual environment variables are required.


## Screenshot
<img width="1058" height="856" alt="Type Setter" src="https://github.com/user-attachments/assets/4ce1af72-fd72-4177-9aa6-278edbfef56f" />

## Screencast
https://github.com/user-attachments/assets/40f249f8-9208-43a4-8bc8-be2e658e868c

## About Me 
✨ I’m **Sufyan bin Uzayr**, an open-source developer passionate about building and sharing meaningful projects.
You can learn more about me and my work at [sufyanism.com](https://sufyanism.com/) or connect with me on [Linkedin](https://www.linkedin.com/in/sufyanism)

## Your all-in-one learning hub! 
🚀 Explore courses and resources in coding, tech, and development at **zeba.academy** and **code.zeba.academy**. Empower yourself with practical skills through curated tutorials, real-world projects, and hands-on experience. Level up your tech game today! 💻✨

**Zeba Academy**  is a learning platform dedicated to **coding**, **technology**, and **development**.  
➡ Visit our main site: [zeba.academy](https://zeba.academy)   <br>
➡ Explore hands-on courses and resources at: [code.zeba.academy](https://code.zeba.academy)   <br>
➡ Check out our YouTube for more tutorials: [zeba.academy](https://www.youtube.com/@zeba.academy)  <br>
➡ Follow us on Instagram: [zeba.academy](https://www.instagram.com/zeba.academy/)  <br>

**Thank you for visiting!**
