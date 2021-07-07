import time


# it can't be Ctrl+C stopped
# while True:
#     try:
#         print('Weeee! You cannot stop me')
#         time.sleep(.5)
#         # raise Exception('woah')  # even I raise Exception, a program doesn't stop
#     except:
#         print('Oww... Whatever imma keep running')


# it can be Ctrl+C stooped
while True:
    try:
        print('Weeee! You cannot stop me')
        time.sleep(.5)
    except Exception:
        print('Oww... Whatever imma keep running')
