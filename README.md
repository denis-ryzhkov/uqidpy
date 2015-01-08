uqid.py
=======

Returns unique id from random chars.  
Default is 64 chars 0-9a-zA-Z aka base62.

Usage:

    pip install uqid
    from uqid import uqid, digits

    print(uqid()) # e7ljCIs4grYZ9tOv6bpX3TQIA7FyA23umzGjDcIjHff2XwF2ziAw56B7S3EdOuCA
    print(uqid(4, digits)) # 4982

uqid.py version 0.1.0  
Copyright (C) 2015 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
