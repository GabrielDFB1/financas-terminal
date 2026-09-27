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
        tipo = "receita" if tipo == 1 else "despesa"
        valor = float(input("Valor: "))
        descricao = input("Descrição: ")
        data = input("Data:" )

        transactions.append({
            "tipo": tipo,
            "valor": valor,
            "descricao": descricao,
            "data": data,
        })
        print("\n")

    elif escolha == 2:
        if len(transactions) == 0:
            print("Não há transações realizadas.")
            continue

        print("-"*30)
        print("Lista de Transações")
        for transaction in transactions:
            print(f"Tipo: {transaction["tipo"]}")
            print(f"Valor: {transaction["valor"]}")
            print(f"Descrição: {transaction["descricao"]}")
            print(f"Data: {transaction["data"]}\n")

        print("-"*30)




