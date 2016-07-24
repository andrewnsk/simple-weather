from setuptools import setup

setup(name='simple-weather',
      version='0.0.1',
      description='pyowm wrapper',
      url='http://github.com/andrewnsk/simple-weather/',
      author='Smartgo',
      author_email='andrewnorilsk@gmail.com',
      license='GNU v3',
      packages=['simple-weather'],
      install_requires=[
          'pyowm',
          'mako'
      ],
      zip_safe=False)