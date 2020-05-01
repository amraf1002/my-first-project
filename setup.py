import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def read_requirements_file(path):
    """
    Read requirements.txt, ignore comments
    """
    requires = list()
    f = open(path, "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[:line.find("#")].strip()
        if line:
            requires.append(line)
    return requires


try:
    REQUIRES = read_requirements_file("requirements.txt")
except Exception as e:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setuptools.setup(
    name='awesome_utility',
    version='0.0.1',
    author="John Doe",
    author_email="john.doe@jmail.com",
    description="Simple package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES
)
