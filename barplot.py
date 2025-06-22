import zipfile
import pandas as pd
import matplotlib.pyplot as plt

with zipfile.ZipFile(r"C:\Users\Acer\OneDrive\Desktop\archive.zip", 'r') as zip_ref:

    zip_ref.extractall("data/")

df = pd.read_csv("data/tested.csv")


df["Pclass"].value_counts().sort_index().plot(kind='bar', color='purple')
plt.title("Passenger Count by Class - Bar Plot")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()
