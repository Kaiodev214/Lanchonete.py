from listas import lista_de_preco, lista_de_preco_bebidas
from lanchonete import total3

def lanche():
    print("Cardápio de lanches")
    print(f"1. Hambúrguer - R$ {lista_de_preco[0]:.2f}")
    print(f"2. X-Salada - R$ {lista_de_preco[1]:.2f}")
    print(f"3. X-tudo- R$ {lista_de_preco[2]:.2f}")
    print(f"4. Pizza de calabresa - R$ {lista_de_preco[3]:.2f}")
    print(f"5. Porção de batata frita - R$ {lista_de_preco[4]:.2f}" )

def bebidas ():
    print("Cardápio de bebidas")
    print(f"1. Coca-Cola 350ml - R$ {lista_de_preco_bebidas[0]:.2f}")
    print(f"2. Coca-Cola 600ml - R$ {lista_de_preco_bebidas[1]:.2f}")
    print(f"3. Coca-Cola 2L - R$ {lista_de_preco_bebidas[2]:.2f}")
    print(f"4. Guaraná 350ml - R$ {lista_de_preco_bebidas[3]:.2f}")
    print(f"5. Guaraná 600ml - R$ {lista_de_preco_bebidas[4]:.2f}")
    print(f"6. Guaraná 2L - R$ {lista_de_preco_bebidas[5]:.2f}")
    print(f"7. Água Mineral 500ml - R$ {lista_de_preco_bebidas[6]:.2f}")

def calcular_preco(escolha, quantidade):
    return lista_de_preco[escolha - 1] * quantidade

def dinheiro():
    while True:
        
        try:
            
            dinheiro = float(input("Qual o seu saldo? "))
            if dinheiro < 0:
                print("o seu saldo não pode ser negativo ")
                continue
            return dinheiro
        
        except ValueError:
                print("Digite um numero válido")
        

def pagamento(total, dinheiro):
    troco = dinheiro - total
    if dinheiro >= total:
        print(f"Pagamento realizado! Seu troco é R$ {troco:.2f}")
        return True
    else:
        print("Dinheiro insuficiente!")
        return False

def nota_fiscal(nome, total3, troco):
    print("\n----Nota Fiscal----")
    print(f"Cliente: {nome}")
    print(f"Total da compra: R$ {total3:.2f}")
    print(f"valor pago: R$ {total3:.2f}")
    print(f"Troco: R$ {troco:.2f}")
    

def validar_email():

    while True:

        print("======================")
        email = input("Digite seu email: ").strip().lower()
        print("======================")

        partes = email.split("@")

        if email == "":
            print("Email vazio!")

        elif email.count("@") != 1:
            print("Tem que ter exatamente 1 @!")

        elif len(email) < 12:
            print("O seu email precisa ter pelo menos 12 caracteres!")

        elif len(email) > 65:
            print("O seu email precisa ter menos de 65 caracteres!")

        elif " " in email:
            print("Email não pode ter espaços!")

        elif partes[0] == "":
            print("Falta o nome antes do @!")

        elif partes[1] == "":
            print("Falta o domínio depois do @!")

        elif "." not in partes[1]:
            print("Falta o ponto depois do @!")

        else:
            dominio = partes[1].split(".")

            if dominio[0] == "":
                print("Você precisa colocar um domínio!")

            elif dominio[1] == "":
                print("Você precisa colocar o final do domínio!")

            else:
                print("Email válido!")
                break