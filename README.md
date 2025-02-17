# AI-AIsist for Troubleshooting

[![Deployed on Render](https://img.shields.io/badge/Render-Deployed-blue?style=flat&logo=render)](https://ai-aissit-for-troubleshooting.onrender.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)

<p align="center">
  <img src="https://github.com/user-attachments/assets/aa214b3b-9c62-4fbd-9d0c-858afd7ff6c6" alt="AI-AI-Sist Banner" style="max-width:100%;">
</p>

---

## Overview

**AI-AI-Sist for Troubleshooting** is a web application designed to diagnose and resolve common technical issues.  It uses Natural Language Processing (NLP) with spaCy, machine learning with scikit-learn, and optionally, AI-powered insights from the OpenAI API.  The interface is designed to be modern and intuitive.

**Live Demo:** [ai-aissit-for-troubleshooting.onrender.com](https://ai-aissit-for-troubleshooting.onrender.com)

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Intelligent Diagnosis:** Uses spaCy and scikit-learn to understand natural language input and diagnose technical problems.
- **Troubleshooting Steps:** Provides troubleshooting steps for common issues (printer problems, slow computers, network issues, etc.).
- **Fallback Mechanism (Optional):**  If no direct match is found, the application can use a web search (Google) or the OpenAI API (if configured) to find solutions.
- **Modern UI/UX:**  Responsive design with HTML5 and CSS3.
- **Cloud Deployment:** Hosted on Render.

---

## Architecture

The application uses the following technologies:

- **Backend:** Python and Flask.
- **NLP & Machine Learning:**
    - spaCy
    - scikit-learn (TF-IDF Vectorization, Multinomial Naive Bayes)
- **AI Integration (Optional):** OpenAI API (`text-davinci-003` engine).
- **Web Search:** `googlesearch-python` package.
- **Frontend:** HTML5, CSS3, Google Fonts.
- **Deployment:** Render.

---

## Installation

### Prerequisites

- **Python 3.7+**
- **Git**
- **Virtual Environment (recommended)**

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Tillu6/ai-aissit-for-troubleshooting.git
   cd ai-aissit-for-troubleshooting
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the spaCy Model (if not already installed):**

   The application auto-downloads `en_core_web_sm` if missing. Alternatively, run:

   ```bash
   python -m spacy download en_core_web_sm
   ```

---

## Configuration

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Adjust any additional configuration settings directly within `app.py` as required.

---

## Usage

To run the application locally, execute:

```bash
python app.py
```

Then, open your browser and navigate to [http://localhost:5000](http://localhost:5000) to start troubleshooting.

---

## Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/203b8249-dff0-49fc-8313-e8f653b33c0f" alt="Futuristic Interface Preview" style="max-width:100%;">
</p>


---

## Project Structure

```plaintext
ai-aissit-for-troubleshooting/
├── app.py                  # Main Flask application and backend logic
├── templates/
│   └── index.html          # Frontend HTML template
├── requirements.txt        # List of Python dependencies
├── .env                    # Environment variables (excluded from version control)
└── README.md               # This documentation file
```

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork** the repository.
2. Create a new branch:  
   `git checkout -b feature/YourFeature`
3. **Commit** your changes:  
   `git commit -am 'Add new feature'`
4. **Push** to your branch:  
   `git push origin feature/YourFeature`
5. **Open a Pull Request** describing your changes.

For significant changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- **[spaCy](https://spacy.io/):** For delivering powerful natural language processing capabilities.
- **[scikit-learn](https://scikit-learn.org/):** For its user-friendly machine learning implementations.
- **[OpenAI](https://openai.com/):** For providing AI-driven insights that power our fallback mechanism.
- **[Flask](https://flask.palletsprojects.com/):** For enabling a lightweight yet robust web framework.
- **[Render](https://render.com/):** For hassle-free cloud deployment.
- **[Google Search API](https://pypi.org/project/googlesearch-python/):** For integrated web search functionality.

---

Embrace the future of troubleshooting with **AI-AI-Sist for Troubleshooting** – where innovative technology meets next-generation design.
```
