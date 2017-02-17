# coding: utf-8

from www import orm
from www.models import User, Blog, Comment
import asyncio
import logging;logging.basicConfig(level=logging.INFO)

async def test():
    await orm.create_pool(loop=loop, user='web', password='web', db='blog')
    users = await User.findAll(orderBy='created_at')
    for user in users:
        logging.info('name: %s, password: %s, created_at: %s' % (user.name, user.passwd, user.created_at))
    u = User(name='Test1', email='test11@example.com', passwd='1234567800', image='about:blank')
    await u.save()
    u = User(name='Test2', email='test22@example.com', passwd='2345678900', image='about:blank')
    await u.save()
    u = User(name='Test3', email='test33@example.com', passwd='3456789000', image='about:blank')
    await u.save()
    logging.info('test ok.')
    await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()

