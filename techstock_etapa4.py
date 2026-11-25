produtos = []

while True:
    print("\n===== TECHSTOCK =====")
    print("1 - Cadastrar produto")
    print("10 - Buscar produto")
    print("11 - Alterar produto")
    print("12 - Relatório geral")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        codigo = int(input("Código do produto: "))

        existe = False
        for produto in produtos:
            if produto["codigo"] == codigo:
                existe = True
                break

        if existe:
            print("Código já cadastrado!")
        else:
            nome = input("Nome: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))

            if quantidade < 0 or preco < 0:
                print("Quantidade e preço não podem ser negativos.")
            else:
                novo = {
                    "codigo": codigo,
                    "nome": nome,
                    "quantidade": quantidade,
                    "preco": preco
                }
                produtos.append(novo)
                print("Produto cadastrado!")

    elif opcao == "10":
        codigo = int(input("Código para buscar: "))
        encontrado = None

        for produto in produtos:
            if produto["codigo"] == codigo:
                encontrado = produto
                break

        if encontrado == None:
            print("Produto não encontrado.")
        else:
            print("Nome:", encontrado["nome"])
            print("Quantidade:", encontrado["quantidade"])
            print(f"Preço: R$ {encontrado['preco']:.2f}")

    elif opcao == "11":
        codigo = int(input("Código do produto: "))
        encontrado = None

        for produto in produtos:
            if produto["codigo"] == codigo:
                encontrado = produto
                break

        if encontrado == None:
            print("Produto não encontrado.")
        else:
            print("1 - Alterar nome")
            print("2 - Alterar quantidade")

            escolha = input("Escolha: ")

            if escolha == "1":
                encontrado["nome"] = input("Novo nome: ")
                print("Nome atualizado!")

            elif escolha == "2":
                nova_qtd = int(input("Nova quantidade: "))

                if nova_qtd < 0:
                    print("Quantidade inválida!")
                else:
                    encontrado["quantidade"] = nova_qtd
                    print("Quantidade atualizada!")

            else:
                print("Opção inválida.")

    elif opcao == "12":
        total = 0

        print("====== RELATÓRIO GERAL ======")

        for produto in produtos:
            subtotal = produto["quantidade"] * produto["preco"]
            total = total + subtotal

            print(produto["codigo"], "-", produto["nome"])
            print("Quantidade:", produto["quantidade"])
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Subtotal: R$ {subtotal:.2f}")

        print(f"Total do estoque: R$ {total:.2f}")

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")