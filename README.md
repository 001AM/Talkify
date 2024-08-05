# Django Text-to-Speech Converter

## Introduction
This project is a simple web application built using Django that converts text input into speech using the gTTS (Google Text-to-Speech) library. Users can enter text, and the application will generate an audio file of the spoken text.

## Features
- Text input form
- Text-to-speech conversion using gTTS
- Downloadable audio file

## Tech Stack
- **Backend:** Django
- **Text-to-Speech:** gTTS

## Installation

### Prerequisites
- Python 3.8+

### Setup Instructions
1. **Clone the repository:**
    ```bash
    git clone https://github.com/001AM/Talkify.git
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage
1. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000`.

2. **Convert text to speech:**
   Enter the text you want to convert into speech in the input form and submit. The application will generate an audio file that you can download and listen to.
