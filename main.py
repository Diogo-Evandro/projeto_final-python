#main.py

import contacts

def mostrar_menu():
    print("")
    print("MENU:")
    print("")
    print("1. Adicionar Contacto")
    print("2. Editar Contacto")
    print("3. Remover Contacto")
    print("4. Pesquisar Contacto por Nome")
    print("5. Pesquisar Contacto por Numero")
    print("6. Listar Contacto")
    print("7. Sair")
    print("")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        print("")
        if opcao =="1":
            nome = input("Nome: ")
            email = input("Email: ")
            numero = input("Numero: ")
            endereco = input("Enderço: ")
            contacts.adicionar_contacto(nome, email, numero, endereco)
        elif opcao =="2":
            nome = input("Nome do contacto a ser editado: ")
            novo_nome = input("Novo nome (deixe em branco para manter o mesmo): ")
            novo_numero = input("Novo numero (deixe em branco para manter o mesmo): ")
            contacts.editar_contacto(nome, novo_nome, novo_numero)
        elif opcao =="3":
            nome = input("Nome do contacto a ser removido: ")
            contacts.remover_contacto(nome)
        elif opcao =="4":
            nome = input("Nome do contacto a ser pesquisado: ")
            contacts.pesquisar_contacto_nome(nome)
        elif opcao =="5":
            numero = input("Numero do contacto a ser pesquisado: ")
            contacts.pesquisar_contacto_numero(numero)
        elif opcao =="6":
            contacts.ler_ficheiro()
        elif opcao =="7":
            print("Saindo...")
            break
        else:
            print("Opção invalida. Tente novamente.")

if __name__ == "__main__":
    main()



