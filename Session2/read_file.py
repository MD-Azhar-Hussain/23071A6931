import pandas as pd

# Read a CSV file
df = pd.read_csv(r'C:\Users\azhar\Downloads\country_wise_latest_modified.csv')

# Display the DataFrame
print(df)

#fill missing values
miss_in = df.isnull().sum()
print(miss_in[miss_in>0])

# Fill missing values with a constant (e.g., 0 or 'unknown')
df_filled_constant = df.fillna(0)

# Forward fill (uses the previous value to fill)
df_filled_forward = df.fillna(method='ffill')

# Backward fill (uses the next value to fill)
df_filled_backward = df.fillna(method='bfill')

# Display the modified DataFrames
print("\nFilled with constant 0:")
print(df_filled_constant)


print("\nForward filled:")
print(df_filled_forward)

print("\nBackward filled:")
print(df_filled_backward)

#drop rows and coulmns
#column
df_filled_constant = df_filled_constant.drop('Deaths',axis=1)
print(df_filled_constant)
#row
df_filled_constant = df_filled_constant.drop(0,axis=0)
print(df_filled_constant)

df_filled_constant.to_csv(r'C:\Users\azhar\Downloads\counrty_modified.csv', index=False)    

