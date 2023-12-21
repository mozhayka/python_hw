import click
import sys


@click.command()
@click.argument('file', type=click.File('r'), default=sys.stdin)
def nl(file):
    for num, line in enumerate(file, 1):
        click.echo(f"{num}\t{line}", nl=False)


if __name__ == '__main__':
    nl()
