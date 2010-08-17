from setuptools import setup, find_packages

setup(
        name='happyforms',
        version='0.0.1',
        description='Automatically strip spaces from Django Forms.',
        long_description=open('README.rst').read(),
        author='Dave Dash',
        author_email='dd+pypi@davedash.com',
        url='http://github.com/mozilla/happyforms',
        license='BSD',
        packages=find_packages(),
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )


