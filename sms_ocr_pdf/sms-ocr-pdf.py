import os
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# Explicitly set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Directory with text message images
image_folder = r"C:\Users\adamj\Downloads\Wendy texts -20250415T051215Z-001\Wendy texts"

# Output PDF file
output_pdf = "text_message_transcript.pdf"

# Grab and sort image files
image_files = sorted([
    os.path.join(image_folder, f)
    for f in os.listdir(image_folder)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

# OCR with preprocessing
all_text = ""
for file in image_files:
    try:
        img = Image.open(file)
        # Preprocess: grayscale and binarize
        img = img.convert("L")  # Grayscale
        img = img.point(lambda x: 0 if x < 128 else 255, "1")  # Binarize
        text = pytesseract.image_to_string(img, config="--psm 6")  # Assume block of text
        all_text += f"\n--- {os.path.basename(file)} ---\n{text}\n"
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Write to PDF with proper text wrapping
c = canvas.Canvas(output_pdf, pagesize=LETTER)
width, height = LETTER
margin = inch * 0.5
text_width = width - 2 * margin
c.setFont("Helvetica", 10)  # Set font explicitly
textobject = c.beginText(margin, height - margin)
textobject.setLeading(12)  # Line spacing

lines = all_text.split("\n")
for line in lines:
    # Wrap text to fit page width
    wrapped_lines = c.drawStringSplitter().split(line, text_width)
    for wrapped in wrapped_lines:
        if textobject.getY() < margin:
            c.drawText(textobject)
            c.showPage()
            textobject = c.beginText(margin, height - margin)
            textobject.setLeading(12)
        textobject.textLine(wrapped)

c.drawText(textobject)
try:
    c.save()
    if os.path.exists(output_pdf):
        print(f"✅ Transcript saved as: {output_pdf}")
    else:
        print(f"❌ Failed to create {output_pdf}")
except PermissionError as e:
    print(f"❌ Permission error saving PDF: {e}")