from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="1.0",
    author= "chris nevin",
    author_email= "chrisselfInit@gmail.com",
    install_requirements = ["openai","langchain","streamlit","python-dotenv", "PyPDF2"],
    packages= find_packages()
)