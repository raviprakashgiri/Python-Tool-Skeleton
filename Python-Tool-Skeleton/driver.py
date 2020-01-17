import click
import logging


logging.basicConfig(format='%(asctime)s %(message)s')
logging.getLogger().setLevel(logging.INFO)

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')


def main_fun():
	"""Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    main_fun()