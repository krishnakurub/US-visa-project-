from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="krishna"
    author_email="mohankrishna910@gmail.com",
    packages=find_packages())  ### it look for constructor in evry folder (ie folders inside us_visa so tat we directly do" from us_visa import  some thing",,,us _visa becomes local pakcage)