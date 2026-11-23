from funções import lanche, bebidas, calcular_preco
from listas import lista_de_preco, lista_de_preco_bebidas
from funções import dinheiro, pagamento, nota_fiscal
from funções import validar_email


# LANCHONETE
print("Seja muito bem vindo, a nossa lanchonete")

# LOGIN DE CLIENTE
while True:
    try:
        nome = input("Digite qual o seu nome: ")
        if nome.startswith(" ") or nome.endswith(" "):
            print("Não pode começar ou terminar com espaço")
            continue
        if "  " in nome:
            print("Não pode ter mais de um espaço entre os nomes")
            continue
        if len(nome) < 4:
            print("Nome inválido. Tem que ter pelo menos 4 letras.")
            continue
        if len(nome) > 50:
            print("Nome inválido. Tem que ter no máximo 50 letras.")
            continue
        if any(letra.isdigit() for letra in nome):
            print("Não pode conter número no seu nome")
            continue
        if any(not letra.isalpha() and not letra.isspace() for letra in nome):
            print("Não pode conter caracteres especiais no seu nome")
            continue
        print(f"Seja bem vindo {nome}")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um nome válido.")

validar_email()
print("login concluido")
#DINHEIRO DO CLIENTE
meudinheiro = dinheiro()

# OPÇÃO DE COMPRAR MAIS DE UM LANCHES
total = 0
while True:
    lanche()
    while True:
        try:
            escolha = int(input("Digite o número do item que deseja comprar: "))
            if escolha < 1 or escolha > len(lista_de_preco):
                print("Escolha inválida. Por favor, digite um número válido.")
                continue
            quantidade = int(input("Digite a quantidade que deseja comprar: "))
            if quantidade < 1:
                print("Tem que ser pelo menos 1")
                continue
            break 
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    total += calcular_preco(escolha, quantidade)

    mais = input("Quer comprar mais algum produto? sim/nao: ").strip().lower()
    if mais != "sim":
        break

#OPÇÃO DE COMPRAR BEBIDAS
total2 = 0
while True:
    bebidas()
    while True:
        try:
            escolha_bebida = int(input("Digite o número da bebida que deseja comprar: "))
            if escolha_bebida < 1 or escolha_bebida > len(lista_de_preco_bebidas):
                print("Escolha inválida. Por favor, digite um número válido.")
                continue
            quantidade_bebida = int(input("Digite a quantidade que deseja comprar: "))
            if quantidade_bebida < 1:
                print("Tem que ser pelo menos 1")
                continue
            break 
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    total2 += lista_de_preco_bebidas[escolha_bebida - 1] * quantidade_bebida

    mais_bebida = input("Quer comprar mais alguma bebida? sim/nao: ").strip().lower()
    if mais_bebida != "sim":
        break
 
total3 = total + total2
print(f"O total da sua compra é: R$ {total3:.2f}")

#ESCOLHA DE PAGAMENTO
escolha_pagamento = input("Escolha a forma de pagamento (dinheiro/cartão): ").strip().lower()
if escolha_pagamento == "dinheiro":
    if pagamento(total3, meudinheiro) == True:
        print("Compra finalizada com sucesso!")
    else:
        print("Compra não realizada devido a falta de dinheiro.")
elif escolha_pagamento == "cartão" or escolha_pagamento == "cartao":
    print("Compra realizada com sucesso no cartão!")
else:
    print("Forma de pagamento inválida. Por favor, escolha entre 'dinheiro' ou 'cartão'.")

nota_fiscal(nome, total3, meudinheiro - total3)

