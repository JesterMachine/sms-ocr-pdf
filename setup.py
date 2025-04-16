from setuptools import setup, find_packages

setup(
    name="sms-ocr-pdf",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytesseract>=0.3.10",
        "Pillow>=9.0.0",
        "reportlab>=3.6.0"
    ],
    author="JesterMachine",
    author_email="your@email.com",
    description="Extracts text from SMS screenshots and outputs a searchable PDF transcript.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JesterMachine/sms-ocr-pdf",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Utilities"
    ],
    python_requires='>=3.6',
)
