from setuptools import setup, find_packages

from consent_user_information import __version__

setup(
    name="django-consent-user-information",
    version=__version__,
    description="To store information about the user.",
    long_description="""
To store information about the user like the browser and device.
""",
    keywords="django, consent, user-agent, browser, ip",
    author="Brief.me",
    author_email="tech@brief.me",
    url="https://github.com/briefmnews/django-consent-user-information",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=["django-ipware", "django-user-agents"],
    entry_points={
        "console_scripts": [],
    },
)
