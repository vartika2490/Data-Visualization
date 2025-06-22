import zipfile
import pandas as pd
import matplotlib.pyplot as plt

with zipfile.ZipFile(r"C:\Users\Acer\OneDrive\Desktop\archive.zip", 'r') as zip_ref:

    zip_ref.extractall("data/")

df = pd.read_csv("data/tested.csv")

# Scatter Plot: Age vs Fare
plt.scatter(df["Age"], df["Fare"], color='green')
plt.title("Age vs Fare - Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
