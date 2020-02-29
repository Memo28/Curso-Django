clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        add_comma()
    else:
        print("Client already is in the client's list")

def list_clients():
    global clients
    print(clients)

def add_comma():
    global clients
    clients += ','

def prints_welcome():
    print('Welcome to Platzi ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Creat user')
    print('[D] Delete user')

if __name__ == '__main__':
    prints_welcome()

    command = input()

    if command == 'C':
        client_name = input('What is the client name? : ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')