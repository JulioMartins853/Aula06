# Cria o discionário
alunos = {"Maria":99,"Clovis":88,"Ana":77,"Dio":66} 
# Alterar um valor
alunos["Clovis"] = 55
print(alunos)
# remoção
alunos.pop("Clovis")
print(alunos)
alunos["Kiko"] = 44 # adição de valor
for nome, mat in alunos.items(): # iterando no discioário
    print(f"Nome {nome} Matricula {mat}")
alunosCopia = alunos.copy()
alunosCopia["Ana"] = 33
print("Alunos ",alunos)
print("Alunos Copia ",alunosCopia)