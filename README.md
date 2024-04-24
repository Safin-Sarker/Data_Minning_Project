# Multilingual Check-worthiness Estimation in Text

# Fact-Checking Model Evaluation

This repository contains scripts and notebooks for evaluating and comparing the performance of fine-tuned transformer models and a baseline model for fact-checking tasks.

## Repository Structure

- **baseline**: Contains scripts related to the baseline model.
  - `baseline.py`: Python script for baseline model implementation.
  - `process_baseline_output.py`: Python script for processing baseline model output.
- **comparison**: Contains a Jupyter notebook for comparing the performance of different models.
  - `comparison.ipynb`: Jupyter notebook for model performance comparison.
- **data**: Contains both raw and processed data used for model training and evaluation.
  - `processed_data`: Processed data used for model evaluation.
  - `raw_data`: Raw data used for model training.
- **format_checker**: Contains a Python script for checking the format of input data.
  - `format_checker.py`: Python script for checking input data format.
- **output_data**: Contains output files generated during model evaluation.
  - `baseline`: Output files related to the baseline model.
  - `transformer`: Output files related to fine-tuned transformer models.
- **pre_process**: Contains a Jupyter notebook for data preprocessing.
  - `pre_process.ipynb`: Jupyter notebook for data preprocessing.
- **scorer**: Contains a Jupyter notebook for scoring model performance.
  - `scorer.ipynb`: Jupyter notebook for model performance scoring.
- **transformer**: Contains Jupyter notebooks for fine-tuning transformer models.
  - `custom_tuned_model.ipynb`: Jupyter notebook for custom fine-tuned transformer model.
  - `transformer_model_tuning.ipynb`: Jupyter notebook for tuning transformer model hyperparameters.
- **fine_tuned_model**: Contains directories for fine-tuned transformer models in different languages.
  - `fine_tuned_model_english`: Fine-tuned transformer model for English.
  - `fine_tuned_model_arabic`: Fine-tuned transformer model for Arabic.
  - `fine_tuned_model_dutch`: Fine-tuned transformer model for Dutch.

## Usage

1. Clone the repository.
2. Ensure all dependencies are installed as per requirements mentined in the begining of each code file.
3. Execute scripts and notebooks as needed for data preprocessing, model training, evaluation, and comparison.

