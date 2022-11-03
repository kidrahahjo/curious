print('Import time', locals())


VAR_GLOBAL = 1


def x():
    print('Begin X', locals())
    VAR_X = 1
    def y():
        pass
    print('End X', locals())


def z():
    try:
        y = VAR_GLOBAL
        VAR_GLOBAL = 1
    except UnboundLocalError as err:
        print("ERROR: ", repr(err))


def w():
    global VAR_GLOBAL
    print('Begin W', locals())
    del VAR_GLOBAL
    print('End W', locals())


if __name__ == '__main__':
    print('Begin Exec', locals())
    x()
    z()
    w()
    print('End Exec', locals())

# Resource: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
