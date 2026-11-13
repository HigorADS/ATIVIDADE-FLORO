def pedir_idade(pessoa):
    while True:
        entrada = input(f"Digite a idade da {pessoa}: ").strip()

        try:
            idade = int(entrada)
        except ValueError:
            print("Digite uma idade usando um número inteiro.")
            continue

        if idade < 0:
            print("A idade não pode ser negativa.")
            continue

        return idade


def main():
    idades = [
        ("Pessoa 1", pedir_idade("Pessoa 1")),
        ("Pessoa 2", pedir_idade("Pessoa 2")),
    ]

    for pessoa, idade in idades:
        if idade >= 18:
            print(f"{pessoa} tem {idade} anos e é maior de idade.")
        else:
            print(f"{pessoa} tem {idade} anos e é menor de idade.")


if __name__ == "__main__":
    main()
