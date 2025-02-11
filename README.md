## SmartScore-Pipeline-and-Predictive-Analyzer



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
