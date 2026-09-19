#Proposta: 4. Peça uma temperatura em graus Celsius e converta para Fahrenheit. A fórmula é F = C × 9 / 5 + 32.
celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} °C é igual á {fahrenheit} °F")