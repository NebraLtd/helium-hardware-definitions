import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='hm-hardware-defs',
    version='0.1.6a2',
    author="Nebra Ltd",
    author_email="sales@nebra.com",
    description="Helium Hardware Definitions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NebraLtd/helium-hardware-definitions",
    project_urls={
        "Bug Tracker": "https://github.com/NebraLtd/"
                       "helium-hardware-definitions/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
