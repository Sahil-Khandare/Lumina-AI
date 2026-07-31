# Lumina AI

### See Beyond the Pixels

Lumina AI is an AI-powered image analysis web application that transforms visual content into meaningful insights. Built using Streamlit and NVIDIA NIM, the application leverages multimodal vision-language models to analyze uploaded images and generate intelligent descriptions, summaries, object detections, and scene explanations in real time.

---

## 🚀 Live Demo

🔗 **Live Application:** [https://lumina-vision.streamlit.app/]<br>
**Note:** The app is hosted on Streamlit Community Cloud and may take a few seconds to wake up if inactive.

---

## Features

* Upload JPG, JPEG, and PNG images
* Generate detailed image descriptions
* Create concise image summaries
* Detect and identify visible objects
* Explain scenes and visual context
* Download AI-generated analysis reports
* Modern space-themed user interface
* Real-time AI-powered image understanding

---

## Tech Stack

### Frontend

* Streamlit
* HTML/CSS
* Custom UI Styling

### Backend

* Python
* Requests
* Python Dotenv

### AI & Cloud

* NVIDIA NIM
* Llama 3.2 Vision Instruct Model

---

## Application Workflow

1. Upload an image.
2. Select an analysis mode:

   * Describe Image
   * Quick Summary
   * Detect Objects
   * Generate Caption
3. Click **Generate Analysis**.
4. The image is processed by NVIDIA's multimodal vision model.
5. AI-generated insights are displayed instantly.
6. Download the generated report if needed.

---

## Screenshot

### Application Interface

![Lumina AI Interface](screenshot/homepage.jpg)

---

## Project Structure

```text
Lumina-AI/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   └── moon.png
│
├── screenshot/
│   └── homepage.png
│
├── .dockerignore
├── Dockerfile
│
├── api.py
│
├── app.py
│
├── prompts.py
│
├── style.css
│
├── moon.png
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Run with Docker

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Lumina-AI.git
cd Lumina-AI
```

### 2. Create a `.env` file

```env
NVIDIA_API_KEY=YOUR_API_KEY
```

### 3. Build the Docker image

```bash
docker build -t lumina-ai .
```

### 4. Run the container

```bash
docker run -p 8501:8501 --env-file .env lumina-ai
```

### 5. Open the application

Visit:

```
http://localhost:8501
```

---

## 🔑 Environment Variables

| Variable       | Description        |
| -------------- | ------------------ |
| NVIDIA_API_KEY | NVIDIA NIM API Key |

---

## Use Cases

* Image Understanding
* Visual Content Analysis
* Educational Applications
* Accessibility Assistance
* Content Summarization
* AI-Powered Vision Systems

---

## Future Enhancements

* Support for additional image formats
* OCR (Text Extraction)
* Image Captioning Improvements
* Multi-image Analysis
* PDF Report Generation
* Chat-based Image Question Answering
* Improve caption generation by fine-tuning prompts or using a dedicated image-captioning model to generate concise, engaging, and context-aware captions.

---

## Author

**Sahil Khandare**

Engineering Student | AI & Machine Learning Enthusiast

---

## Acknowledgements

* NVIDIA NIM
* Meta Llama 3.2 Vision Model
* Streamlit
* Open Source AI Community

---

## 📜 License

This project is intended for educational and portfolio purposes.
