from setuptools import setup, find_packages

setup(
    name = "asd",
    desciption = "Various command line helper scripts`",
    version = "1.0.0",
    author = 'Lajos Santa',
    author_email = 'santa.lajos@coldline.hu',
    install_requires = [
        "argcomplete==1.0.0",
    ],
    scripts = [
        'bin/asd',
    ],
    include_package_data = True,
    packages = find_packages(),
)