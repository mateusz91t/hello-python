import os

folder_wyjsciowy = 'D:/Mateusz/zdjecia'

for p in os.walk(folder_wyjsciowy):
    print(p)

print('\n\n\n')

# False to iteracja od tyłu
for pliki in os.walk(folder_wyjsciowy, False):
    print(pliki[0])
    print('\t', pliki[1])
    print('\t\t', pliki[2])

print('\n\n\n')

for folder, podfoldery, pliki in os.walk(folder_wyjsciowy):
    print('FOLDER:', folder)
    if podfoldery:
        print('\tPODFOLDERY:')
        for podfolder in podfoldery:
            print('\t\t', podfolder)
    if pliki:
        print('\tPLIKI:')
        for plik in pliki:
            # print('\t\t', plik)
            print('\t\t', plik, '\t',
                  os.path.getsize(folder.replace('\\','/') + '/' + plik),
                  'bajtów')

print('\n\n\n')

print(os.getcwd())
os.chdir(folder_wyjsciowy)
print(os.getcwd())
print(os.listdir())
print(os.path.exists(folder_wyjsciowy))
print(os.path.exists(folder_wyjsciowy + 'asd'))
print(os.path.isdir(folder_wyjsciowy))
print(os.path.isfile(folder_wyjsciowy))
print(os.path.getsize('D:/Mateusz/zdjecia/inne/zakupy/ram/r1.jpg'), 'bajtów')

print('\n\n\n')

print(os.path)
print(os.name)
print(os.cpu_count())
print(os.defpath)
print(os.environ)
print(os.getlogin())
print(os.pipe())
print(os.getcwd())
print(os.getpid())
print(os.sep)

print('\n\n\n')

print(os.getcwd())
print(os.listdir())
os.mkdir('helloPy')
print(os.listdir())
os.rmdir('helloPy')
print(os.listdir())
