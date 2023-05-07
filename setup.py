from pathlib import Path
from setuptools import setup


with open("README.md", 'r') as readme:
    long_description = readme.read()



setup(
    name="verse",
    version="1.0",
    description="A simple cli tool to get the verse of the day",
    long_description=long_description,
    long_description_content_type="text/makdown",
    url="https://github.com/LordUbuntu/verse",
    keywords=["python", "bible", "verse", "cli"],
    license="MIT",
    author="Jacobus Burger",
    author_email="therealjacoburger@gmail.com",
    packages=["verse"],
    install_requires=["beautifulsoup4==4.11.1", "requests==2.28.2"],
    extras_require={
        "dev": ["pytest>=7.2", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
    platforms=["any"],
    py_modules=["verse"],
    entry_points={
        "consol_scripts": ["verse=verse.verse:main"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Environment :: Console",
    ]
)
