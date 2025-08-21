"""
Movie Ratings Prediction Project
--------------------------------
This script preprocesses a movie dataset and applies different regression models 
to predict IMDb ratings based on genres, release year, and movie type.

Steps included:
1. Data Loading & Cleaning
2. Feature Engineering (genres, type encoding, scaling)
3. Train-Test Split
4. Model Training & Evaluation (Linear Regression, Ridge, Random Forest)
5. Visualization
6. Save Final Cleaned Dataset
"""

# Import required libraries
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os

# Define base directory for relative paths
BASE_DIR = os.path.dirname(__file__)

# Load dataset (movies_clean.csv) with no header, then assign column names
df = pd.read_csv(os.path.join(BASE_DIR, "movies_clean.csv"), header=None)
df.columns = ["poster_link", "genres", "imdb_id", "title", "rating", "year", "description", "type"]

# ----------------- Data Preprocessing -----------------

# Drop columns not useful for prediction (poster, description, title) 
# but keep imdb_id for uniqueness
df = df.drop(columns=["poster_link", "description", "title"])

# Handle missing genres by replacing NaN with empty string
df['genres'] = df['genres'].fillna('')

# Convert genre string into list (split by comma)
df['genres'] = df['genres'].apply(lambda x: x.split(", ") if x else [])

# Explode list into separate rows (one genre per row)
df = df.explode('genres')

# One-hot encode genres (convert categorical values into binary columns)
df = pd.get_dummies(df, columns=['genres'])

# Group by imdb_id (unique movie) and aggregate genre/type one-hot columns using max()
df = df.groupby(['imdb_id', 'rating', 'year', 'type'], as_index=False).max()

# Drop imdb_id since it’s just an identifier (not useful for ML)
df = df.drop(columns=['imdb_id'])

# One-hot encode the "type" column (e.g., Movie/TV Show)
df = pd.get_dummies(df, columns=['type'])

# ----------------- Handle Missing & Numeric Data -----------------

# Convert rating & year to numeric (force errors to NaN if non-numeric)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Fill missing rating & year with their mean values
df['rating'].fillna(df['rating'].mean(), inplace=True)
df['year'].fillna(df['year'].mean(), inplace=True)

# ----------------- Feature Engineering -----------------

# Separate features (X) and target (y)
X = df.drop("rating", axis=1)
y = df["rating"]

# Drop low-variance columns (very little information content, e.g. rare genres)
X = X.loc[:, X.var() > 0.01]

# Standardize "year" column (scale to mean=0, std=1 for ML stability)
scaler = StandardScaler()
X['year'] = scaler.fit_transform(X[['year']])

# ----------------- Train/Test Split -----------------

# Split dataset: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ----------------- Model Evaluation Function -----------------

def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    """
    Fits a model, makes predictions, and evaluates performance using:
    - Mean Squared Error (MSE)
    - R² score on test set
    - Average R² score using 5-fold cross-validation
    """
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)  # error metric
    r2 = r2_score(y_test, y_pred)             # performance metric
    cv_r2 = cross_val_score(model, X, y, cv=5, scoring='r2').mean()  # CV avg

    print(f"\n{name}:")
    print(f"  MSE (test): {mse:.2f}")
    print(f"  R2 (test): {r2:.2f}")
    print(f"  R2 (5-fold CV): {cv_r2:.2f}")
    return mse, r2, cv_r2

# ----------------- Model Training & Comparison -----------------

# Define models to compare
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

# Run evaluations for each model
print("\n--- Model Evaluation ---")
results = {}
for name, model in models.items():
    results[name] = evaluate_model(name, model, X_train, X_test, y_train, y_test)

# ----------------- Visualization -----------------

# Scatter plot: Rating vs. Year
plt.figure(figsize=(8, 5))
plt.scatter(df['year'], df['rating'], alpha=0.5)
plt.title('IMDb Ratings vs. Release Year')
plt.xlabel('Year')
plt.ylabel('IMDb Rating')
plt.savefig(os.path.join(BASE_DIR, "rating_vs_year.png"))  # Save plot
plt.close()

# ----------------- Save Cleaned Dataset -----------------

df.to_csv("movies_cleaned_final.csv", index=False)
print("\nCleaned dataset saved as movies_cleaned_final.csv")
print(df.head())
