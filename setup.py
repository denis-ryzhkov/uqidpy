from distutils.core import setup

setup(
    name='uqid',
    version='0.1.0',
    description='Returns unique id from random chars. Default is 64 chars 0-9a-zA-Z aka base62.',
    long_description='''
Usage::

    pip install uqid
    from uqid import uqid, digits

    print(uqid()) # e7ljCIs4grYZ9tOv6bpX3TQIA7FyA23umzGjDcIjHff2XwF2ziAw56B7S3EdOuCA
    print(uqid(4, digits)) # 4982

''',
    url='https://github.com/denis-ryzhkov/uqidpy',
    author='Denis Ryzhkov',
    author_email='denisr@denisr.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    py_modules=['uqid'],
)
