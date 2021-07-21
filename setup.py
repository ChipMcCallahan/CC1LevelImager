from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='cc1_level_imager',
    url='https://github.com/ChipMcCallahan/CC1LevelImager',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['PIL>=1.1.7'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='GNU General Public License v3.0',
    description='Basic imaging functionality for CC1 levels. Not intended to be full featured.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)