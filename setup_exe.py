#! /usr/bin/python
from distutils.core import setup
from glob import glob
import sys
sys.path.append("lib");
import py2exe

# to install type:
# python setup.py install --root=/

setup (name='Adawat Latex', version='1.0',
      description='Adawat Latex Arabic Text Tools',
      author='Taha Zerrouki',
      author_email='taha dot zerrouki at gmail.com',
      url='http://Adawat Latex.sf.net/',
      license='GPL',
     console = [
        {
            "script": "adawat-latex-gui.py",
            "icon_resources": [(1, "resources/images/adawat.ico")]
        }
    ],
     windows = [
        {
            "script": "adawat-latex-gui.py",
            "icon_resources": [(1, "resources/images/adawat.ico")]
        }
    ],

      #scripts=['Adawat Latex'],
      classifiers=[
          'Development Status ::  5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ],
      data_files=[
      ('resources',

      ('resources/fonts',
      [   
        './resources/fonts/AmiriTypewriter-Regular.ttf',
      ]),
      ('resources/images',
      [   
        './resources/images/adawat.ico',
      ]),

  
      ]);

