"""Setup Script """
from setuptools import setup, find_packages
import sys
sys.path.append('./tests')

__author__ = 'KAWASAKI Yasukazu (yakawa)'
__email__ = 'kawasaki@dev.kawa1128.jp'
__version__ = '0.0.1.0'

setup(
  name='PyBufCrex',
  version=__version__,
  description='BUFR/CREX read module',
  author=__author__,
  author_email=__email__,
  long_description=open('README.md').read(),
  license='MIT',
  keywords=['BUFR', 'CREX', 'WMO', 'Parser'],
  url='https://github.com/yakawa/PyBufrCrex',
  install_requires=[
  ],
  tests_require=[
  ],
  package_dir={'': 'src'},
  packages=find_packages('src'),
  include_package_data=True,
  test_suite='testPyBufrCrex.suite',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Scientific/Engineering :: Atmospheric Science'
  ],
)
