from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='mecab_functions',
    version='1.0.0',
    license='ライセンス',
    description='Mecabを使ったfunction',
    author='jarunga',
    url='https://github.com/Jarunga/mecab_functions.git',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/**/*.py',recursive=True)],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov']
)
