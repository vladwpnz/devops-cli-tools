import click

@click.group(help="Набір невеликих CLI-команд на Click.")
def cli():
    pass

@cli.command(help="Виводить ім'я, якщо воно не починається з p/P.")
@click.option("--name", "-n", required=True, help="Ім'я користувача")
def say(name: str):
    if name and name[0].lower() == "p":
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)

if __name__ == "__main__":
    cli()
