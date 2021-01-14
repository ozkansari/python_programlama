def listing(module, verbose=True):

    if verbose:
        print('name:', module.__name__, 'file:', module.__file__)

    count = 0
    for attr in module.__dict__:
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(module.__name__, 'has %d names' % count)

if __name__ == '__main__':
    mydir = __import__("12_3_metaprogram")
    listing(mydir)
