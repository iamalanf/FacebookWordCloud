from setuptools import setup

# Not yet registered TODO:
with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='facebookWordCloud',
   version='1.0',
   description='Create wordclouds from facebook messanger downloads',
   author='DoomedBunny',
   packages=['facebookWordCloud'],
   install_requires=[
       'sys', 'getopt', 'wordcloud',
       'matplotlib', 'json', 'pandas'
       ], 
)