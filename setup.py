from setuptools import setup, find_packages

setup(
    name="notiadb",
    packages = find_packages(),
    include_package_data=True,
    version="0.4",
    author="Kyshi",
    author_email="kyshi58@outlook.com",
    description="A basic database system for Python.",
    url="https://github.com/kyshi/NotiaDB",
    keywords='database',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)