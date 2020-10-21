import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twinkly-client",
    version="0.0.1",
    author="dr1rrb",
    author_email="py-twinkly-client@torick.net",
    description="A package to communicate with Twinkly LED strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dr1rrb/py-twinkly-client",
    packages=setuptools.find_packages(),
    install_requires=[
        "aiohttp",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Topic :: Home Automation',
    ],
    python_requires='>=3.6',
)