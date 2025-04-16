import os

folders = [
    'sms_ocr_pdf',
    'screenshots'
]
files = {
    'sms_ocr_pdf/__init__.py': '',
    'sms_ocr_pdf/extractor.py': '# Your OCR script goes here\n',
    'main.py': 'from sms_ocr_pdf.extractor import run_ocr_pipeline\n\nif __name__ == "__main__":\n    run_ocr_pipeline()',
    'requirements.txt': 'pytesseract>=0.3.10\nPillow>=9.0.0\nreportlab>=3.6.0\n',
    '.gitignore': '__pycache__/\n*.pyc\n*.log\ntext_message_transcript.pdf',
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content)

print("📁 Project scaffold created!")
