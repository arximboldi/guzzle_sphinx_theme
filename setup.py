from setuptools import setup

setup(
    name='sinusoidal_sphinx_theme',
    version='0.7.11',
    description='Sphinx theme used by Sinusoidal Engineering.',
    long_description=open('README.rst').read(),
    author='Juan Pedro Bolivar Puente',
    author_email='raskolnikov@gnu.org',
    url='https://github.com/arximboldi/sinusoidal_sphinx_theme',
    packages=['sinusoidal_sphinx_theme'],
    include_package_data=True,
    install_requires=['Sphinx>=1.2'],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
)
