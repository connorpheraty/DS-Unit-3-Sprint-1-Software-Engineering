""" Lambda OOP DS Sprint Challenge
"""

import setuptools
REQUIRED = [
  "numpy",
  "pandas"
]

with open("README.md", "r") as fh:
  LONG_DESCRIPTION = fh.read()

  setuptools.setup(
    name="sprint_challenge_packages",
    version='0.0.1',
    author='connorpheraty',
    description='Lambda OOP DS Sprint Challenge',
    long_description=LONG_DESCRIPTION,
    long_Description_content_type="text/markdown",
    url="https://github.com/connorpheraty/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/sprint_challenge",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
  )