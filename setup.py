from setuptools import setup, find_packages

setup(
    name="fenix",
    version="0.1.0",
    author="Azeem Teli",
    author_email="tinprogrammers@gmail.com",
    description="A blazing fast and minimal Python full-stack web framework",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tinprogrammers/fenix",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Future dependencies (empty for now)
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FeniX",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
