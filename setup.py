from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="badwords",
    version="1.1.0",
    author="FlacSy",
    author_email="flacsy.x@gmail.com",
    description="This library is needed to check text for bad words in different languages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlacSy/badwords",
    packages=find_packages(),
    install_requires=[
        'easyocr',
                      ],
    package_data={'bad_words': ['resource/*','resource/*/*']}, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
