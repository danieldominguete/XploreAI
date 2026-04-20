from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name="xploreds",
    version=__version__,
    url="https://github.com/danieldominguete/XploreAI",
    license="MIT License",
    author="Daniel Dominguete",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="daniel.dominguete@gmail.com",
    keywords="Agentic AI",
    description="Easy-to-use package of the most relevant Agentic AI techniques.",
    packages=["xploreds"],
    install_requires=[
        "pandas==2.2.3",
    ],
    python_requires=">=3.10",
)
