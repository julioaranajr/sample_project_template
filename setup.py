from __future__ import annotations

from setuptools import find_packages, setup

setup(
    name="sample",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
