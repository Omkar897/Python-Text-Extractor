Python Text Extractor
📌 A Python-based text extractor designed to extract text from medical documents and store it in key-value pairs.

🚀 Features
Extracts text from medical documents (PDFs, images, etc.)

Uses PyTesseract for Optical Character Recognition (OCR)

Supports preprocessing using OpenCV (grayscale, thresholding, noise removal)

Stores extracted data in structured key-value format

Optionally saves output to Excel/CSV

🛠 Tech Stack
Python

PyTesseract (OCR)

OpenCV (Image Processing)

Pandas (Data Handling)

Streamlit (Optional: UI for visualization)

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Omkar897/Python-Text-Extractor.git
cd Python-Text-Extractor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure Tesseract OCR is installed:

Download from: Tesseract OCR

Add its path to your system environment variables

📜 Usage
Run the extractor on an image/PDF:

bash
Copy
Edit
python extract_text.py --input document.png --output result.json
For UI-based extraction (using Streamlit):

bash
Copy
Edit
streamlit run app.py

🏗 Future Enhancements
✅ Improve OCR accuracy with deep learning models
✅ Add support for handwritten text extraction
✅ Deploy as a web app for easy access

