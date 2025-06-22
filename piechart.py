import zipfile
import pandas as pd
import matplotlib.pyplot as plt

with zipfile.ZipFile(r"C:\Users\Acer\OneDrive\Desktop\archive.zip", 'r') as zip_ref:

    zip_ref.extractall("data/")

df = pd.read_csv("data/tested.csv")

# Pie Chart: Embarked Distribution
df["Embarked"].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Embarked Location Distribution - Pie Chart")
plt.ylabel("")  # Hide y-axis label
plt.axis('equal')
plt.show()

