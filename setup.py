import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()
    
    
__version__ = "0.0.1"
REPOSITORY_NAME = "textSummaizer"
AUTHOR_USER_NAME = "Arshp-svg"
SRC_REPOSITORY = "github.com/{AUTHOR_USER_NAME}/{REPOSITORY_NAME}.git"
AUTHOR_EMAIL = "arshpatel213@gmail.com"


setuptools.setup(
    name=REPOSITORY_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization project using advanced NLP techniques.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://{SRC_REPOSITORY}",
    project_urls={
        "Bug Tracker": f"https://{SRC_REPOSITORY}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)