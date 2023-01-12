from setuptools import setup, find_packages


def readme():
    with open('README.md', encoding="utf-8") as f:
        return f.read()


setup(name='openritardi',
      version='0.1',
      python_requires='>=3.9',
      description='A package to obtain data on trains in Italy',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
      ],
      url='https://github.com/hadriensevel/openritardi',
      author='Open Ritardi Development Team',
      author_email='hadrien.sevel@outlook.com',
      license='MIT',
      packages=find_packages(),
      # install_requires=[
      #     'markdown',
      # ],
      include_package_data=True,
      zip_safe=False)
