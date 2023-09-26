nome_pessoa = input("Qual seu nome?")
nome = ("Olá", nome_pessoa)
peso = float(input("Qual seu peso? (kg)"))
altura = float(input("Qual sua altura? (em metros)"))

print("Vamos calcular seu IMC")

imc = (peso / (altura * altura))

print(nome_pessoa , (f"Seu IMC é: {imc:.2f}"))
if imc < 16:
	print("Seu estado é de Magreza grave\n")
elif imc < 17:
	print("Seu estado é de Magreza moderada\n")
elif imc < 18.5:
	print("Seu estado é de Magreza leve\n")
elif imc < 25:
	print("Você está Saudável.\nParabéns!")
elif imc < 30:
	print("Seu estado é de Sobrepeso\n")
elif imc < 35:
	print("Seu estado é de Obesidade Grau I\n")
elif imc < 40:
	print("Seu estado é de Obesidade Grau II (severa)\n")
else:
	print("Seu estado é de Obesidade Grau III (mórbida)\n")