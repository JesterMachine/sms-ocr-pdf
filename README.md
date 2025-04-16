

```
# 📱 Text Message OCR Extractor

A Python tool that extracts text from screenshots of text message conversations using OCR (Optical Character Recognition) and compiles them into a searchable, neatly formatted PDF transcript.

---

## 📚 Table of Contents
- [Overview](#overview)
- [Use Cases](#use-cases)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Features](#features)
- [Limitations](#limitations)
- [Processing Time](#processing-time)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)

---

## 📖 Overview

This script processes a folder of image files (e.g., `.jpg` or `.png`) that contain text message screenshots. It uses Tesseract OCR to extract the text and creates a single PDF file containing the entire transcript.

---

## 🧰 Use Cases

- Archiving text message conversations for legal or personal documentation  
- Creating searchable PDFs from phone screenshots  
- Extracting texts for analysis, annotation, or records  
- Processing visual data for court or academic submission  

---

## ⚙️ Requirements

- **Python** 3.6 or higher  
- **Tesseract OCR** installed on your system  
- Python libraries:
  - `pytesseract`
  - `Pillow`
  - `reportlab`
  - `shutil` (part of the standard library)

---

## 🛠️ Installation

### Install Python

Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/).

### Install Tesseract OCR

- **Windows**:  
  Download the UB Mannheim Tesseract build from [github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

- **macOS**:
  ```bash
  brew install tesseract
  ```

- **Linux**:
  ```bash
  sudo apt install tesseract-ocr
  ```

### Install Python Dependencies

```bash
pip install pytesseract pillow reportlab
```

---

## 🚀 Usage

### 1. Place screenshots in a folder

Put all your `.png`, `.jpg`, or `.jpeg` message images into a directory.

### 2. Update the `image_folder` path in the script

```python
# Windows
image_folder = r"C:\path\to\your\screenshots"

# macOS/Linux
image_folder = "/path/to/your/screenshots"
```

### 3. (Optional) Set Tesseract executable path (Windows only)

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 4. Run the script

```bash
python sms-ocr-pdf.py
```

### 5. Output

A file named `text_message_transcript.pdf` will be created in the **same directory as the script**.

---

## 📝 Example Output

```text
--- screenshot_001.png ---
John: Hey, are you free this weekend?
12:34 PM · Oct 1, 2023

Jane: Maybe! Let me check.
12:35 PM · Oct 1, 2023
```

---

## ✅ Features

- Supports PNG and JPG image formats
- Outputs a clean, searchable `.pdf` transcript
- Preserves message order and line breaks
- Includes file headers to identify original screenshot
- Uses binarization and grayscale for OCR clarity
- Works offline – your data stays private

---

## ⚠️ Limitations

- OCR accuracy depends on image clarity and contrast  
- May struggle with low-quality screenshots or emoji-heavy texts  
- Not designed to reconstruct full message bubbles or app UI  

---

## ⏳ Processing Time

Processing time depends on:

- Number of images (e.g., 800+ screenshots may take 15–30 minutes or more)
- Image resolution and size
- Your computer's processing power

---

## 🛠️ Troubleshooting

- **Tesseract not found**:  
  Double-check that Tesseract is installed and its path is correctly set in the script (especially on Windows).

- **Poor OCR results**:  
  Use high-contrast, readable screenshots. Avoid blurred images or those with overlays.

- **Missing dependencies**:  
  Re-run:
  ```bash
  pip install pytesseract pillow reportlab
  ```

- **Weird formatting in output**:  
  Try cleaning your images with a pre-processing script or increasing contrast manually.

---

## 📄 License

MIT License. See the [LICENSE](./LICENSE) file for full terms.

---

## 🤝 Contributing

Contributions, suggestions, and issue reports are always welcome!  
Feel free to open an [issue](https://github.com/JesterMachine/sms-ocr-pdf/issues) or submit a pull request.

---
```

---

