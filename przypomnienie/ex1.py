try:
    print(t) # NameError
except NameError:
    print('catch NameError')

try:
    1/0
except ZeroDivisionError:
    print('catch ZeroDivisionError')

try:
    'a' + 2
except TypeError:
    print('catch TypeError')

####
try:
    1%'a'
except TypeError as te:
    print('te: %r' % te)

try:
    1/ 'a'
except (TypeError, NameError) as err:
    print('errors: %r' % err)
    # raise

try:
    raise EOFError("i'm eofError")
except EOFError as er:
    print(er)

try:
    raise KeyboardInterrupt
finally:
    print('kbi')



