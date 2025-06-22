import zipfile
import pandas as pd
import matplotlib.pyplot as plt

# Extract ZIP
with zipfile.ZipFile(r"C:\Users\Acer\OneDrive\Desktop\archive.zip", 'r') as zip_ref:

    zip_ref.extractall("data/")

# Load CSV
df = pd.read_csv("data/tested.csv")

# Line Plot: PassengerId vs Fare
plt.plot(df["PassengerId"], df["Fare"], color='blue')
plt.title("PassengerId vs Fare - Line Plot")
plt.xlabel("PassengerId")
plt.ylabel("Fare")
plt.grid(True)
plt.show()
