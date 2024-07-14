import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

requirements = ['selenium==4.1.0',
                'webdriver-manager==3.2.2',
                'selenium-wire==5.1.0',
                'python-dateutil==2.8.2']


setuptools.setup(
    name="facebook_page_scraper",
    version="5.0.6",
    author="Sajid Shaikh",
    author_email="shaikhsajid3732@gmail.com",
    description="Python package to scrap facebook's pages front end with no limitations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/shaikhsajid1111/facebook_page_scraper",
    keywords="web-scraping selenium facebook facebook-pages",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP"

    ],
    python_requires=">=3.7",
    install_requires=requirements
)
