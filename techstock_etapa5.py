# ============================================
#     TechStock - Controle de estoque TechPoint
#     Aluno(a): Gabriel Alex Martins Ribeiro
# ============================================

produtos = []
movimentacoes = []


def buscar_produto(codigo):
    for p in produtos:
        if p["codigo"] == codigo:
            return p
    return None


def cadastrar_produto():
    print("\n--- Cadastro de produto ---")
    codigo = int(input("Código do produto: "))

    if buscar_produto(codigo) != None:
        print("Código já cadastrado!")
        return

    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    prateleira = input("Prateleira: ")

    if quantidade < 0 or preco < 0:
        print("Valores inválidos! Não pode ser negativo.")
        return

    novo = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "prateleira": prateleira
    }
    produtos.append(novo)
    print("Produto cadastrado!")


def registrar_entrada():
    print("\n--- Registrar entrada ---")
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
        return

    qtd = int(input("Quantidade que entrou: "))
    if qtd <= 0:
        print("Quantidade inválida!")
        return

    produto["quantidade"] = produto["quantidade"] + qtd
    movimentacoes.append({
        "tipo": "Entrada",
        "produto": produto["nome"],
        "quantidade": qtd
    })
    print("Entrada registrada!")


def registrar_venda():
    print("\n--- Registrar venda ---")
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
        return

    qtd = int(input("Quantidade vendida: "))
    if qtd <= 0:
        print("Quantidade inválida!")
        return

    if qtd > produto["quantidade"]:
        print("Estoque insuficiente!")
        return

    produto["quantidade"] = produto["quantidade"] - qtd
    valor_venda = qtd * produto["preco"]

    movimentacoes.append({
        "tipo": "Venda",
        "produto": produto["nome"],
        "quantidade": qtd,
        "valor": valor_venda
    })
    print(f"Venda registrada! Total: R$ {valor_venda:.2f}")


def ficha_produto():
    print("\n--- Ficha do produto ---")
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
    else:
        subtotal = produto["quantidade"] * produto["preco"]
        print("Código:", produto["codigo"])
        print("Nome:", produto["nome"])
        print("Quantidade:", produto["quantidade"])
        print(f"Preço: R$ {produto['preco']:.2f}")
        print("Prateleira:", produto["prateleira"])
        print(f"Valor em estoque: R$ {subtotal:.2f}")


def grafico_estoque():
    print("\n--- Gráfico do estoque ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for p in produtos:
        barras = "#" * p["quantidade"]
        print(f"{p['nome']}: {barras} ({p['quantidade']})")


def inventario_prateleira():
    print("\n--- Inventário por prateleira ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    prat = input("Digite a prateleira: ")
    achou = False

    for p in produtos:
        if p["prateleira"] == prat:
            print(p["codigo"], "-", p["nome"], "| Qtd:", p["quantidade"])
            achou = True

    if achou == False:
        print("Nenhum produto nessa prateleira.")


def relatorio_dia():
    print("\n--- Relatório do dia ---")
    if len(movimentacoes) == 0:
        print("Nenhuma movimentação hoje.")
        return

    total_vendas = 0
    for m in movimentacoes:
        print(m["tipo"], "-", m["produto"], "- Qtd:", m["quantidade"])
        if m["tipo"] == "Venda":
            total_vendas = total_vendas + m["valor"]

    print(f"Total vendido: R$ {total_vendas:.2f}")


def alterar_preco():
    print("\n--- Alterar preço ---")
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
        return

    novo_preco = float(input("Novo preço: "))
    if novo_preco < 0:
        print("Preço inválido!")
    else:
        produto["preco"] = novo_preco
        print("Preço atualizado!")


def excluir_produto():
    print("\n--- Excluir produto ---")
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
    else:
        produtos.remove(produto)
        print("Produto excluído!")


def buscar_por_codigo():
    print("\n--- Buscar produto ---")
    codigo = int(input("Código para buscar: "))
    encontrado = buscar_produto(codigo)

    if encontrado == None:
        print("Produto não encontrado.")
    else:
        print("Nome:", encontrado["nome"])
        print("Quantidade:", encontrado["quantidade"])
        print(f"Preço: R$ {encontrado['preco']:.2f}")
        print("Prateleira:", encontrado["prateleira"])


def atualizar_produto():
    print("\n--- Atualizar produto ---")
    codigo = int(input("Código do produto: "))
    encontrado = buscar_produto(codigo)

    if encontrado == None:
        print("Produto não encontrado.")
        return

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


def relatorio_geral():
    print("\n====== RELATÓRIO GERAL ======")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    total = 0
    for produto in produtos:
        subtotal = produto["quantidade"] * produto["preco"]
        total = total + subtotal

        print(produto["codigo"], "-", produto["nome"])
        print("Quantidade:", produto["quantidade"])
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Subtotal: R$ {subtotal:.2f}")

    print(f"Total do estoque: R$ {total:.2f}")


while True:
    print("\n===== TECHSTOCK =====")
    print("1 - Cadastrar produto")
    print("2 - Registrar entrada")
    print("3 - Registrar venda")
    print("4 - Ficha do produto")
    print("5 - Gráfico do estoque")
    print("6 - Inventário por prateleira")
    print("7 - Relatório do dia")
    print("8 - Alterar preço")
    print("9 - Excluir produto")
    print("10 - Buscar produto")
    print("11 - Atualizar nome ou quantidade")
    print("12 - Relatório geral")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        registrar_entrada()
    elif opcao == "3":
        registrar_venda()
    elif opcao == "4":
        ficha_produto()
    elif opcao == "5":
        grafico_estoque()
    elif opcao == "6":
        inventario_prateleira()
    elif opcao == "7":
        relatorio_dia()
    elif opcao == "8":
        alterar_preco()
    elif opcao == "9":
        excluir_produto()
    elif opcao == "10":
        buscar_por_codigo()
    elif opcao == "11":
        atualizar_produto()
    elif opcao == "12":
        relatorio_geral()
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida.")