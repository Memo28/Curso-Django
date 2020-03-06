import click

from clients.services import ClientService
from clients.models import Client


# Con los decoradores convertimos las funciones a comandos de CLICK
@click.group()
def clients():
    """ Manages the clients lifecycle """
    pass

# Registramos los comandos como parte de clients
@clients.command()
# Da informacion al usuario del dato que debe introducir
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='Client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='Client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='Client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='Client position')
@click.pass_context
def create(context, name, company, email, position):
    """ Create a new client """
    client = Client(name, company, email, position)
    client_service = ClientService(context.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """ List all clients """
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    click.echo(' ID  | Name  | Company  | Email  | Position')
    click.echo('*' * 100)

    for client in client_list:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=client['uid'], name=client['name'], company=client['company'], email=client['email'], position=client['position']))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """ Updates a client """
    client_service = ClientService(ctx.obj['clients_table'])

    # Obtenemos la lista de los cliente y verificamos si existe en la lista
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_uid]


    if client:
        client = _update_client_flow(Client(**client[0]))
        print(client)
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """ Deletes a client """
    pass


all = clients
