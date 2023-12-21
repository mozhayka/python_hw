import click


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
def wc(files):
    if len(files) == 0:
        text = click.get_text_stream('stdin').readlines()
        print(text)

        lines_cnt = 0
        words_cnt = 0
        chars_cnt = 0

        for line in text:
            lines_cnt += 1
            words_cnt += len(line.split())
            chars_cnt += len(line) - 1  # считаем лишний символ конца строки

        click.echo(f"{lines_cnt}\t{words_cnt}\t{chars_cnt}")
        return

    total_lines = 0
    total_words = 0
    total_chars = 0
    for file in files:
        text = file.read().splitlines()

        lines_cnt = 0
        words_cnt = 0
        chars_cnt = 0

        for line in text:
            lines_cnt += 1
            words_cnt += len(line.split())
            chars_cnt += len(line)

        click.echo(f"{lines_cnt}\t{words_cnt}\t{chars_cnt}\t{file.name}")
        total_lines += lines_cnt
        total_words += words_cnt
        total_chars += chars_cnt

    if len(files) > 1:
        click.echo(f"{total_lines}\t{total_words}\t{total_chars}\ttotal")


if __name__ == '__main__':
    wc()
