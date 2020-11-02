from setuptools import setup, find_packages

setup(
    name="soccergen",
    version="0.1",
    packages=find_packages(),
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["gfootball>=2.28.0",],
    # metadata to display on PyPI
    author="Peter Xenopoulos",
    author_email="xenopoulos@nyu.edu",
    description="Soccer trajectory and event data generation",
    keywords="soccer data-generation foootball",
    url="https://github.com/pnxenopoulos/soccer-data-gen",  # project home page, if any
    project_urls={
        "Issues": "https://github.com/pnxenopoulos/soccer-data-gen/issues",
        "Documentation": "https://github.com/pnxenopoulos/soccer-data-gen/csgo/",
        "Github": "https://github.com/pnxenopoulos/soccer-data-gen/csgo/",
    },
    classifiers=["License :: OSI Approved :: MIT License"],
)
