def createUser():

    users_list = []

    create_user_input = input("What is your name?: ")
    id_input = input("What is your id?: ")
    

    users_list.append(({"id": id_input, "name": create_user_input}))
    
    return users_list
