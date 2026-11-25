# ============================================
#     TechStock - Controle de estoque TechPoint
#     Aluno(a): Gabriel Alex Martins Ribeiro
# ============================================

import json

ARQUIVO = "estoque.json"

produtos = []
movimentacoes = []
historico = []
fila_reposicao = []


####### salvar estoque #######
def salvar_estoque():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)


####### buscar produto #######
def buscar_produto(codigo):
    for p in produtos:
        if p["codigo"] == codigo:
            return p
    return None


####### registrar historico #######
def registrar_historico(produto, descricao):
    historico.append({
        "codigo": produto["codigo"],
        "quantidade_antes": produto["quantidade"],
        "descricao": descricao
    })


####### cadastro do produto #######
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
    salvar_estoque()
    print("Produto cadastrado!")


####### registrar entrada #######
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

    registrar_historico(produto, "entrada")
    produto["quantidade"] = produto["quantidade"] + qtd
    movimentacoes.append({
        "tipo": "Entrada",
        "produto": produto["nome"],
        "quantidade": qtd
    })
    salvar_estoque()
    print("Entrada registrada!")


####### registrar venda #######
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

    registrar_historico(produto, "saída")
    produto["quantidade"] = produto["quantidade"] - qtd
    valor_venda = qtd * produto["preco"]

    movimentacoes.append({
        "tipo": "Venda",
        "produto": produto["nome"],
        "quantidade": qtd,
        "valor": valor_venda
    })
    salvar_estoque()
    print(f"Venda registrada! Total: R$ {valor_venda:.2f}")


####### ficha do produto #######
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


####### grafico do estoque #######
def grafico_estoque():
    print("\n--- Gráfico do estoque ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for p in produtos:
        barras = "#" * p["quantidade"]
        print(f"{p['nome']}: {barras} ({p['quantidade']})")


####### inventario por prateleira #######
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

    if not achou:
        print("Nenhum produto nessa prateleira.")


####### relatorio do dia #######
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


####### alterar preco #######
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
        salvar_estoque()
        print("Preço atualizado!")


####### excluir produto #######
def excluir_produto():
    print("\n--- Excluir produto ---")
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)

    if produto == None:
        print("Produto não encontrado.")
    else:
        produtos.remove(produto)
        salvar_estoque()
        print("Produto excluído!")


####### buscar por codigo #######
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


####### atualizar produto #######
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
        salvar_estoque()
        print("Nome atualizado!")
    elif escolha == "2":
        nova_qtd = int(input("Nova quantidade: "))
        if nova_qtd < 0:
            print("Quantidade inválida!")
        else:
            registrar_historico(encontrado, "quantidade alterada")
            encontrado["quantidade"] = nova_qtd
            salvar_estoque()
            print("Quantidade atualizada!")
    else:
        print("Opção inválida.")


####### relatorio geral #######
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


####### desfazer ultima alteracao #######
def desfazer():
    if len(historico) == 0:
        print("Nada para desfazer.")
        return

    ultimo = historico.pop()
    produto = buscar_produto(ultimo["codigo"])
    if produto == None:
        print("O produto dessa alteração não existe mais.")
        return

    produto["quantidade"] = ultimo["quantidade_antes"]
    salvar_estoque()
    print("Desfeito:", ultimo["descricao"], "-", produto["nome"])
    print("A quantidade voltou para", produto["quantidade"])


####### ver historico #######
def ver_historico():
    if len(historico) == 0:
        print("Histórico vazio.")
        return

    print("Do mais recente para o mais antigo:")
    i = len(historico) - 1
    while i >= 0:
        registro = historico[i]
        print("-", registro["descricao"], "| código", registro["codigo"], "| antes:", registro["quantidade_antes"])
        i = i - 1


####### pedir reposicao #######
def pedir_reposicao():
    codigo = int(input("Código do produto: "))
    produto = buscar_produto(codigo)
    if produto == None:
        print("Produto não encontrado.")
        return

    quantidade = int(input("Quantas unidades pedir? "))
    if quantidade <= 0:
        print("Quantidade inválida!")
        return

    fila_reposicao.append({
        "codigo": codigo,
        "quantidade": quantidade
    })
    print("Pedido na fila. Posição:", len(fila_reposicao))


####### receber reposicao #######
def receber_reposicao():
    if len(fila_reposicao) == 0:
        print("Nenhum pedido na fila.")
        return

    pedido = fila_reposicao.pop(0)
    produto = buscar_produto(pedido["codigo"])
    if produto == None:
        print("O produto não existe mais. Pedido descartado.")
        return

    registrar_historico(produto, "reposição recebida")
    produto["quantidade"] = produto["quantidade"] + pedido["quantidade"]
    salvar_estoque()
    print("Chegaram", pedido["quantidade"], "unidade(s) de", produto["nome"])
    print("Pedidos restantes na fila:", len(fila_reposicao))


####### ver fila #######
def ver_fila():
    if len(fila_reposicao) == 0:
        print("Fila de reposição vazia.")
        return

    for i in range(len(fila_reposicao)):
        pedido = fila_reposicao[i]
        print(f"{i + 1}º lugar | código {pedido['codigo']} | {pedido['quantidade']} unidade(s)")


####### exibir menu #######
def exibir_menu():
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
    print("18 - Desfazer última alteração")
    print("19 - Ver histórico")
    print("20 - Pedir reposição")
    print("21 - Receber próxima reposição")
    print("22 - Ver fila de reposição")
    print("0 - Sair")


####### loop principal #######
while True:
    exibir_menu()
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
    elif opcao == "18":
        desfazer()
    elif opcao == "19":
        ver_historico()
    elif opcao == "20":
        pedir_reposicao()
    elif opcao == "21":
        receber_reposicao()
    elif opcao == "22":
        ver_fila()
    elif opcao == "0":
        salvar_estoque()
        print("Estoque salvo. Saindo do TechStock...")
        break
    else:
        print("Opção inválida.")