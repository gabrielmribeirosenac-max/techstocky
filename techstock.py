# ============================================
#     TechStock - Controle de estoque TechPoint
#     Aluno(a): Gabriel Alex Martins Ribeiro
# ============================================


print("=================================")
print("         TECHSTOCK - TECHPOINT")
print("=================================")

#######  cadastro do produto ####### 
codigo = input("Código do produto: ")
nome = input("Nome do produto: ")
preco = float(input("Preço de venda (R$): "))
quantidade = int(input("Quantidade em estoque: "))
estoque_minimo = int(input("Estoque mínimo: "))

#######  validação do cadastro ####### 
if preco > 0 and quantidade >= 0 and estoque_minimo >= 0:
    print("Cadastro válido!")

    #######  menu de operações ####### 
    print()
    print("O que você deseja fazer?")
    print("[1] Registrar entrada (chegou mercadoria)")
    print("[2] Registrar saída (venda)")
    print("[3] Apenas consultar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        entrada = int(input("Quantas unidades chegaram? "))

        if entrada > 0:
            quantidade = quantidade + entrada
            print("Entrada registrada:", entrada, "unidade(s).")
        else:
            print("ERRO: a quantidade de entrada precisa ser maior que zero.")

    elif opcao == "2":
        saida = int(input("Quantas unidades foram vendidas? "))

        if saida <= 0:
            print("ERRO: a quantidade de saída precisa ser maior que zero.")
        elif saida > quantidade:
            print("ERRO: estoque insuficiente. Disponível:", quantidade)
        else:
            quantidade = quantidade - saida
            print("Saída registrada:", saida, "unidade(s).")

    elif opcao == "3":
        print("Consulta selecionada.")

    else:
        print("Opção inválida. Mostrando apenas a ficha.")

    ####### cálculos ####### 
    valor_total = preco * quantidade
    valor_total = round(valor_total, 2)

    #######  ficha do produto ####### 
    print("=================================")
    print("Código:", codigo)
    print("Produto:", nome)
    print(f"Preço: R$ {preco:.2f}")
    print("Quantidade:", quantidade, "unidade(s)")
    print("Estoque mínimo:", estoque_minimo)
    print(f"Valor total: R$ {valor_total:.2f}")

    ####### situação do estoque ####### 
    if quantidade == 0:
        print("Situação: SEM ESTOQUE - repor urgente!")
    elif quantidade < estoque_minimo:
        faltam = estoque_minimo - quantidade
        print("Situação: ESTOQUE BAIXO - repor pelo menos", faltam, "unidade(s)")
    else:
        print("Situação: ESTOQUE OK")

    print("=================================")

else:
    print("ERRO: cadastro inválido.")
    print("O preço deve ser maior que zero e as quantidades não podem ser negativas.")