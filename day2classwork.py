from datetime import date
import pandas as pd
import numpy as np

engagement = pd.read_csv('./CSVs/engagements.csv')
enrollment = pd.read_csv('./CSVs/enrollments.csv')
submissions = pd.read_csv('./CSVs/submissions.csv')

df_engagement = pd.DataFrame(data=engagement, index=None)
df_enrollment = pd.DataFrame(data=enrollment, index=None)
df_submissions = pd.DataFrame(data=submissions, index=None)

#### In Class work

# How many students were active within the first week? Provisionally, 1237

df_enrollment.rename(columns={ "account_key": 'acct'}, inplace=True)
ee_merge = pd.merge(df_engagement, df_enrollment[['join_date', 'acct']], on='acct', how='right')

ee_merge.utc_date = pd.to_datetime(ee_merge['utc_date'])
ee_merge.join_date = pd.to_datetime(ee_merge['join_date'])

time_delta_of_seven = ee_merge.loc[(ee_merge['utc_date'] - ee_merge['join_date']).dt.days <= 7]
filtered = time_delta_of_seven.drop_duplicates(subset='acct')

print(filtered)

# How many minutes did each student spend on the website total? 

grouped_accounts = df_engagement.groupby(['acct']).sum()

print(grouped_accounts)

