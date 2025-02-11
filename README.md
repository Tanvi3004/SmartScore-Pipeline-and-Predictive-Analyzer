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

# Model Training Details

- Algorithm: CatBoost Classifier
- Hyperparameter Optimization: Tuned via Grid Search
- Performance Metrics:
  - Accuracy
  - Precision, Recall, F1-score
  - Feature Importance Analysis
 
# Visualization & Monitoring

- Training and evaluation logs are stored in catboost_info/
- Jupyter notebooks provide detailed EDA and model analysis
- HTML templates allow for visualizing key model insights

# Web Interface Preview
Below are screenshots of the SmartScore Pipeline and Predictive Analyzer web interface.

## 1. Home Page
Displays a welcome message upon accessing the application.
Confirms that the application is running successfully on the specified server.
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/2389b3d8-8d3c-42f6-bb15-660684f47719" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/2cd0bdb8-28f5-49d6-a915-0fbcd4af3502" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/436184a9-dd89-42a6-9554-8a210dc0064f" />
## 2. Student Exam Performance Prediction Page
Users can input student details such as gender, ethnicity, parental education level, lunch type, test preparation course completion, writing score, and reading score.
A button labeled "Predict your Maths Score" triggers the machine learning model to generate a prediction.

## 3. Prediction Output
After entering the required inputs, the app provides a predicted maths score based on the model’s trained data.
This prediction helps in analyzing student performance trends.
