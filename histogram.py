import zipfile
import pandas as pd
import matplotlib.pyplot as plt

with zipfile.ZipFile(r"C:\Users\Acer\OneDrive\Desktop\archive.zip", 'r') as zip_ref:

    zip_ref.extractall("data/")

df = pd.read_csv("data/tested.csv")


df["Age"].dropna().hist(bins=20, color='pink', edgecolor='black')
plt.title("Age Distribution - Histogram")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
