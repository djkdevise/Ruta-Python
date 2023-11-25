#Calculadora de pesos a Monedas
dollar = 10
pesos = 50000

dollar_to_pesos = 4500
pesos_to_dollar = 1 / dollar_to_pesos  # Invertir la tasa de conversión


print(pesos, "Pesos son", round(pesos / dollar_to_pesos, 2), "dolares")
print(dollar, "Dolares son", round(dollar / pesos_to_dollar, 2), "Pesos")
