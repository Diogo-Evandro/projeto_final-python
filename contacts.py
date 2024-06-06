#contacts.py

from tabulate import tabulate

# Função para adicionar um contacto

def adicionar_contacto(nome, email, numero, endereço):
    try:
        with open("contacts.txt", "a") as file:
            file.write(f"{nome},{numero},{email},{endereço}\n")
        print("Contacto adicionado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o contacto: {str(e)}")


# Função para editar um contacto

def editar_contacto(nome, novo_nome=None, novo_numero=None):
    try:
        with open("contacts.txt", "r") as file:
            linhas = file.readlines()
        with open("contacts.txt", "w") as file:
            for linha in linhas:
                partes = linha.strip().split(",")
                if partes[0] == nome:
                    if novo_nome:
                        partes[0] = novo_nome
                    if novo_numero:
                        partes[2] = novo_numero
                    linha = ",".join(partes) + "\n"
                file.write(linha)
        print("Contacto editado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao editar o contacto: {str(e)}")


# Função para remover um contacto

def remover_contacto(nome):
    try:
        with open("contacts.txt", "r") as file:
            linhas = file.readlines()
        with open("contacts.txt", "w") as file:
            for linha in linhas:
                if linha.strip().split(",")[0] != nome:
                    file.write(linha)
        print("Contacto removido com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao remover o contacto: {str(e)}")


# Função para pesquisar um contacto por nome

def pesquisar_contacto_nome(nome):
    try:
        with open("contacts.txt", "r") as file:
            for linha in file:
                partes = linha.strip().split(",")
                if partes[0] == nome:
                    print("Nome: ", partes[0])
                    print("Email: ", partes[1])
                    print("Numero: ", partes[2])
                    print("Endereço: ", partes[3])
                    return
        print("Contacto não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao pesquisar o contacto: {str(e)}")


# Função para pesquisar um contacto por numero

def pesquisar_contacto_numero(numero):
    try:
        with open("contacts.txt", "r") as file:
            for linha in file:
                partes = linha.strip().split(",")
                if partes[2] == numero:
                    print("Nome: ", partes[0])
                    print("Email: ", partes[1])
                    print("Numero: ", partes[2])
                    print("Endereço: ", partes[3])
                    return
        print("Contacto não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao pesquisar o contacto: {str(e)}")
    

# Funções para ler e escrever no ficheiro de contactos

def ler_ficheiro():
    try:
        dados = []
        with open("contacts.txt", "r") as file:
            print("Lista de contactos: \n")
            for linha in file:
                dados.append(linha.strip().split(','))
            print(tabulate(dados, headers= ["Nome","Email","Numero","Endereco"], tablefmt='grid'))
    except Exception as e:
        print(f"Ocorreu um erro ao ler o ficheiro de contactos: {str(e)}")

def escrever_ficheiro(contactos):
    try:
        with open("contacts.txt", "w") as file:
            for contacto in contactos:
                file.write(",".join(contacto) + "\n")
        print("Ficheiro de contactos atualizado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no ficheiro de contactos: {str(e)}")


