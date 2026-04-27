import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Sales.csv")

print(df.head())    # for see data
print(df.info())    # structure

print("Average Profit: ",df["Total Profit"].mean())

# bar chart
df.groupby("Region")["Total Profit"].sum().plot(kind="bar")
print(df.groupby("Region")["Total Profit"].sum().sort_values(ascending=False))
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.show()

#heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

