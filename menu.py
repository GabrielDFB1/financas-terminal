import re
import uuid

transactions = []


# Uma transação contém os campos id, tipo, valor, descricao e data.
# Tirei categoria pois não acho que faz sentido por enquanto.

while True:
    print("-"*20)
    print("Gerenciador Financeiro")
    print("-"*20)
    print()

    print("1 - Adicionar Transação")
    print("2 - Listar Transações")
    print("3 - Sair")

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("\nEntrada inválida\nTente novamente\n")
        continue

    if escolha != 1 and escolha != 2 and escolha != 3:
        print("\nValores inválidos\nTentenovamente!\n")
        continue

    if escolha == 3: break

    if escolha == 1:

        try:
            tipo = int(input("\n1 - Receita\n2 - Despesa\nTipo: "))

        except ValueError:
            print("\nEntrada inválida.\nTente novamente\n")
            continue

        if tipo != 1 and tipo != 2:
            print("\nValores inválidos\nTentenovamente!\n")
            continue

        tipo = "receita" if tipo == 1 else "despesa"

        try:
            valor = float(input("Valor: "))
        except ValueError:
            print("\nValor digitado inválido.\nTente novamente\n")
            continue

        categoria = input("Categoria: ")
        categoria = categoria.strip()

        descricao = input("Descrição: ")
        data = input("Data:" )

        if not re.fullmatch(r"\d\d\/\d\d\/\d\d\d\d", data):
            print("\nFormato de data inválido.\nData deve ser: dd/mm/yyyy\n")
            continue

        transactions.append({
            "id": uuid.uuid4(),
            "tipo": tipo,
            "valor": valor,
            "categoria": categoria,
            "descricao": descricao,
            "data": data,
        })

        print("Transação salva com sucesso!\n")

    elif escolha == 2:
        if len(transactions) == 0:
            print("\nNão há transações realizadas.\n")
            continue

        print()
        print("-"*30)
        print("Lista de Transações")
        for transaction in transactions:
            print(f"ID: {transaction['id']}")
            print(f"Tipo: {transaction['tipo']}")
            print(f"Valor: {transaction['valor']}")
            print(f"Categoria: {transaction['categoria']}")
            print(f"Descrição: {transaction['descricao']}")
            print(f"Data: {transaction['data']}\n")

        print("-"*30)




