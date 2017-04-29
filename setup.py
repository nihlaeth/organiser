"""Installation script for organiser."""
from setuptools import setup, find_packages

setup(
    name='organiser',
    version='1.0',
    description='online organiser',
    author='nihlaeth',
    author_email='info@nihlaeth.nl',
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=[
        'user_config',
        'aiohttp',
        'aiosmtplib>=1.0.1',
        'markupsafe',
        'markdown',
        'aiohttp_session[secure]',
        'Jinja2',
        'aiohttp_jinja2',
        'motor',
        'aiohttp-login',
        'uvloop'],
    entry_points={
        'console_scripts': ['organiser = organiser:start']},
    package_data={'organiser': ['static/*', 'templates/*']},
    )
