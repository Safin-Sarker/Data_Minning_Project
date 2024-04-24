import pandas as pd
import os
from together import Together

def predict_check_worthiness(file):
    # Load the TSV file into a pandas DataFrame
    df = pd.read_csv(file, sep=',')

    # Initialize Together client
    client = Together()

    # Initialize an empty list to store predictions
    predictions = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Get the tweet text from the 'Text' column
        tweet_text = row['tweet_text']
        
        # Format the tweet text within the prompt
        prompt = f"""Does the sentence contain a verifiable factual claim? 
        Does the sentence contain a verifiable factual claim? 
        Will the sentence's claim have an impact on or be of interest to the general public?
        Do you think that a professional fact-checker should verify the claim in the sentence?
        Is the sentence harmful to the society?
        Considering these questions, tell if the sentence is check worthy or not. Only reply with 'Yes' or 'No'. If you are not sure, just say 'No'.: {tweet_text}"""
        
        try:
            # Predict the class label of the tweet text
            response = client.chat.completions.create(
                model="meta-llama/Llama-2-70b-chat-hf",
                messages=[{"role": "user", "content": prompt}],
            )
            predicted_label = response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error processing tweet {row['tweet_id']}: {e}")
            predicted_label = "No"  # Assuming 'No' as the default label in case of an error
        
        
        # Append the tweet and predicted class label to the predictions list
        predictions.append({'tweet_id': row['tweet_id'], 'class_label': predicted_label})

    # Convert the predictions list into a DataFrame
    predictions_df = pd.DataFrame(predictions)

    # Get the file name without path
    file_name = os.path.basename(file)
    # Construct the output file path
    output_file = os.path.join("../output_data/baseline/", file_name.replace('_dev-test_preprocessed.csv', '_baselined.csv'))

    # Write the predictions to the output file
    predictions_df.to_csv(output_file, sep=',', index=False)


predict_check_worthiness("../data/processed_data/CT24_checkworthy_english/CT24_checkworthy_english_dev-test_preprocessed.csv")
predict_check_worthiness("../data/processed_data/CT24_checkworthy_dutch/CT24_checkworthy_dutch_dev-test_preprocessed.csv")
predict_check_worthiness("../data/processed_data/CT24_checkworthy_arabic/CT24_checkworthy_arabic_dev-test_preprocessed.csv")