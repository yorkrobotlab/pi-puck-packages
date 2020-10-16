import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi-puck",
    version="1.0.0",
    author="Russell Joyce",
    author_email="russell.joyce@york.ac.uk",
    description="Pi-puck robot Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yorkrobotlab/pi-puck",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.5',
)
