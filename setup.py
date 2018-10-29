from setuptools import setup, find_packages

install_requires = [
    'validators>=0.12.2',
    'tldextract>=2.2.0',
]

setup(
    name="t4c",
    version="0.1",
    packages=find_packages('.',
        exclude=[
            "test",
            "tests.*"
            ".eggs",
            ".tox",
        ]
    ),
    platforms='any',
    install_requires=install_requires,
    build_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)
