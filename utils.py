import os


def move_cifar():
    """
    Move cifar-10 data from 'Descargas' to keras datasets default folder.
    """
    if not os.path.exists('~/.keras/datasets/'):
        os.makedirs('~/.keras/datasets/')

    os.rename('~/Decargas/cifar-10-python.tar.gz',
              '~/.keras/datasets/cifar-10-batches-py.tar.gz')
