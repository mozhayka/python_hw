import sys


def nl(file):
    f = open(file, 'r') if file else sys.stdin
    for num, line in enumerate(f, 1):
        print(f"{num}\t{line}", end='')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        nl(sys.argv[1])
    else:
        nl(None)
