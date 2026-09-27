import re

transactions = list()


# Uma transação contém os campos id, tipo, valor, descricao e data.
# Tirei categoria pois não acho que faz sentido por enquanto.

while (True):
    print("-"*20)
    print("Gerenciador Financeiro")
    print("-"*20)
    print()

    print("1 - Adicionar Transação")
    print("2 - Listar Transações")
    print("3 - Sair")
    escolha = int(input("Escolha: "))

    if escolha == 3: break

    if escolha == 1:
        
        tipo = int(input("\n1 - Receita\n2 - Despesa\nTipo: "))
        if tipo != 1 and tipo != 2:
            print("\nEscolha do tipo inválida!\nTente novamente\n")
            continue

        tipo = "receita" if tipo == 1 else "despesa"

        try:
            valor = float(input("Valor: "))
        except ValueError:
            print("\nValor digitado inválido.\nTente novamente\n")
            continue

        descricao = input("Descrição: ")
        data = input("Data:" )

        if not re.match(r"\d\d\/\d\d\/\d\d\d\d", data):
            print("\nFormato de data inválido.\nData deve ser: dd/mm/yyyy\n")
            continue

        transactions.append({
            "tipo": tipo,
            "valor": valor,
            "descricao": descricao,
            "data": data,
        })
        print("\n")

    elif escolha == 2:
        if len(transactions) == 0:
            print("\nNão há transações realizadas.\n")
            continue

        print("-"*30)
        print("Lista de Transações")
        for transaction in transactions:
            print(f"Tipo: {transaction["tipo"]}")
            print(f"Valor: {transaction["valor"]}")
            print(f"Descrição: {transaction["descricao"]}")
            print(f"Data: {transaction["data"]}\n")

        print("-"*30)




