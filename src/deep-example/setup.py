from setuptools import setup

setup(name="deep",version="0.1",
    description="Example package",
    author="Sjoerd Gnodde",url="https://intodeep.ai",
    license='MIT',author_email="sgnodde@hhdelfland.nl",install_requires=['numpy', 'pandas'],tests_require=['matplotlib'],
    long_description=open('README.md').read()
)
