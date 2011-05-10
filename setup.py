from setuptools import setup

setup(
    name='armstrong.core.arm_profiles',
    version='0.1',
    description='Provides the user profiles',
    author='Bay Citizen & Texas Tribune',
    author_email='info@armstrongcms.org',
    url='http://github.com/armstrongcms/armstrong.core.arm_profiles/',
    packages=[
        'armstrong',
        'armstrong.core',
        'armstrong.core.arm_profiles',
    ],

    install_requires=[
        'distribute',
        'idios',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
