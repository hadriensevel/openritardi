from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='openritardi_api',
      version='0.1',
      description='A package to get data from the viaggiatreno API',
      long_description=readme(),
      url='https://github.com/hadriensevel/openritardi_api',
      author='Hadrien Sevel',
      author_email='hadrien.sevel@outlook.com',
      license='MIT',
      packages=find_packages(),
      # install_requires=[
      #     'markdown',
      # ],
      include_package_data=True,
      zip_safe=False)
