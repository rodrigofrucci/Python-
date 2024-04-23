dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
votos = [0, 0, 0, 0, 0]
# Número de colaboradores
num_colaboradores = int(input("Quantos colaboradores irão participar da votação? "))
# Receber os votos
for i in range(num_colaboradores):
    print(f"Colaborador {i + 1}:")
    print("Escolha o dia da semana para a live:")
    for index, dia in enumerate(dias_semana, 1):
        print(f"{index} - {dia}")
    # Contabilizar voto
    voto = int(input("Digite o número correspondente ao dia: "))
    # Verificar voto
    if voto >= 1 and voto <= 5:
        votos[voto - 1] += 1
    else:
        print("Voto inválido. Tente novamente.")
# Verificar se houve empate
max_votos = max(votos)
dias_empate = [dias_semana[i] for i, v in enumerate(votos) if v == max_votos]
if len(dias_empate) > 1:
    print("Houve um empate entre os seguintes dias:")
    for dia in dias_empate:
        print(f"- {dia} com {max_votos} votos")
else:
    # Dia mais votado
    indice_dia_mais_votado = votos.index(max_votos)
    dia_mais_votado = dias_semana[indice_dia_mais_votado]
    # Resultado
    print("\nResultado da votação:")
    print(f"O dia escolhido para a live é: {dia_mais_votado}, com {max_votos} votos.")



