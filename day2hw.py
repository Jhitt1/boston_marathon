#### Homework
import pandas as pd
import numpy as np

marathon = pd.read_csv('./CSVs/marathon_results.csv')
df_marathon = pd.DataFrame(data=marathon)
del df_marathon['Unnamed: 0']


# Question 1 - What is the average age by state

def average_age_by_state(dataset):

    by_state = dataset[['State', 'Age']].groupby('State').mean()
    return by_state.astype(int)

print(average_age_by_state(df_marathon))

# Question 2 - What country has the most participants? USA

def most_participants(dataset):

    by_country = dataset.groupby('Country').count()
    participants = by_country['Citizen'].value_counts
    return participants

print(most_participants(df_marathon))

# I could not figure out the rest.