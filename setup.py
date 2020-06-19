import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-jakoblj", # Replace with your own username
    version="0.0.1",
    author="Jakob LJ",
    author_email="post@jakoblj.com",
    description="A template generator for fastapi subapps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakob-lj/fastapi-subapp-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)