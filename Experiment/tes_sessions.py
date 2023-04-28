import pandas as pd

# Assume the DataFrame is already loaded and stored in a variable called `df`

# Define a custom function to assign a session number based on time of day
def assign_session(row):
    hour = row['Datetime'].hour
    
    if (hour >= 13 and hour <= 22):
        return 'New York session'
    elif (hour >= 7 and hour <= 16):
        return 'London session'
    elif (hour >= 0 and hour <= 9):
        return 'Tokyo session'
    elif (hour >= 21 or hour <= 6):
        return 'Sidney session'
    else:
        return None

# Apply the function to each row and assign the results to the 'sessions' column
df['sessions'] = df.apply(assign_session, axis=1)

# Print the updated DataFrame
print(df)
