# Final_AI_Palmistry_Group-6
DESCRIPTION
     Final_AI_Palmistry_Group-6 is an AI-powered Palmistry Analysis application developed as a final course project. The system 
uses computer vision, machine learning, and palmistry-based analysis techniques to process palm images and generate intelligent interpretations.

     Users can upload a hand image, and the application extracts palm features, analyzes palm characteristics, predicts
personality traits, provides career suggestions, and generates a summarized report based on the detected palm patterns.

MAIN FEATURES
- Upload and process palm images
- Palm feature extraction and analysis
- AI-based personality prediction
- Career recommendation system
- Automated report generation
- Result summary and interpretation
- User-friendly web interface

PROJECT STRUCTURE
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
