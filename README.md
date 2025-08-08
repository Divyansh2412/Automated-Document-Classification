# 📄 Automated Document Classification

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Contributions welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat)](../../issues)

An AI-powered system that classifies text documents into predefined categories using multiple Machine Learning algorithms.  
The project includes document preprocessing, feature extraction, model training, and evaluation — all integrated into a simple and scalable Python-based application.

---

## 🚀 Features
- **Automated Text Preprocessing**  
  Removes stopwords, punctuation, and performs tokenization for cleaner input data.
- **Multiple Classification Models**  
  - Naive Bayes  
  - K-Nearest Neighbors (KNN)  
  - Support Vector Machines (SVM)  
  - Decision Trees  
  - K-Means (unsupervised clustering)
- **Easy Dataset Management**  
  Through the `DatasetManager` module.
- **Scalable Code Structure**  
  Modular Python files for each model and preprocessing task.
- **Flask Integration**  
  Simple web interface to interact with the classification models.

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Divyansh2412/Automated-Document-Classification.git
cd Automated-Document-Classification
````

2. **Create a virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
Automated-Document-Classification/
│
├── app.py                       # Flask app for web interface
├── Main.py                      # Main script for model execution
├── DatasetManager.py            # Handles dataset loading and management
├── DocumentPreprocessing.py     # Text cleaning and preprocessing
├── NaiveBayes.py                 # Naive Bayes classifier
├── KNN.py                        # K-Nearest Neighbors classifier
├── SVM.py                        # Support Vector Machine classifier
├── DecisionTree.py               # Decision Tree classifier
├── KMeans.py                     # K-Means clustering
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

---

## ▶️ Usage

### Run from terminal:

```bash
python Main.py
```

### Run Flask web app:

```bash
python app.py
```

The web interface will be available at:
**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📊 Models & Evaluation

Each model is trained and tested using the preprocessed dataset.
The project compares model performance based on:

* Accuracy
* Precision
* Recall
* F1-score

---

## 📌 Requirements

All dependencies are listed in [`requirements.txt`](requirements.txt):

```
flask
joblib
matplotlib
nltk
numpy
pandas
scikit-learn
scipy
seaborn
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✨ Author

**Divyansh Miyan Bazaz**

* GitHub: [@Divyansh2412](https://github.com/Divyansh2412)
* LinkedIn: [Profile](https://www.linkedin.com/in/divyansh-miyan-bazaz-723792231/)

````

---

### **LICENSE File (MIT)**
Create a file named `LICENSE` in your project folder with:

```text
MIT License

Copyright (c) 2025 Divyansh Miyan Bazaz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
````

