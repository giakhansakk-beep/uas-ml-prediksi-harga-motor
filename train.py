import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("BIKE DETAILS.csv", sep=";")

df["year"] = df["year"].astype(int)
df["selling_price"] = df["selling_price"].astype(float)

X = df[["year"]]
y = df["selling_price"]

model = LinearRegression()
model.fit(X, y)

with open("model_harga.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model_harga.pkl BERHASIL DIBUAT")
