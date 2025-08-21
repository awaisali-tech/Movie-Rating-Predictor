# Movie-Rating-Predictor

My first end-to-end machine learning pipeline project! 🚀

## Overview
This project predicts IMDb movie ratings using data fetched from a RapidAPI endpoint. It includes:
- **Data Acquisition**: `data_from_api.py` pulls ~500 movies.
- **Preprocessing**: `preprocess.py` and `data_preprocessing_1.py` clean data, handle genres, and engineer features (e.g., genre count).
- **Modeling**: Tests Linear Regression (MSE: 0.25, R2: -0.09), Ridge, and Random Forest (MSE: 0.31, R2: -0.31) with cross-validation and tuning.
- **Visualizations**: `rating_hist.png` and `rating_vs_year.png` explore the data.

## How It Works
1. Run `data_from_api.py` to fetch data and save as `movies.json` (requires a RapidAPI key in `.env`).
2. Run `preprocess.py` to convert to `movies_clean.csv`.
3. Run `data_preprocessing_1.py` to preprocess, train models, generate plots, and save `movies_cleaned_final.csv`.

## Lessons Learned
- Handling real-world API data and securing keys with `.env`.
- Preprocessing challenges (e.g., NaN values, grouping by IMDb ID).
- Model performance limited by small dataset; working on more data for positive R2.

## Files
- `data_from_api.py`: Fetches movie data.
- `preprocess.py`: Cleans raw JSON to CSV.
- `data_preprocessing_1.py`: Preprocesses and trains models.
- `movies.json`, `movies_clean.csv`, `movies_cleaned_final.csv`: Data files.
- `rating_hist.png`, `rating_vs_year.png`: Visualizations.
- `.gitignore`: Excludes `.env` and temporary files.

## Next Steps
- Fetch more diverse data to improve R2.
- Tune models further.
- Add more visualizations.

## Feedback
I’m new to this—suggestions welcome! Contact me or open an issue.  

#MachineLearning #Python #MLPipeline #BeginnerJourney
