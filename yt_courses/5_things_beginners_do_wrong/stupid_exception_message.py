import traceback


try:
    raise Exception('bad exception with stupid message')
except Exception as e:
    # the worst method
    print('This is what printing the exception is like')
    print(e)

    print()

    # the best method
    print('This is what traceback.print_exc() is like')
    traceback.print_exc()

    print()

    # good method
    print('This is what printing traceback.format_exc() is like')
    mess = traceback.format_exc()
    print(type(mess), mess)
