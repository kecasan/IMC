def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso normal.")
elif 18.5 <= imc < 24.9:
    print("Você está com peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print("Cuidado: Obesidade grau 1.")
elif 35 <= imc < 39.9:
    print("Cuidado: Obesidade grau 2.")
else:
    print("Cuidado: Obesidade grau 3.")
