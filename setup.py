import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjyutping",
    version="1.0.0",
    author="Macro Yau",
    author_email="macroyau.development@gmail.com",
    description="Chinese text to Jyutping conversion library in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MacroYau/PyJyutping",
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={
        "pyjyutping": ["data/jyutping_dictionary.json"]
    },
    entry_points={
        "console_scripts": ["pyjyutping=pyjyutping.jyutping:main"]
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
