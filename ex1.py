alunos: dict[str, int] = {
    "Evelyn": 8,
    "Pedro": 6,
    "Gustavo": 9,
    "Mateus": 5,
    "Felipe": 7,
    "Marcelo": 10
}

ap: int = 0
rp: int = 0

for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome} aprovado com nota {nota}")
        ap += 1
    else:
        print(f"{nome} reprovado com nota {nota}")
        rp += 1

print(f"Total de alunos {len(alunos.items())} Aprovador {ap} Reprovado {rp}")
