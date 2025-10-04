import pandas as pd 
import os 

data = {
    'Name':['Ath','Bth','Cth'],
    'Age':[10,20,30],
    'City':['N','P','Q']
}

df=pd.DataFrame(data)

os.makedirs('data',exist_ok=True)

file_path=os.path.join('data','sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file is created at {file_path}")