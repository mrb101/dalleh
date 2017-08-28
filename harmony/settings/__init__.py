import os


ENV = os.environ['ENV']

if ENV == 'DEV':
    try:
        from .dev import *
    except ImportError:
        raise ImportError('Dev settings does not exists!')
elif ENV == 'TEST':
    try:
        from .test import *
    except ImportError:
        raise ImportError('Test settings does not exists!')
elif ENV == 'PROD':
    try:
        from .prod import *
    except ImportError:
        raise ImportError('Prod settings does not exists!')
else:
    print('Set the ENV in your environment variables')
