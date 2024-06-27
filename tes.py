def somar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


# Dicionário de funções
funcoes = {
    "somar": somar,
    "subtrair": subtrair
}

# Pega a escolha do usuário
choice = input("Qual função deseja usar (somar/subtrair) => ")

# Verifica se a escolha está no dicionário de funções
if choice in funcoes:
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    resultado = funcoes[choice](x, y)
    print(f"O resultado é: {resultado}")
else:
    print("Função inválida.")
