# Lumina AI

### See Beyond the Pixels

Lumina AI is an AI-powered image analysis web application that transforms visual content into meaningful insights. Built using Streamlit and NVIDIA NIM, the application leverages multimodal vision-language models to analyze uploaded images and generate intelligent descriptions, summaries, object detections, and scene explanations in real time.

---

## 🚀 Live Demo

🔗 **Live Application:** [https://lumina-vision.streamlit.app/]

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
   * Summarize Image
   * Detect Objects
   * Explain Scene
3. Click **Generate Analysis**.
4. The image is processed by NVIDIA's multimodal vision model.
5. AI-generated insights are displayed instantly.
6. Download the generated report if needed.

---

## Screenshot

### Application Interface

![Lumina AI Interface](screenshot/image.png)

---

## Project Structure

```text
Lumina-AI/
│
├── .streamlit/
│   └── config.toml
│
├── screenshot/
│   └── image.png
│
├── app.py
├── moon.png
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Lumina-AI.git
cd Lumina-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
NVIDIA_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run app.py
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
