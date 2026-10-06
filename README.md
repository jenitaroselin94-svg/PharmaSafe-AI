# PharmaSafe AI – Medicine Label Safety Checker

PharmaSafe AI is an AI-based medicine label safety checker that uses Optical Character Recognition (OCR) to extract and analyze important information from medicine labels.

## About the Project

Medicine labels contain important information such as medicine name, dosage, expiry date, storage instructions, warnings, and precautions. PharmaSafe AI allows users to upload a medicine label image and automatically extracts the visible text using OCR. The extracted information is then checked for important safety-related details.

## Features

- Upload medicine label images
- Extract text from medicine labels using OCR
- Detect expiry information
- Detect dosage information
- Detect storage instructions
- Detect warnings and precautions
- Identify prescription medicine indicators
- Display extracted label information
- Highlight missing or undetected safety information

## Technologies Used

- Python
- Streamlit
- Tesseract OCR
- Pytesseract
- Pillow

## Working

The user uploads a clear medicine label image. The image is processed using Tesseract OCR to extract the text. PharmaSafe AI then checks the extracted text for important safety information such as expiry, dosage, storage instructions, warnings, and prescription indicators. The detected information and warnings are displayed in the application.

## Project Structure

PharmaSafe-AI/
- app.py
- ocr.py
- safety_checker.py
- requirements.txt
- README.md

## How to Run

Install the required Python packages:

    python -m pip install -r requirements.txt

Run the application:

    streamlit run app.py

After running the application, upload a clear medicine label image and click the "Check Medicine Label" button to view the extracted information and safety warnings.

## Live Demo
https://pharmasafe-ai-agsmwlq3stmhyamxjakvmm.streamlit.app/
<img width="992" height="901" alt="Screenshot 2026-10-06 081018" src="https://github.com/user-attachments/assets/539ff029-8748-4130-bf1d-a6c0f04f5f45" />
<img width="970" height="782" alt="Screenshot 2026-10-06 081057" src="https://github.com/user-attachments/assets/ea68f7e5-9087-41a2-8485-5b2aec7bf1ed" />
<img width="931" height="392" alt="Screenshot 2026-10-06 081111" src="https://github.com/user-attachments/assets/8f73d2ce-298d-422c-b684-7e6277b658d6" />

## Future Enhancements

- Automatic expiry date calculation
- Medicine name recognition
- Barcode and QR code scanning
- Medicine information database integration
- Multilingual OCR support
- Improved OCR accuracy
- AI-based medicine verification

## Note

PharmaSafe AI is an educational prototype developed for medicine label information checking. It does not provide medical diagnosis, prescribe medicines, or replace professional advice from a qualified doctor or pharmacist.
