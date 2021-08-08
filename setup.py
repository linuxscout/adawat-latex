#! /usr/bin/python
from distutils.core import setup
from glob import glob

# to install type:
# python setup.py install --root=/

setup (name='Adawat-latex', version='1.0',
      description='Adawat Latex: tools for Latex',
      author='Taha Zerrouki',
      author_email='taha(dot) zerrouki (at) gmail.com',
      url='http://github.com/linuxscout/adawat-latex/',
      license='GPL',
      #platform="OS independent",
      package_dir={'adawat-latex': 'adawat-latex',},
      packages=['adawat-latex'],
      # include_package_data=True,
      package_data = {
        'adawat-latex': ['doc/*.*','doc/html/*'],
        'resources': ['resources/*.*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ],
    );
