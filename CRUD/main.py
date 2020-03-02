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

def update_client(client_name, update_client_name):
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name)
        add_comma()
        list_clients()
    else:
        print('Client is not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')

def search_client(client_name):
    global clients

    client_list = clients.split(',')
    for client in client_list:
        if client != client_name:
            continue
        else:
            return True



def prints_welcome():
    print('Welcome to Platzi ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Creat user')
    print('[D] Delete user')
    print('[U] Update client')
    print('[S] Search client')

def _get_client_name():
    return input('What is the client name? : ') 

if __name__ == '__main__':
    prints_welcome()

    command = input().upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the new name? : ')
        update_client(client_name, update_client_name)
    elif  command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client list')
        else:
            print('The client {} is not in the client list'.format(client_name))
    else:
        print('Invalid command')