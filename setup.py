
#!/usr/bin/env python

"""The setup script."""
import os

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()


setup_requires = ["pipenv", "pipfile"]


def list_requirements(category="default"):
    try:
        import pipfile
    except ModuleNotFoundError:
        os.system(f"pip install {' '.join(setup_requires)}")
        import pipfile

    pf = pipfile.load("Pipfile")

    requirements = []
    for k, v in pf.data[category].items():
        version = v if not isinstance(v, dict) else v.get("version")
        requirements.append(f"{k}{version}")
    return requirements


setup(
    name="my_lib",
    author="Pedro",
    author_email="pepito@gmail.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    description="My personal project!",
    install_requires=list_requirements(),
    long_description=readme,
    include_package_data=True,
    packages=find_packages(include=["app", "app.*"]),
    setup_requires=setup_requires,
    url="https://github.com/pedro",
    version="1.0.0",
    zip_safe=False,
)