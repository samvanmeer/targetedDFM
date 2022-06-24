from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='targetDFM',
    url='https://github.com/samvanmeer/targetedDFM',
    author='Sam van Meer',
    author_email='samvanmeer@gmail.com',
    # Needed to actually package something
    packages=['targetedDFM'],
    # Needed for dependencies
    #install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='NAN',
    description='Target',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read(),
)
