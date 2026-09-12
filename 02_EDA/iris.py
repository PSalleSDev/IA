import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import Bunch
from sklearn.datasets import load_iris

iris: Bunch = load_iris(as_frame=True)

iris.frame["species"] = iris.frame["target"].map(
    dict(enumerate(iris.target_names))
)

df: pd.DataFrame = iris.frame

df["petal_area"] = (
    df["petal length (cm)"] *
    df["petal width (cm)"]
)

print("\nHEAD:")
print(df.head())

print("\nSHAPE:")
print(df.shape)

print("\nCOLUMNS:")
print(df.columns)

print("\nINFO:")
df.info()

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATES:")
print(df.duplicated().sum())

print("\nDESCRIBE:")
print(df.describe())

print("\nVALUE COUNTS:")
print(df["species"].value_counts())

species_groups = df.groupby("species")["petal_area"]

print("\nMEAN PETAL AREA BY SPECIES:")
print(species_groups.mean())

species = df["species"].unique()

petal_area_by_species = [
    df[df["species"] == species_name]["petal_area"]
    for species_name in species
]

mean_petal_area = df.groupby("species")["petal_area"].mean()

plt.bar(
    mean_petal_area.index,
    mean_petal_area.values,
    color=["coral", "lightgreen", "skyblue"],
    edgecolor="black"
)

plt.xlabel("Espécie")
plt.ylabel("Média da Área da Pétala ($cm^2$)")
plt.title("Média da Área da Pétala por Espécie")
plt.show()

plt.hist(
    df["petal_area"],
    bins=15,
    color="purple",
    edgecolor="black",
    alpha=0.7
)

plt.xlabel("Área da Pétala ($cm^2$)")
plt.ylabel("Frequência")
plt.title("Distribuição da Área das Pétalas")
plt.show()

species_colors = {
    "setosa": "coral",
    "versicolor": "lightgreen",
    "virginica": "skyblue"
}

for species_name, group in df.groupby("species"):
    plt.scatter(
        group["petal length (cm)"],
        group["petal width (cm)"],
        label=species_name,
        color=species_colors[species_name],
        edgecolor="black",
        alpha=0.8
    )

plt.xlabel("Comprimento da Pétala (cm)")
plt.ylabel("Largura da Pétala (cm)")
plt.title("Comprimento x Largura da Pétala")
plt.legend()
plt.show()

plt.boxplot(
    petal_area_by_species,
    tick_labels=species,
    patch_artist=True,
    boxprops=dict(
        facecolor="lightblue",
        color="blue"
    )
)

plt.xlabel("Espécie")
plt.ylabel("Área da Pétala ($cm^2$)")
plt.title("Área da Pétala por Espécie")
plt.show()

correlation = df.corr(numeric_only=True)

print("\nCORRELATION:")
print(correlation)