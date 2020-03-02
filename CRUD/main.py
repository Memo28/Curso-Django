import sys
clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@gmail.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Toño',
        'company': 'Amazon',
        'email': 'toño@facebook.com',
        'position': 'Data enginieer'
    }
]


def create_client(client):
    global clients
    if client not in clients:
        clients.append(client_name)
    else:
        print("Client already is in the client's list")


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, name=client['name'], company=client['company'], email=client['email'], position=client['position']))


def update_client(client_name):
    global clients

    user_id = _exist_user(client_name)
    if user_id:
        clients[user_id] = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        list_clients()
    else:
        print('Client is not in clients list')


def delete_client(client_name):
    global clients

    user_id = _exist_user(client_name)
    if user_id:
        clients.pop(user_id)
    else:
        print('Client is not in clients list')


def _exist_user(client_name):
    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            return idx

    return False


def search_client(client_name):
    global clients
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('Whats the client {} ? : '.format(field_name))

    return field


def prints_welcome():
    print('Welcome to Platzi ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C] Creat user')
    print('[D] Delete user')
    print('[U] Update client')
    print('[S] Search client')


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? : ')

        if client_name == 'exit':
            client_name == None
            break

    if not client_name:
        sys.exit()
    return client_name


if __name__ == '__main__':
    prints_welcome()

    command = input().upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        clients.append(client)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client(client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = _exist_user(client_name)
        if found:
            print('The client is in the client list')
        else:
            print('The client {} is not in the client list'.format(client_name))
    else:
        print('Invalid command')
