import pandas as pd

def process_predicted_labels(file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file)

    # Define a function to process the values in the 'predicted_label' column
    def process_predicted_label(value):
        if value.startswith('Yes'):
            return 'Yes'
        elif value.startswith('No'):
            return 'No'
        else:
            return 'No'

    # Apply the function to the 'predicted_label' column
    df['predicted_label'] = df['predicted_label'].apply(process_predicted_label)

    # Save the modified DataFrame back to the CSV file
    modified_csv_file = file.replace('.csv', '_processsed.csv')
    df.to_csv(modified_csv_file, index=False)
    

process_predicted_labels("../output_data/baseline/CT24_checkworthy_english_baselined.csv")
process_predicted_labels("../output_data/baseline/CT24_checkworthy_dutch_baselined.csv")
process_predicted_labels("../output_data/baseline/CT24_checkworthy_arabic_baselined.csv")
