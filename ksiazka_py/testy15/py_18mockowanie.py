import random
from unittest.mock import patch

for i in range(3):
    print(random.random())

print()
with patch('random.random') as mock_rand:
    mock_rand.return_value = 0.05
    for i in range(3):
        print(random.random())
print('')

for i in range(3):
    print(random.random())
