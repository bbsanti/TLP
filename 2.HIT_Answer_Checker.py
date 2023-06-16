import pandas as pd

# Load the first CSV file
df1 = pd.read_csv('D:/Users/Santi/Downloads/Batch_5092411_batch_results (1).csv')  # replace with your actual file path

# Load the second CSV file
df2 = pd.read_csv('D:/Users/Santi/Documents/Github_Repos/TLP/Bally_PIT@TBR_URLS - KEY of 1-100.csv')  # replace with your actual file path

# Specify the names of your video columns (replace with your actual column names)
video_column1 = 'Input.video_url'
video_column2 = 'Input.video_url'

# Specify the names of your answer columns
answer_column1 = 'Answer.category.label'
answer_column2 = 'Answer.category.label'

# Specify your custom strings
match_string = 'x'
mismatch_string = 'Wrong transition labeled'

# Specify your custom column names
match_column = 'Approve'
mismatch_column = 'Reject'

# Initialize your custom columns
df1[match_column] = ''
df1[mismatch_column] = ''

# Check each video in df1
for i, row in df1.iterrows():
    # If the video is also in df2
    if row[video_column1] in df2[video_column2].values:
        # Find the corresponding row in df2
        df2_row = df2[df2[video_column2] == row[video_column1]]
        # If the answers match, put match_string in match_column
        if df2_row[answer_column2].values[0] == row[answer_column1]:
            df1.at[i, match_column] = match_string
        # Else, put mismatch_string in mismatch_column
        else:
            df1.at[i, mismatch_column] = mismatch_string

# Save the modified df1 as a new CSV file
df1.to_csv('D:/Users/Santi/Downloads/Batch_5092411_batch_results-checked.csv', index=False)  # replace with your desired file path
