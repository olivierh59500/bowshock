from setuptools import setup, find_packages
import os

setup(
    name='bowshock',
    version='0.0.1',
    author='Emir Ozer',
    author_email='emirozer@yandex.com',
    url='https://github.com/emirozer/bowshock',
    description='An all-in-one library for NASA Api\'s',
    long_description=os.path.join(os.path.dirname(__file__), 'README.md'),
    packages=find_packages(exclude=[]),
    install_requires=[
        'fake-factory>=0.4.2',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
