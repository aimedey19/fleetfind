from setuptools import setup, find_packages

setup(
    name='fleetfind',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'django>=2.2',
        # Add other dependencies as needed
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            # If your package includes command-line scripts, add them here
        ],
    },
    author='Aimé An-Nyong DEGBEY',
    author_email='annyongdey19@gmail.com',
    description='A Django package for searching across multiple models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://da-kodesio.github.io/fleetfind',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        # Add other classifiers as needed
    ],
    keywords='django search multi-model',
    project_urls={
        'Source': 'https://github.com/yourusername/fleetfind',
    },
)
