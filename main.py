from openpyxl import load_workbook, Workbook

arquivo = load_workbook('alunos.xlsx')
planilha_alunos = arquivo['Alunos']

alunos_aprovados = []
alunos_reprovados = []

soma_nota = 0
maior_nota = 0 

for aluno in planilha_alunos.iter_rows(min_row=2, values_only=True):
    nome, curso, idade, nota_final, data_matricula = aluno
    soma_nota+= nota_final
    if nota_final > maior_nota:
        maior_nota = nota_final
        aluno_maior_nota = nome
    alunos_dicionario = {
        'nome': nome,
        'curso': curso,
        'idade': idade,
        'nota_final': nota_final,
        'data_matricula': data_matricula
    }
    if nota_final >= 7:
        alunos_aprovados.append(alunos_dicionario)
    else:
        alunos_reprovados.append(alunos_dicionario)

media_nota = soma_nota / (len(alunos_aprovados)+len(alunos_reprovados))

arquivo_aprovado = Workbook()
planilha_aprovados = arquivo_aprovado.active
planilha_aprovados.title = 'Alunos aprovados'

arquivo_reprovado = Workbook()
planilha_reprovados = arquivo_reprovado.active
planilha_reprovados.title = 'Alunos Reprovados'

planilha_aprovados.append(['Nome', 'Curso', 'Idade', 'Nota Final', 'Data Matricula'])
for aluno in alunos_aprovados:
    planilha_aprovados.append(list(aluno.values()))

planilha_reprovados.append(['Nome', 'Curso', 'Idade', 'Nota Final', 'Data Matricula'])
for aluno in alunos_reprovados:
    planilha_reprovados.append(list(aluno.values()))

arquivo_aprovado.save('Aprovados.xlsx')
arquivo_reprovado.save('Reprovados.xlsx')

print(f"Número de aprovados é: {len(alunos_aprovados)}")
print(f"Número de aprovados é: {len(alunos_reprovados)}")
print(f"Média de notas: {media_nota}")
print(f"A maior nota foi: {aluno_maior_nota} - {maior_nota}")