from distutils.core import setup

setup(
    name='Python-Tool-Skeleton',
    version='0.1.0',
    author='Ravi Prakash Giri',
    author_email='fullname@gmail.com',
    packages=['Python-Tool-Skeleton', 'Python-Tool-Skeleton.test'],
    #scripts=['bin/my_script1.py','bin/my_script2.py'],
    url='https://github.com/raviprakashgiri/Python-Tool-Skeleton',
    license='LICENSE.txt',
    description='A simple python tool development skeleton.',
    long_description=open('README.txt').read(),
    #install_requires=[ use pipreqs and get the dependencies
    #   "Django >= 1.1.1",
    #   "caldav == 0.1.4",
    #],
)
