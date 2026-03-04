def adicionar_contatos(nome, telefone,email,agenda):
    contato={"Nome": nome, "Telefone": telefone, "E-mail": email, "Favorito":False}
    agenda.append(contato)
    print("Contato adicionado com sucesso!")
    

def ver_contatos(agenda):
    if len(agenda) == 0:
        print("\n Nenhum contato cadastrado.")
        return
    print("\n ---- Contatos ----")
    for i, contato in enumerate(agenda, start=1):
        favorito = "⭐" if contato["Favorito"] else " "
        print(f"{i}. [{favorito}] {contato['Nome']} | {contato['Telefone']} | {contato['E-mail']}")


def atualizar_contato(agenda, indice_agenda, novo_nome=None, novo_telefone=None, novo_email=None):
    indice = int(indice_agenda) - 1

    if 0 <= indice < len(agenda):
        if novo_nome:
            agenda[indice]["Nome"] = novo_nome
        if novo_telefone:
            agenda[indice]["Telefone"] = novo_telefone
        if novo_email:
            agenda[indice]["E-mail"] = novo_email

        print("Contato atualizado com sucesso!")
    else:
        print("Índice de contato inválido.")
        
def deletar_contato(agenda, indice_agenda):
    indice = int(indice_agenda) - 1

    if 0 <= indice < len(agenda):
        contato_removido = agenda.pop(indice)
        print(f"Contato {contato_removido['Nome']} removido com sucesso!")
    else:
        print("Índice inválido.")    

def favoritar_contato(agenda, indice_agenda):
    indice = int(indice_agenda) - 1

    if 0 <= indice < len(agenda):
        agenda[indice]["Favorito"] = not agenda[indice]["Favorito"]

        if agenda[indice]["Favorito"]:
            print(f"Contato {agenda[indice]['Nome']} favoritado ⭐")
        else:
            print(f"Contato {agenda[indice]['Nome']} desfavoritado.")
    else:
        print("Índice inválido.")

def ver_favoritos(agenda):
    favoritos = [contato for contato in agenda if contato["Favorito"]]

    if len(favoritos) == 0:
        print("\nNenhum contato favoritado.")
        return

    print("\n--- Contatos Favoritos ---")
    for i, contato in enumerate(favoritos, start=1):
        print(f"{i}. ⭐ {contato['Nome']} | {contato['Telefone']} | {contato['E-mail']}")
        
agenda_contatos=[]
while True:
    print("\n Agenda de contatos")
    print("1- Adicionar Contato")
    print("2- Ver Contatos")
    print("3- Atualizar Contato")
    print("4- Deletar Contato")
    print("5- Favoritar Contato")
    print("6- Ver Favoritos")
    print("7- Sair")
    
    escolha_user= input("Digite um número para acessar a agenda:")
   
    if escolha_user =="1":
       nome = input("Digite o nome: ")
       telefone = input("Digite o telefone: ")
       email = input("Digite o e-mail: ")
       adicionar_contatos(nome, telefone, email, agenda_contatos)
    
    elif escolha_user == "2":
        ver_contatos(agenda_contatos) 
        
    elif escolha_user == "3":
        ver_contatos(agenda_contatos)
        indice_agenda = input("Digite o índice do contato que deseja atualizar: ")

        novo_nome = input("Novo nome (enter para manter): ").strip()
        novo_telefone = input("Novo telefone (enter para manter): ").strip()
        novo_email = input("Novo e-mail (enter para manter): ").strip()

        atualizar_contato(
            agenda_contatos,
            indice_agenda,
            novo_nome if novo_nome else None,
            novo_telefone if novo_telefone else None,
            novo_email if novo_email else None
        )
    elif escolha_user == "4":
        ver_contatos(agenda_contatos)
        indice_agenda = input("Digite o índice do contato que deseja deletar: ")
        deletar_contato(agenda_contatos, indice_agenda)
        
    elif escolha_user == "5":
        ver_contatos(agenda_contatos)
        indice_agenda = input("Digite o índice do contato que deseja favoritar/desfavoritar: ")
        favoritar_contato(agenda_contatos, indice_agenda)
    
    elif escolha_user == "6":
        ver_favoritos(agenda_contatos)

    elif escolha_user == "7":
        break
print("Fim do programa")