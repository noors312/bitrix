from setuptools import setup

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Framework :: Django",
    "Framework :: Django :: 1.11",
    "Framework :: Django :: 2.0",
    "Intended Audience :: Developers",
    # "License :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
]

setup(
    name="bitrix",
    version='0.0.3',
    author="Noors Ergesh",
    author_email="jackmovies01@gmail.com",
    description="Bitrix24 python library",
    license='MIT',
    # long_description=LONG_DESCRIPTION,
    url="https://github.com/NursErgesh/bitrix.git",
    packages=("bitrix",),
    include_package_data=True,
    install_requires=open('requirements/requirements.txt').read().splitlines(),
    tests_require=open('requirements/test.txt').read().splitlines(),
    classifiers=CLASSIFIERS,
    zip_safe=False,
)
