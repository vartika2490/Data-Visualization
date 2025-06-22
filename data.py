import zipfile
import pandas as pd


with zipfile.ZipFile(r"C:\Users\Acer\OneDrive\Desktop\archive.zip", 'r') as zip_ref:
    zip_ref.extractall("data/")  
   

df = pd.read_csv(r"C:\Users\Acer\OneDrive\Desktop\archive.csv")  
print(df.head())



