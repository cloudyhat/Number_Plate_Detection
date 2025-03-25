# Number_Plate_Detection
📌 Overview

This project is an Automatic Number Plate Recognition (ANPR) system that detects and extracts vehicle license plate numbers from images, real=time, and video feed using YOLOv7 deep learning model. It processes video frames, detects license plates, extracts text using OCR (Tesseract), and stores the results in a database.

📂 Project Structure

Number_Plate_Detection/
│── app.py                 # Flask app for web interface
│── main1.py               # Main script for number plate detection
│── create_db.py           # Script to create and initialize database
│── best.pt                # Trained YOLO model for number plate detection
│── car_plate_data.db      # SQLite database storing detected plate numbers
│── car_plate_data.txt     # Log file storing detected plate numbers
│── coco1.txt              # COCO class labels for YOLO
│── assets/
│   └── mycarplate.mp4     # Sample video for testing
│── templates/
│   ├── index.html         # Web UI homepage
│   ├── login.html         # Login page
│── styles.css             # Styles for the web interface

🚀 Features

Real-time Number Plate Detection using YOLO
OCR-based Text Extraction using Tesseract
Video Processing from a pre-recorded video
Database Storage for extracted plate numbers
Flask Web Interface for viewing detected plates

🎯 How It Works

Video Processing: Reads frames from mycarplate.mp4
YOLO Detection: Uses best.pt to detect license plates
OCR Extraction: Uses Tesseract OCR to read plate numbers
Database Logging: Saves extracted numbers in car_plate_data.db
Web UI Display: Flask app shows detected plates in real-time