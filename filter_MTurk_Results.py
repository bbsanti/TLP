import pandas as pd
from collections import Counter

# Specify the names of your columns and your labels of interest
video_id_column = 'Input.video_url'
label_column = 'Answer.category.label'
labels_of_interest = ['Dissolve Transition', 'Wipe Transition']  # Replace with your labels

# Load the CSV file
df = pd.read_csv('D:/Users/Santi/Downloads/Batch_5092411_batch_results (1).csv')

# Filter rows: only consider rows where 'label' is in 'labels_of_interest'
df = df[df[label_column].isin(labels_of_interest)]

# Group by 'video_id' and get the count of each label
grouped_df = df.groupby(video_id_column)[label_column].apply(list).reset_index()

# Function to check if any label occurs at least twice
def has_duplicate(labels):
    counter = Counter(labels)
    for count in counter.values():
        if count >= 2:
            return True
    return False

# Function to find the most common label
def most_common_label(labels):
    counter = Counter(labels)
    return counter.most_common(1)[0][0]

# Apply the functions to the grouped dataframe
grouped_df['has_duplicate'] = grouped_df[label_column].apply(has_duplicate)
grouped_df['most_common_label'] = grouped_df[label_column].apply(most_common_label)

# Filter the dataframe for videos with at least 2 of the same label
filtered_df = grouped_df[grouped_df['has_duplicate']]

# Load the second CSV file
df2 = pd.read_csv('D:/Users/Santi/Downloads/Bally_PIT@TBR_URLS - KEY of 1-100.csv')  # Replace with your actual file path

# Merge the two dataframes on 'video_id_column'
merged_df = pd.merge(filtered_df, df2, on=video_id_column)

# Add a new column that checks if the labels match
merged_df['labels_match'] = merged_df['most_common_label'] == merged_df[label_column+'_y']

merged_df = merged_df[[ 'Input.video_url','Answer.category.label_x','most_common_label','Answer.category.label_y','labels_match']]

# Display the result
print(merged_df.to_string())


