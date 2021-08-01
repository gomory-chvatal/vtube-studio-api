import setuptools

setuptools.setup(
    name='vtsapi',
    version='0.1.0a1',
    description='Library for working with the VTube Studio API.',
    author='Gomory Chvatal',
    author_email='gomory.chvatal@gmail.com',
    url='https://github.com/gomory-chvatal/vtube-studio-api',
    packages=setuptools.find_packages(exclude=['*tests']),
    package_data={'vtsapi': ['*.png']},
    install_requires=['websockets'],
    python_requires='>=3.9',
    zip_safe=False
)
