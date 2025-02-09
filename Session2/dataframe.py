import pandas as pd

# Create a DataFrame
df = {
    'Name': ['John', 'Jane', 'Sue', 'Fred'],
    'Age': [23, 29, 21, 18],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Boston'],
    'state': ['NY', 'CA', 'IL', 'MA']
}
df_new = pd.DataFrame(df)
print(df_new)

ndf ={
    'Salary': [1000, 2000, 3000, 4000],
    'Department': ['HR', 'Engineering', 'Finance', 'Marketing']
}
ndf_new = pd.DataFrame(ndf)

# Concatenate two DataFrames
#horizontally
result = pd.concat([df_new, ndf_new], axis=1)
print(result)
#vertically
result = pd.concat([df_new, ndf_new], ignore_index=True)
print(result)