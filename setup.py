import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setuptools.setup(
    name="neo4j-big-bang-euonymus", # Replace with your own username
    version="0.0.1",
    author="euonymus",
    author_email="euonymus0220@gmail.com",
    description="This is a library allow you to import csv data into neo4j database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/euonymus/neo4j-big-bang",
    packages=setuptools.find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "big-bang-node=neo4j_big_bang.import_nodes:main",
            "big-bang-rel=neo4j_big_bang.import_relationships:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
