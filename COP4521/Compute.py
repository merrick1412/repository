"""
Name:Merrick Moncure
Date: 2/9/25
Assignmnent: Module 6: Python Dask large data set
load a large data file into a dask dataframe.
Assumptions: NA
All work below was performed by Merrick Moncure
"""
#https://www.kaggle.com/datasets
import dask.dataframe as dd
def fix_blood_pressure(val):
        systolic, diastolic = map(int, val.split('/'))
        return systolic + diastolic #makes the blood pressure a string

def convert_y_n(val): #1 or yes, 0 for no
    return 1 if val == 'Y' else 0 if val == 'N' else None
dtypes = { #defines the datatypes ill be using
    'Gender': 'object',
    'Age': 'int64',
    'Sleep duration': 'float64',
    'Sleep quality': 'int64',
    'Stress level': 'int64',
    'Blood pressure': 'object',
    'Heart rate': 'int64',
    'Daily steps': 'int64',
    'Physical activity': 'int64',
    'Height': 'int64',
    'Weight': 'int64',
    'Sleep disorder': 'object',
    'Wake up during night': 'object',
    'Feel sleepy during day': 'object',
    'Caffeine consumption': 'object',
    'Alcohol consumption': 'object',
    'Smoking': 'object',
    'Medical issue': 'object',
    'Ongoing medication': 'object',
    'Smart device before bed': 'object',
    'Average screen time': 'float64',
    'Blue-light filter': 'object',
    'Discomfort Eye-strain': 'object',
    'Redness in eye': 'object',
    'Itchiness/Irritation in eye': 'object',
    'Dry Eye Disease': 'object',
}
df = dd.read_csv('Dry_Eye_Dataset.csv', dtype=dtypes) #load it into dask
# Convelrt 'Y'/'N' columns to 1/0

df['Caffeine consumption'] = df['Caffeine consumption'].apply(convert_y_n, meta=('Caffeine consumption', 'float64'))
df['Alcohol consumption'] = df['Alcohol consumption'].apply(convert_y_n, meta=('Alcohol consumption', 'float64'))
df['Smoking'] = df['Smoking'].apply(convert_y_n, meta=('Smoking', 'float64'))
df['Blood pressure'] = df['Blood pressure'].apply(fix_blood_pressure, meta=('Blood pressure', 'float64'))

#groupby operation and calculates the mean
result = df.groupby(['Age', 'Caffeine consumption', 'Alcohol consumption', 'Smoking'])['Sleep duration'].mean()
result = result.reset_index() #fixes index
result.visualize(filename='dask_dag.png')
#display the first few rows
print(result.head())



