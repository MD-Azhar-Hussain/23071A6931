import pandas as pd

# Read a CSV file
df = pd.read_csv(r'C:\Users\azhar\Downloads\country_wise_latest_modified.csv')
print(df)

filter_df = df[(df['Confirmed'] > 100000) & (df['Recovered'] > 50000)]
print(filter_df)

#plotings
#in pd df.plot(kind,x,y,title)
#in matplotlib plt.plot(dfx,dfy,color,label)

import matplotlib.pyplot as plt

plt.pie(df['New cases'],labels=df['WHO Region'],autopct='%1.1f%%',startangle=90,shadow=True)
plt.title('New cases vs WHO Region')
plt.show()

plt.bar(df['New cases'],df['WHO Region'],color='red',label='New cases vs WHO Region')
plt.xlabel('New cases')
plt.ylabel('WHO Region')
plt.title('New cases vs WHO Region')
plt.show()

plt.scatter(df['Confirmed'],df['Deaths'],color='blue',label='Confirmed vs Deaths')
plt.xlabel('Confirmed')
plt.ylabel('Deaths')
plt.show()

plt.plot(df['Confirmed'],df['1 week change'],color='green',label='Confirmed vs 1 week change')
plt.xlabel('Confirmed')
plt.ylabel('1 week change')
plt.show()

plt.boxplot(df['Active'],vert=False)
plt.show()

