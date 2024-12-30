from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="1.0",
    author= "chris nevin",
    author_email= "chrisselfinit@gmail.com",
    install_requirements = ["openai","bitsandbytes","accelerate","langchain","streamlit","python-dotenv", "PyPDF2", "torch", "lanngchain_community", "transformers"],
    packages= find_packages()
)