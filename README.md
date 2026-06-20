# 🖐️ Final_AI_Palmistry_Group-6

## 📖 Description

**Final_AI_Palmistry_Group-6** is an AI-powered Palmistry Analysis web application developed as a final course project. The system integrates Computer Vision, Machine Learning, and Palmistry-based analysis techniques to process palm images and generate intelligent interpretations.

Users can upload a palm image, and the application automatically extracts hand features, analyzes palm characteristics, predicts personality traits, provides career recommendations, and generates summarized reports based on detected palm patterns.

---

## ✨ Main Features

✔ Upload and process palm images

✔ Palm feature extraction and analysis

✔ AI-based personality prediction

✔ Career recommendation system

✔ Automated report generation

✔ Result summary and interpretation

✔ User-friendly web interface

---

## 📂 Project Structure

```text
Final_AI_Palmistry_Group-6
│
├── AI_model/
│   ├── pretrained/
│   │   ├── traits_model.pkl
│   │   └── feature_columns.pkl
│   │
│   ├── prediction/
│   │   └── predict_palm.py
│   │
│   └── training/
│       └── .gitkeep
│
├── dataset/
│   └── .gitkeep
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── images/
│   │   └── .gitkeep
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── report.html
│
├── engines/
│   ├── analysis_engine.py
│   ├── career_engine.py
│   └── summary_engine.py
│
├── reports/
│   ├── report_generator.py
│   └── .gitkeep
│
├── utils/
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```
---

## 📥 Dataset & Model Download

> **Important Note**
>
> Due to GitHub file size limitations, some project files are not included in this repository because they exceed the upload size limit.
>
> Please download the required files from the links below before running the application.

### Dataset

Download the dataset folder here:

Dataset Link:
https://drive.google.com/drive/folders/17pfKczN4mosIfYdY8pJK_lf4jGom6Bao?usp=sharing

After downloading, place the folder inside:

```text
Final_AI_Palmistry_Group-6/
└── dataset/
```

### Trained Model

Download the pretrained model (`traits_model.pkl`) here:

Model Link:
https://drive.google.com/drive/folders/1xAH-mObcpcQNbbJrXdEPvHYl2TA4_TY4?usp=sharing

After downloading, place the file inside:

```text
Final_AI_Palmistry_Group-6/
└── traits_model.pkl
```
