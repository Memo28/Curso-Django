import click
from clients import command as clients_commands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

#Registramos los comandos
cli.add_command(clients_commands.all)
