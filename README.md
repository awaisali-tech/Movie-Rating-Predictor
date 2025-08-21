# 🎬 Movie-Rating-Predictor  
My first end-to-end machine learning pipeline project! 🚀  

## 📌 Overview  
This project predicts **IMDb movie ratings** using data fetched from a **RapidAPI endpoint**. It covers the full ML pipeline from data acquisition → preprocessing → modeling → evaluation → visualization.  

### Features  
- **Data Acquisition**: `data_from_api.py` pulls ~500 movies.  
- **Preprocessing**: `preprocess.py` and `data_preprocessing_1.py` clean data, handle genres, and engineer features (e.g., genre count).  
- **Modeling**: Tested Linear Regression (MSE: 0.25, R²: -0.09), Ridge, and Random Forest (MSE: 0.31, R²: -0.31) with cross-validation & hyperparameter tuning.  
- **Visualization**: `rating_vs_year.png` explore the data visually.  

---

## ⚙️ Installation  

1. Clone this repository  
   ```bash
   git clone https://github.com/awaisali-tech/Movie-Rating-Predictor.git
   cd Movie-Rating-Predictor```

#Install dependencies
```bash
pip install -r requirements.txt```

# RapidAPI Key 

RAPIDAPI_KEY="9dd01a5592mshc2deb8ada4c83dep157468jsn1f6ffd1c60c4"

Run the pipeline step by step:
# 1. Fetch data from API
python data_from_api.py  

# 2. Convert raw JSON → CSV
python preprocess.py  

# 3. Preprocess, train models & generate plots
python data_preprocessing_1.py  

Outputs include:
movies.json → Raw API data

movies_clean.csv → Intermediate cleaned dataset

movies_cleaned_final.csv → Final dataset used for training

rating_hist.png, rating_vs_year.png → Visualizations

### Histogram of IMDb Ratings:
<img width="1142" height="721" alt="image" src="https://github.com/user-attachments/assets/36847399-e764-47d2-b13b-a689addd2f9a" />

## 💡 Lessons Learned

How to handle real-world API data and secure keys with .env.

Preprocessing challenges like missing values & grouping by IMDb ID.

Model performance is limited by small dataset size → need more diverse data.

## 🔮 Next Steps

Fetch larger & more diverse datasets for better R² scores.

Add more feature engineering (director, actors, budget, etc.).

Improve visualizations & experiment with deep learning models.


## 📂 Project Structure:
├── data_from_api.py            # Fetches movie data
├── preprocess.py               # Cleans raw JSON → CSV
├── data_preprocessing_1.py     # Preprocessing + modeling + plots
├── movies.json                 # Raw dataset
├── movies_clean.csv            # Cleaned dataset
├── movies_cleaned_final.csv    # Final dataset
├── rating_hist.png             # Histogram visualization
├── rating_vs_year.png          # Year vs rating plot
├── .gitignore                  # Excludes .env & temp files
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation


## 📬 Contact  
If you have suggestions, feel free to open an [issue](../../issues) or reach out! 



