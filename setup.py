from setuptools import setup


with open("README.md") as f:
    readme = f.read()

setup(
    name="vpype-dxf",
    version="0.1.0",
    description="vpype dxf plugin",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tatarize",
    author_email="tatarize@gmail.com",
    url="https://github.com/tatarize/vpype-dxf/",
    packages=["vpype_dxf"],
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
    install_requires=[
        "click",
        "vpype>=1.9,<2.0",
        "numpy",
        "ezdxf>=0.14.0",
        "svgelements>=1.4.0"
    ],
    entry_points="""
            [vpype.plugins]
            dread=vpype_dxf.dread:dread
        """,
)