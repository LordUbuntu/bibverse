from setuptools import setup


with open("README.md", 'r') as readme:
    long_description = readme.read()



setup(
    name="bibverse",
    version="1.3",
    description="A simple cli tool to get the bible verse of the day",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LordUbuntu/bibverse",
    keywords=["python", "bible", "cli"],
    license="MIT",
    author="Jacobus Burger",
    author_email="therealjacoburger@gmail.com",
    packages=["bibverse"],
    install_requires=[
        "beautifulsoup4==4.12.2", "bs4==0.0.1", "requests==2.30.0"
    ],
    extras_require={
        "dev": ["pytest>=7.2", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
    platforms=["any"],
    py_modules=["bibverse"],
    entry_points={
        "console_scripts": ["bibverse=bibverse.__main__:main"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
    ]
)
