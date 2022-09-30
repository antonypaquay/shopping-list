import sys

list = []
is_invalid = True
instructions = """
------------------------------------------------------------
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
"""

while is_invalid:
    print(instructions)
    user_choice = input('Votre choix : ')
    if user_choice.isdigit():
        is_invalid = False
        if user_choice == "1":
            element_to_add = input("Entrer le nom d'un élément à ajouter à la liste de courses : ")
            list.append(element_to_add)
            print(f'L\'élément {element_to_add} a bien été ajouté à la liste.')
        elif user_choice == "2":
            removed = False
            while not removed:
                element_to_remove = input("Entrer le nom d'un élément à supprimer : ")
                if (element_to_remove in list):
                    removed = True
                    list.remove(element_to_remove)
                    print(f'L\'élément {element_to_remove} a bien été supprimé de la liste.')
                else:
                    print(f'L\'élément {element_to_remove} n\'existe pas.')
        elif user_choice == "3":
            if len(list) > 0:
                for i, element in enumerate(list):
                    print(f'{i + 1}: {element}')
            else:
                print('La liste est vide.')
        elif user_choice == "4":
            list.clear()
            print('La liste a été vidée avec succès')
        elif user_choice == "5":
            print('Au revoir !')
            sys.exit()

        is_invalid = True
