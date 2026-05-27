# 🛡️ ThreatInbox
### 🔐 AI-Powered Phishing Email Detection System (Streaming ML + Flask)

ThreatInbox is a machine learning-based cybersecurity web application that detects phishing emails using NLP, URL analysis, and real-world streaming datasets — without requiring large dataset downloads.

---

# 📌 Overview

ThreatInbox classifies emails as:

- ⚠️ Phishing
- ✅ Safe

It combines:

- Natural Language Processing (TF-IDF)
- URL feature extraction
- Real-world streaming datasets
- Flask web interface

---

# ⚡ Features

| 🤖 Machine Learning | 🌐 Web Application | ⚡ Real-World Dataset System |
|---------------------|-------------------|------------------------------|
| TF-IDF text vectorization | Paste email text | Streaming dataset loading |
| URL extraction & analysis | Upload `.txt` email files | Batch-based training |
| Suspicious keyword detection | Instant prediction result | Real phishing patterns |
| Long URL detection | Clean UI with result page | Lightweight ML pipeline |
| Logistic Regression classifier |  |  |
| Confidence score prediction |  |  |

---

# 🧠 How It Works

```text
┌──────────────────────────────┐
│ User Input                   │
│ (Email Text / File Upload)   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Flask Backend                │
│ (ThreatInbox.py)             │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Feature Extraction           │
│ • TF-IDF Features            │
│ • URL + Keyword Features     │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ ML Model                     │
│ (pipeline.pkl)               │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Prediction Output            │
│ ⚠️ Phishing / ✅ Safe        │
└──────────────────────────────┘
```

---

# 🏗️ Project Structure

```text
ThreatInbox/
│
├── ThreatInbox.py                  # Flask Web App
├── ThreatInbox-train-model.py      # ML Training Script (Streaming)
├── pipeline.pkl                    # Saved Trained Model
├── emails.csv                      # Sample dataset (optional)
├── requirements.txt                # Dependencies
│
├── templates/
│   ├── index.html                  # Home Page
│   └── result.html                 # Result Page
│
├── static/
│   └── style.css                   # UI Styling
│
└── uploads/                        # Uploaded email files
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ThreatInbox.git
cd ThreatInbox
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install datasets
```

---

# 🧠 Training the Model (Streaming Mode)

ThreatInbox uses real-world streaming datasets (no full download required).

```bash
python ThreatInbox-train-model.py
```

### 🔥 What happens:

- Loads dataset using streaming API
- Fetches phishing emails in batches
- Extracts features (TF-IDF + URL analysis)
- Trains ML model
- Saves `pipeline.pkl`

---

# 🌐 Running the Web App

```bash
python ThreatInbox.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

# 📤 Usage

## ✍️ Option 1: Paste Email

Example:

```text
Your bank account has been suspended.
Click here: http://fake-login.com
```

Click **Analyze Email**

---

## 📁 Option 2: Upload File

- Upload `.txt` email file
- Click **Analyze Email**
- Get prediction instantly

---

# 📊 Output Example

## ⚠️ Phishing Email

```text
Prediction: Phishing
Confidence: 96.3%
```

## ✅ Safe Email

```text
Prediction: Safe
Confidence: 92.1%
```

---

# 🧪 Machine Learning Features

| Feature | Description |
|----------|-------------|
| TF-IDF | Converts email text into numerical vectors |
| URL Count | Number of links in email |
| Suspicious Words | Detects phishing intent |
| Long URLs | Detects hidden/masked links |
| Logistic Regression | Final classifier |

---

# ⚡ Real-World Dataset System

ThreatInbox uses streaming datasets instead of full downloads:

- ✅ Loads only required data
- ✅ Processes in batches
- ✅ No memory overload
- ✅ Real phishing patterns

---

# 🔐 Threat Detection Signals

ThreatInbox detects:

- Fake login pages
- Bank impersonation emails
- Password reset scams
- Urgency manipulation ("act now")
- Suspicious/masked URLs
- Credential theft attempts

---

# 📈 ML Pipeline Flow

```text
Streaming Dataset API
        ↓
Batch Loader (20K samples)
        ↓
Feature Extraction (TF-IDF + URL features)
        ↓
Model Training (Logistic Regression)
        ↓
Save Model (pipeline.pkl)
        ↓
Flask Prediction Engine
```

---

# 📦 Requirements

```text
flask
pandas
scikit-learn
joblib
numpy
datasets
```

---

# 🚀 Future Improvements

## 🤖 AI Enhancements

- BERT-based phishing detection
- Deep learning models
- Multi-class classification (spam/phishing/legit)

## 🔐 Security Enhancements

- VirusTotal API integration
- Domain reputation scoring
- Email header analysis
- SPF/DKIM validation

## 🌐 Web Enhancements

- User authentication system
- Admin dashboard
- Email history tracking
- Real-time monitoring system

---

# ☁️ Deployment Options

| Platform | Difficulty |
|-----------|------------|
| Render | ⭐ Easy |
| Railway | ⭐ Easy |
| PythonAnywhere | ⭐ Easy |
| Hugging Face Spaces | ⭐ Easy (ML friendly) |

---

# 👨‍💻 Author

ThreatInbox is a cybersecurity + machine learning project designed by adiiithyaan for real-world phishing detection using lightweight streaming datasets.

---

# ⭐ Final Note

> “Detect phishing smarter — without downloading massive datasets.”

---

# 📜 License

This project is proprietary and protected under a custom license.

Unauthorized copying, redistribution, or commercial usage is prohibited without permission.
