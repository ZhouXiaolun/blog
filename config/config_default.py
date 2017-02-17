# coding: utf-8

"""Default configurations"""

config = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'web',
        'password': 'web',
        'db': 'blog'
    },
    'session': {
        'secret': 'myblog'
    }
}
