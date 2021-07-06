import time


def useful_function():
    print(__name__)
    for i in range(5):
        print(f"I swear I'm useful {i}")
        time.sleep(1)


# useful_function()

if __name__ == '__main__':
    useful_function()

# out:
# __main__
# I swear I'm useful 0
# I swear I'm useful 1
# I swear I'm useful 2
# I swear I'm useful 3
# I swear I'm useful 4


