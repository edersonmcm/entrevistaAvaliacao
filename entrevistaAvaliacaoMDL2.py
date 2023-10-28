#Declarando variáveis que irão auxiliar no restante do código - EXCETO BASEINFO e PRINT
continua = True
while continua:
    try:
        num = int(input("Quantos candidatos participarão do processo seletivo? "))
        if num > 0:
            continua = False
        else:
            print("O número de candidatos deve ser maior que zero. Por favor, tente novamente.")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

listaCandidatos = []
baseInfo = "eX_tX_pX_sX"
print("\n", baseInfo, "\nA letra 'e' significa Entrevista, 't' teórica, 'p' prática, 's' soft skills. O X é o local onde receberá a nota da avaliação referente às letras que estão acompanhadas (e, t, p, s)")
recebe = []

# Função para receber uma entrada válida para as notas com a opção de tentar novamente
def input_valido(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0 or valor > 10:
                raise ValueError("A nota deve estar entre 0 e 10.")
            return valor
        except ValueError as e:
            print("Ocorreu um erro:", e)
            escolha = input("Deseja tentar novamente? (s/n): ")
            if escolha.lower() != 's':
                return -1  # Retornar um valor inválido para indicar saída

# Perguntar ao usuário se a nota de corte será a mesma para todas as etapas
escolha_nota_corte = input("Deseja definir a nota de corte para cada etapa? (s/n): ")
if escolha_nota_corte.lower() == 's':
    notaCorteE = input_valido("Qual será a nota de corte da etapa de Entrevista?\nR: ")
    notaCorteT = input_valido("Qual será a nota de corte da etapa Teórica?\nR: ")
    notaCorteP = input_valido("Qual será a nota de corte da etapa Prática?\nR: ")
    notaCorteS = input_valido("Qual será a nota de corte da avaliação de Soft Skills?\nR: ")
else:
    notaCorte = input_valido("Qual será a nota de corte para todas as etapas?\nR: ")
    notaCorteE = notaCorte
    notaCorteT = notaCorte
    notaCorteP = notaCorte
    notaCorteS = notaCorte

# Estrutura de repetição que fará a coleta e tratamento de cada candidato de acordo com o número de candidatos
for i in range(num):
    continua_candidato = True
    while continua_candidato:
        try:
            elimina = 0
            guarda = []
            nome_candidato = input("\nDigite o nome do "+str(i+1)+ "º candidato: ")
            entrevista_nota = input_valido("Entrevista: ")
            if entrevista_nota == -1:
                continua_candidato = False
            else:
                guarda.append("e"+str(entrevista_nota))

                teorica_nota = input_valido("Teórica: ")
                if teorica_nota == -1:
                    continua_candidato = False
                else:
                    guarda.append("_t"+str(teorica_nota))

                    pratica_nota = input_valido("Prática: ")
                    if pratica_nota == -1:
                        continua_candidato = False
                    else:
                        guarda.append("_p"+str(pratica_nota))

                        soft_skills_nota = input_valido("Soft Skills: ")
                        if soft_skills_nota == -1:
                            continua_candidato = False
                        else:
                            guarda.append("_s"+str(soft_skills_nota))

                            listaCandidatos.append([nome_candidato, "".join(guarda)])
                            recebe.append([entrevista_nota, teorica_nota, pratica_nota, soft_skills_nota])
                            continua_candidato = False
        except ValueError as e:
            print("Ocorreu um erro:", e)

# Função para verificar a adequação dos candidatos
def verificar_adequacao(notaCorteE, notaCorteT, notaCorteP, notaCorteS):
    media_candidatos = []
    for i in range(len(listaCandidatos)):
        elimina = 0
        media = sum(recebe[i]) / len(recebe[i])
        media_candidatos.append((i, media))
        for j in range(len(recebe[i])):
            if j == 0 and recebe[i][j] < notaCorteE:
                elimina += 1
            elif j == 1 and recebe[i][j] < notaCorteT:
                elimina += 1
            elif j == 2 and recebe[i][j] < notaCorteP:
                elimina += 1
            elif j == 3 and recebe[i][j] < notaCorteS:
                elimina += 1
        if elimina >= 1:
            print("O Candidato ", listaCandidatos[i][0], " não é aderente à vaga.")
        else:
            print("O Candidato ", listaCandidatos[i][0], " possui o perfil que a empresa procura.")
            print(f"{listaCandidatos[i][1]} - {listaCandidatos[i][0]}")

    # Classificar os candidatos de acordo com a média
    media_candidatos.sort(key=lambda x: x[1], reverse=True)
    print("\nRanking dos candidatos de acordo com a média: ")
    for rank, (i, media) in enumerate(media_candidatos, start=1):
        print(f"{rank}. {listaCandidatos[i][0]} - Média: {media:.2f}")

# Chamada da função para verificar a adequação
verificar_adequacao(notaCorteE, notaCorteT, notaCorteP, notaCorteS)
