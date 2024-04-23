while True:
    # Tipo de Investimento
    investimento = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
    valor_resgate = float(input("Insira o valor a ser resgatado R$: "))
    dias_investidos = int(input("Insira o número de dias que o valor da aplicação permaneceu investido: "))
    #CDB
    if investimento == 1:
        if dias_investidos <= 180:
            aliquota_ir = 0.225
        elif 181 >= dias_investidos <= 360:
            aliquota_ir = 0.20
        elif 361 >= dias_investidos <= 720:
            aliquota_ir = 0.175
        else:
            aliquota_ir = 0.15
        break
    # LCI e LCA
    elif investimento == 2 or investimento == 3:
        aliquota_ir = 0
        break
    else:
        print("Erro! Investimento inválido. \n TENTE NOVAMENTE!")
#Cálculo
valor_ir = valor_resgate * aliquota_ir
valor_liquido = valor_resgate - valor_ir
#Resultado
print(f"O Valor do IR: R${valor_ir:.2f}")
print(f"O Valor líquido após o IR: R${valor_liquido:.2f}")