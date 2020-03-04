import click

from clients.services import ClientService
from clients.models import Client


#Con los decoradores convertimos las funciones a comandos de CLICK
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
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """ Updates a client """
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """ Deletes a client """
    pass


all = clients
