# SmartScore-Pipeline-and-Predictive-Analyzer

The SmartScore Pipeline and Predictive Analyzer is designed to provide a streamlined approach for processing and analyzing predictive models using machine learning. This project leverages CatBoost, data preprocessing techniques, and a well-defined ML pipeline to optimize performance and efficiency.

# Project Structure

- **SmartScore-Pipeline-and-Predictive-Analyzer/**
  - `README.md` - Project documentation.
  - `requirements.txt` - List of required dependencies.
  - `setup.py` - Setup script for installation.
  - `application.py` - Main application script.
  - **artifacts/** - Contains processed datasets and saved models.
    - `data.csv` - Raw dataset.
    - `train.csv` - Training dataset.
    - `test.csv` - Test dataset.
    - `model.pkl` - Trained machine learning model.
    - `preprocessor.pkl` - Saved preprocessing pipeline.
  - **catboost_info/** - Stores CatBoost training logs and metadata.
    - `catboost_training.json` - Training details.
    - `learn_error.tsv` - Error logs.
    - `time_left.tsv` - Time estimation logs.
  - **notebook/** - Contains Jupyter notebooks for model development.
    - `1. EDA STUDENT PERFORMANCE.ipynb` - Exploratory Data Analysis.
    - `2. MODEL TRAINING.ipynb` - Model training workflow.
  - **src/** - Core source code for the ML pipeline.
    - **components/** - Submodules for data processing.
      - `data_ingestion.py` - Data loading and ingestion.
      - `data_transformation.py` - Feature engineering.
      - `model_trainer.py` - Model training logic.
    - **pipeline/** - Pipeline scripts.
      - `predict_pipeline.py` - Inference pipeline.
      - `train_pipeline.py` - Model training pipeline.
  - **templates/** - Frontend templates for visualization.
    - `home.html` - Home page template.
    - `index.html` - Index page template.


# Key Features
- End-to-End ML Pipeline: Automates data preprocessing, model training, and prediction.
- CatBoost Implementation: Uses CatBoost for robust classification and performance tuning.
- Data Preprocessing:Includes data cleaning, feature engineering, and transformations.
- Model Training & Evaluation: Stores models and evaluation metrics in the artifacts directory.
- Notebook Documentation: Provides EDA and model training workflows in Jupyter Notebooks.
- Web Interface Support: Supports visualization through templates/ directory.

### 1. Installation
Clone the Repository
``` bash
git clone https://github.com/Tanvi3004/SmartScore-Pipeline-and-Predictive-Analyzer.git
```
``` bash
cd SmartScore-Pipeline-and-Predictive-Analyzer
```
### 2. Create and Activate a Virtual Environment
``` bash
python3 -m venv venv
```
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```

# Usage

### 1. Data Preprocessing
To preprocess data and generate training/test datasets:
``` bash
python src/components/data_ingestion.py
```
### 2. Model Training
To train a new model with the defined pipeline:
``` bash
python src/pipeline/train_pipeline.py
```
### 3. Making Predictions
To generate predictions using the trained model:
``` bash
python src/pipeline/predict_pipeline.py
```
### 4. Running the Application
If a web interface is provided, run the application with:
``` bash
python application.py
```
