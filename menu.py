transactions = list()


# Uma transação contém os campos id, tipo, valor, categoria, descricao e data

while (True):
    print("-"*20)
    print(" " * 9 + "Gerenciador Financeiro")
    print("-"*20)
    print()

    print("1 - Adicionar Transação")
    print("2 - Listar Transações")
    print("3 - Sair")
    escolha = int(input("Escolha: "))

    if escolha == 3: break

    if escolha == 1:
        tipo = int(input("1 - Receita\n2 - Despesa\nEscolha: "))
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

        

