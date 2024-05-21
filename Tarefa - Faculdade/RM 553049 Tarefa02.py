#Preço do carro
valor_carro = float(input("Digite o preço do carro: "))
#Desconto à vista
valor_avista = valor_carro * 0.8
#Tabela Parcelas
parcela_acrescimo = [
    (6, 0.03),
    (12, 0.06),
    (18, 0.09),
    (24, 0.12),
    (30, 0.15),
    (36, 0.18),
    (42, 0.21),
    (48, 0.24),
    (54, 0.27),
    (60, 0.30)
]
#tabela
print(f"O valor do carro a vista do carro com 20% de desconto é: R${valor_avista:.2f}")
for parcela, acrescimo in parcela_acrescimo:
    valor_final = valor_avista * (1 + acrescimo)
    valor_parcela = valor_final / parcela
    print(f"Preço final: R${valor_final:.2f}  |  Número de parcelas {parcela}x  |  Valor das parcelas: R${valor_parcela:.2f}")
