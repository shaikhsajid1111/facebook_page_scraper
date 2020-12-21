import setuptools

with open("README.md","r") as file:
    long_description = file.read()

setuptools.setup(
    name = "facebook_page_scraper",
    version = "0.1.0",
    author = "Shaikh Sajid",
    author_email = "shaikhsajid3732@gmail.com",
    description = "Python package to scrap posts of public pages on facebook",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/shaikhsajid1111/facebook_pages_scraper/",
    keywords = "web-scraping selenium facebook facebook-pages",
    packages = setuptools.find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X", 
       

    ],
    python_requires = ">=3.6.9",
    install_requires=[
        'bs4==0.0.1',
        'requests==2.22.0',
        'fake-headers==1.0.2'
    ])
