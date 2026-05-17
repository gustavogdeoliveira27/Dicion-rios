alunos = {
    "Gustavo": 10.0,
    "Gabriel": 7.0,
    "Leticia": 8.5
}
nome = input("Digite o nome do aluno: ")
nota = alunos.get(nome, "Aluno não encontrado.")
print(f"Resultado do aluno '{nome}':", nota)