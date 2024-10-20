import pandas as pd
df = pd.read_csv('colors.csv')
unique_colors = df['Color Name'].unique().tolist()
print(unique_colors)

color_list = df['Color Name'].tolist()

code = {}
for i in color_list:
    list = []
    for j in unique_colors:
    
        if i == j:
            list.append(1)
        else:
            list.append(0)

            code.update({i:list})

dictionary = {}
for i in color_list:
    dictionary.update({i:code[i]})

# print(dictionary)





    
# print(code)

df = df.assign(**dictionary)

# df[color_list] = 

print(df)