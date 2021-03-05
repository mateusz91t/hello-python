import subprocess

result = subprocess.call(['ping', '-n', '5', 'onet.pl'])
print('\nresult', result, '\n')  # jeśli 0 to jest ok, 1 to błąd

# subprocess.Peopen w porównaniu do os.Peopen wykonuje pracę w innym wątku
result2 = subprocess.Popen(['ping', '-n', '4', 'onet.pl'])
print('\nresult', result2, '\n')
print(result2.communicate())
