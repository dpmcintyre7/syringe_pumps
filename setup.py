import setuptools

with open("pump_control/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pump_control",
    version="1.0.0",
    author="Diana Arguijo",
    author_email="dma25@bu.edu",
    description="Syringe Pump Control Software'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CIDARLAB/syringe_pumps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)