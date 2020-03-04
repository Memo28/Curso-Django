import click

#Con los decoradores convertimos las funciones a comandos de CLICK
@click.group()
def clients():
    """ Manages the clients lifecycle """
    pass

# Registramos los comandos como parte de clients
@clients.command()
@click.pass_context
def create(context, name, company, email, position):
    """ Create a new client """
    pass


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
