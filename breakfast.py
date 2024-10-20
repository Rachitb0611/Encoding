import pandas as pd

df = pd.read_csv('breakfast.csv')

mydict = {
    'every day':3,
    'most days':2,
    'rarely':1,
    'never':0
}

freq_list = df['Frequency of having breakfast'].tolist()
breakfast_list = []
for i in freq_list:
    breakfast_list.append(mydict[i.lower()])
    

df['Breakfast'] = breakfast_list

print(df)