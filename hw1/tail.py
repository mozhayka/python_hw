import click


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
def tail(files):
    if not files:
        lines = click.get_text_stream('stdin').readlines()
        last_lines = lines[-17:] if len(lines) > 17 else lines
        click.echo(''.join(last_lines), nl=False)
    else:
        for file in files:
            click.echo(f'==> {file.name} <==')
            lines = file.readlines()
            last_lines = lines[-10:] if len(lines) > 10 else lines
            click.echo(''.join(last_lines), nl=False)
            click.echo()


if __name__ == '__main__':
    tail()
