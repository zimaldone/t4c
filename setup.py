from setuptools import setup, find_packages

setup(
    name="t4c",
    version="0.1",
    packages=find_packages(
        exclude=[
            ".eggs",
            ".tox",
        ]
    ),
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest-runner",
        "pytest",
        "pytest-cov",
        "pytest-flakes",
        "pytest-testdox",
        "coverage"]
)