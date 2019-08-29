import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

links = []  # for repo urls (dependency_links)
requires = []  # for package names
try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except Exception:
    from pip.req import parse_requirements
    from pip.download import PipSession

requirements = parse_requirements('requirements.txt', session=PipSession())
for item in requirements:
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))  # always the package name

version = "0.0.1"

setuptools.setup(
    name="email-sender",
    version=version,
    author="tonyliu",
    author_email="tonyliu@jiangxing.ai",
    description="A small module for jx to send emails",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=requires
)
