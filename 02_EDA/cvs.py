import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df_titanic: pd.DataFrame = pd.read_csv(url)

print("\nHEAD:")
print(df_titanic.head())

print("\nSHAPE:")
print(df_titanic.shape)

print("\nCOLUMNS:")
print(df_titanic.columns)

print("\nINFO:")
df_titanic.info()

print("\nMISSING VALUES:")
print(df_titanic.isnull().sum())

missing_percentage = (
    df_titanic.isnull().sum() /
    len(df_titanic) * 100
)

print("\nMISSING VALUES (%):")
print(missing_percentage)

print("\nDUPLICATES:")
print(df_titanic.duplicated().sum())

print("\nDESCRIBE:")
print(df_titanic.describe())

print("\nVALUE COUNTS:")
print(df_titanic["Survived"].value_counts())

print("\nSURVIVAL BY SEX:")
print(
    df_titanic.groupby("Sex")["Survived"].mean()
)

print("\nSURVIVAL BY CLASS:")
print(
    df_titanic.groupby("Pclass")["Survived"].mean()
)

age_median = df_titanic["Age"].median()

print("\nAGE MISSING VALUES:")
print(df_titanic["Age"].isnull().sum())

print("\nAGE MEDIAN:")
print(age_median)

survival_by_sex = (
    df_titanic.groupby("Sex")["Survived"].mean()
)

plt.bar(
    survival_by_sex.index,
    survival_by_sex.values,
    color=["coral", "skyblue"],
    edgecolor="black"
)

plt.xlabel("Sexo")
plt.ylabel("Taxa de Sobrevivência")
plt.title("Taxa de Sobrevivência por Sexo")
plt.show()

plt.hist(
    df_titanic["Age"].dropna(),
    bins=20,
    color="purple",
    edgecolor="black",
    alpha=0.7
)

plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.title("Distribuição das Idades")
plt.show()

survival_colors = {
    0: "coral",
    1: "skyblue"
}

for survived, group in df_titanic.groupby("Survived"):
    plt.scatter(
        group["Age"],
        group["Fare"],
        label="Sobreviveu" if survived == 1 else "Não sobreviveu",
        color=survival_colors[survived],
        edgecolor="black",
        alpha=0.6
    )

plt.xlabel("Idade")
plt.ylabel("Tarifa")
plt.title("Idade x Tarifa")
plt.legend()
plt.show()

classes = sorted(df_titanic["Pclass"].unique())

fare_by_class = [
    df_titanic[df_titanic["Pclass"] == passenger_class]["Fare"]
    for passenger_class in classes
]

plt.boxplot(
    fare_by_class,
    tick_labels=classes,
    patch_artist=True,
    boxprops=dict(
        facecolor="lightblue",
        color="blue"
    )
)

plt.xlabel("Classe")
plt.ylabel("Tarifa")
plt.title("Distribuição das Tarifas por Classe")
plt.show()

numeric_columns = [
    "Survived",
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]

correlation = df_titanic[numeric_columns].corr()

print("\nCORRELATION:")
print(correlation)

print("\nSURVIVAL BY SEX AND CLASS:")
print(
    df_titanic.groupby(
        ["Sex", "Pclass"]
    )["Survived"].mean()
)
