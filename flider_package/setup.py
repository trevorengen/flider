import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flider",
    version="1.0.0",
    author="Trevor Engen",
    author_email="Trevorengen@gmail.com",
    description="A lightweight flask skeleton builder.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevorengen/flider",
    project_urls={
        "Bug Tracker": "https://github.com/trevorengen/flider/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=['flider', 'save_files'],
    python_requires=">=3.6",
    package_data={
        'flider': ['*'],
        'save_files': ['*.flid'],
    },
)