import click


@click.command()
@click.option('-i')
def witacz(i):
    # print('witaj %r' % i)  # niestety i przekazuje w apostrofach ;/ jak pozbyć się?
    print(f'witaj {i}')


@click.command()
@click.option('-imie', prompt=True)
def witacz2(imie):
    print('cześć {}'.format(imie))


@click.command()
@click.option('-imie', required=True)
def witacz3(imie):
    print(f'yo {imie}')


@click.command()
@click.option('-imie')
@click.option('-nazw')
def witacz4(imie, nazw):
    print(f'cześć {imie} {nazw}')


@click.command()
@click.option('-i', help='imie witanej osoby')
@click.option('-n', help='nazwisko witanej osoby')
def witacz5(i=str, n=str):
    print(f'cześć {i} {n}')


@click.command()
@click.option('--password', prompt=True, confirmation_prompt=True, hide_input=True)
def connect_to_database(password):
    print(f'connecting to database. URL: user/{password}@localhost/databaseName')
