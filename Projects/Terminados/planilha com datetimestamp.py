import pandas as pd


nome_aluno = []
turma_aluno = []
data_atestado = []
tempo_de_atestado = []
CID = []
num_chamada = []

recebendo_data = True
while recebendo_data:
    num_chamada_in = input("Insira o numero da chamada: ")
    num_chamada.append(num_chamada_in)
    
    nome_aluno_in = input("Insira o nome do aluno:  ")
    nome_aluno.append(nome_aluno_in)

    turma_aluno_in = input("Insira a turma:  ")
    turma_aluno.append(turma_aluno_in)

    data_atestado_data = input("Insira a data do atestado:(ddmmyyyy)  ")
    data_atestado_in = pd.to_datetime(data_atestado_data,dayfirst=True, format='%d%m%Y')
    data_atestado.append(data_atestado_in)

    tempo_de_atestado_in = input("Insira quantos dias de atestado:  ")
    tempo_de_atestado.append(tempo_de_atestado_in)

    CID_in = input("Insira o CID (se houver):  ")
    CID.append(CID_in)

    continuar = input("Deseja Continuar? S/N ")
    if continuar == "S" or continuar == "s":
        pass
    else:
        recebendo_data = False


atestados_df = pd.DataFrame(
    {"Nome do aluno":nome_aluno,
     "Turma":turma_aluno,
     "Data do Atestado":data_atestado,
     "Tempo de Atestado":tempo_de_atestado},
    index=num_chamada)

atestados_df.to_excel("Atestados Alunos.xlsx",sheet_name="Geral", index=True)
