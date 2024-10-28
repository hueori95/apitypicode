from setuptools import setup, find_packages


setup(name='apitest',
      version='1.0',
      description='API Testing',
      author="huent95",
      author_email='huent995@gmail.com',
      url='http://localhost:3000/',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
            "pytest",
            "PyMySQL==1.1.1",
            "pytest-html==2.1.1",
            "requests",
            "requests-oauthlib"
      ]
      )