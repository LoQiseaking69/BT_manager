from setuptools import setup, find_packages

# Improved handling of README file for long description
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='bluetooth_manager',
    version='0.1.0',
    packages=find_packages(),
    description='A package to manage Bluetooth devices using bluetoothctl',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ant O, Greene',
    author_email='anthonygreene2007@gmail.com',
    url='https://github.com/LoQiseaking69/BT_manager',
    install_requires=[
        'PyYAML',  # Assuming PyYAML is a dependency for reading config files
        'subprocess32;python_version<"3.5"',  # For subprocess compatibility in Python < 3.5
    ],
    python_requires='>=3.6',
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)