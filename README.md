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
* dtid(24) is 2x faster than uqid(24) but 2x slower than str(ObjectId()).

tests
-----

    python uqid.py

    Length: 24
    uqid(24): SdGksfuUJAmDGz7suDzgJYr4
    dtid(24): 20160923092803852711Pqci
    str(ObjectId()): 57e4f5a39c5915591b593563
    Iterations: 1000000
    uqid(24) seconds: 11.457604
    dtid(24) seconds: 5.997643
    str(ObjectId()) seconds: 2.715093
    uqid(24) duplicates: 0
    dtid(24) duplicates: 0
    str(ObjectId()) duplicates: 0

uqid.py version 0.2.0  
Copyright (C) 2015-2015 by Denis Ryzhkov <denisr@denisr.com>  
MIT License, see http://opensource.org/licenses/MIT
