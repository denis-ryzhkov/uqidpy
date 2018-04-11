uqid.py
=======

uqid
----

    pip install uqid
    from uqid import uqid, digits

    print(uqid()) # e7ljCIs4grYZ9tOv6bpX3TQIA7FyA23umzGjDcIjHff2XwF2ziAw56B7S3EdOuCA
    print(uqid(4, digits)) # 4982

* Returns unique id from random chars.
* Default is 64 chars 0-9a-zA-Z aka base62.

dtid
----

    pip install uqid
    from uqid import dtid
    print(dtid())

    YYYYMMDDhhmmssmicrosrnd4
    20161231235959123456uN1q

* 24 bytes by default - as str(ObjectId()).
* But human-friendly - unlike ObjectId.
* Microsecond-precise UTC timestamp - unlike second-precise ObjectId().
* May extract datetime_from_dtid().
* May be used as a log timestamp as is.
* Alphabetically ordered.
* Safe chars 0-9a-zA-Z - unlike binary ObjectId() leading to "ValueError: Invalid UTF-8 sequence length" if added to JSON without str().
* base62^4 is over 14M uniques per microsecond.
* dtid(24) is 2x faster than uqid(24) but slower than str(ObjectId())

tests
-----

    python2 uqid.py
    python3 uqid.py

    SAMPLES:
    str(uuid4()): 3bb25137-2422-4d06-bd12-5a9de2ea2bf6
    len(^): 36
    len(v): 24
    str(ObjectId()): 5acdcd1f9c591516ae800615
    uqid(24): UFRFQVCtYu6rtQq8LD33XjI3
    dtid(24): 20180411085351268116tHse
    Iterations: 1000000

    python2 SECONDS:
    str(uuid4()) seconds: 11.825964
    str(ObjectId()) seconds: 2.424702
    uqid(24) seconds: 9.701306
    dtid(24) seconds: 5.357983

    python3 SECONDS:
    str(uuid4()) seconds: 5.826098
    str(ObjectId()) seconds: 3.192565
    uqid(24) seconds: 17.769653
    dtid(24) seconds: 9.588677

    DUPLICATES:
    str(uuid4()) duplicates: 0
    str(ObjectId()) duplicates: 0
    uqid(24) duplicates: 0
    dtid(24) duplicates: 0


uqid.py version 0.3.0  
Copyright (C) 2015-2018 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
