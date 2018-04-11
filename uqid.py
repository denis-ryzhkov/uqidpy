"""
uqid.py version 0.3.0
https://github.com/denis-ryzhkov/uqidpy

Copyright (C) 2015-2018 by Denis Ryzhkov <denisr@denisr.com>
MIT License, see http://opensource.org/licenses/MIT
"""

### import

from datetime import datetime
from random import choice

try:
    xrange
except NameError:
    xrange = range

### chars

digits = '0123456789'
base62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

### uqid

def uqid(length=64, chars=base62):
    return ''.join(choice(chars) for i in xrange(length))

### dtid

_dt_format = '%Y%m%d%H%M%S%f'
_dt_length = 20

def dtid(length=24, chars=base62):
    s = datetime.utcnow().strftime(_dt_format)
    if length > _dt_length:
        return s + uqid(length - _dt_length, chars)
    return s[:length]

### datetime_from_dtid

def datetime_from_dtid(s):
    return datetime.strptime(s[:_dt_length], _dt_format)

### tests

def tests():

    ### import

    from time import time
    from uuid import uuid4

    try:
        from bson import ObjectId
    except ImportError:
        ObjectId = None

    ### samples

    print('\nSAMPLES:')
    length = 24

    print('str(uuid4()): {}'.format(uuid4()))
    print('len(^): {}'.format(len(str(uuid4()))))
    print('len(v): {}'.format(length))

    if ObjectId:
        print('str(ObjectId()): {}'.format(str(ObjectId())))

    print('uqid({}): {}'.format(length, uqid(length)))
    print('dtid({}): {}'.format(length, dtid(length)))

    assert len(uqid(length)) == length
    assert len(dtid(length)) == length
    assert (datetime.utcnow() - datetime_from_dtid(dtid())).total_seconds() < 0.1

    N = 1000*1000
    print('Iterations: {}'.format(N))

    ### seconds

    print('\nSECONDS:')

    start = time()
    for _ in xrange(N):
        str(uuid4())
    print('str(uuid4()) seconds: {:.6f}'.format(time() - start))

    if ObjectId:
        start = time()
        for _ in xrange(N):
            str(ObjectId())
        print('str(ObjectId()) seconds: {:.6f}'.format(time() - start))

    start = time()
    for _ in xrange(N):
        uqid(length)
    print('uqid({}) seconds: {:.6f}'.format(length, time() - start))

    start = time()
    for _ in xrange(N):
        dtid(length)
    print('dtid({}) seconds: {:.6f}'.format(length, time() - start))

    ### duplicates

    print('\nDUPLICATES:')

    U = len(set(str(uuid4()) for _ in xrange(N)))
    print('str(uuid4()) duplicates: {}'.format(N - U))

    if ObjectId:
        U = len(set(str(ObjectId()) for _ in xrange(N)))
        print('str(ObjectId()) duplicates: {}'.format(N - U))

    U = len(set(uqid(length) for _ in xrange(N)))
    print('uqid({}) duplicates: {}'.format(length, N - U))

    U = len(set(dtid(length) for _ in xrange(N)))
    print('dtid({}) duplicates: {}'.format(length, N - U))

if __name__ == '__main__':
    tests()
