from setuptools import setup, find_packages

setup(
    name="councillm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ollama",
        "httpx",
        "textual",
        "duckduckgo-search",
    ],
    entry_points={
        "console_scripts": [
            "councillm=councillm.cli:main",
        ]
    },
)
