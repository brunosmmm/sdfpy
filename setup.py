"""Setup."""

from setuptools import setup, find_packages

setup(
    name="sdfpy",
    version="0.1",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=["networkx>=2.4", "PyYAML>=5.3.1"],
    author="PLACEHOLDER",
    author_email="PLACEHOLDER",
    description="SDFpy: Synchronous Dataflow Graphs in python",
    scripts=[],
)
