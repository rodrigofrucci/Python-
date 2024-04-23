#Divida
valor_divida = float(input("Insira o valor da dívida: "))
#Juros
juros_parcelas = [
    (1, 0.00),
    (3, 0.10),
    (6, 0.15),
    (9, 0.20),
    (12, 0.25),
]
#tabela
print(f"O valor da dívida é de R${valor_divida:.2f}")
for parcela, juros in juros_parcelas:
    valor_juros = valor_divida * juros
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcela
    print(f"Total: R${valor_total:.2f} | Juros: R${valor_juros:.2f} | Número das parcelas: {parcela}x | Valor das Parcelas: R${valor_parcela:.2f}")