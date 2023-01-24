import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
Dataframe=pd.read_csv("C:\\Users\\user\\PycharmProjects\\RealPython\\Unemployment in India.csv")
print(Dataframe)
print(Dataframe.shape)
print(Dataframe.describe())
print(Dataframe.corr())

sns.heatmap(Dataframe.corr(),cmap="pink",annot=True)
plt.show()
Dataframe.columns= ["Region","Date","Frequency","  Unemployment Rate (%)","Estimated Employed",
             "Estimated Labour Participation Rate (%)","Area"]

plt.title("Unemployment in India")
sns.histplot(x="Estimated Employed", hue="Region", data=Dataframe)
plt.show()

plt.title("Unemployment in India")
sns.histplot(x="Estimated Labour Participation Rate (%)", hue="Region", data=Dataframe)
plt.show()
plt.title("Unemployment in India")
sns.histplot(x="Estimated Labour Participation Rate (%)", hue="Area", data=Dataframe)
plt.show()
plt.title("Unemployment in India")
sns.histplot(x="Estimated Employed", hue="Area", data=Dataframe)
plt.show()

