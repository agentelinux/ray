from setuptools import setup, find_packages


def description():
    return """
    Ray is a framework that helps you to deliver
    well designed software without been stucked in your framework.
    Ray it's a ready to production framework that contains
    a uWSGI server that can be used in production as well.
    """

setup(
    name="ray_appengine",
    version="0.0.1",
    author="Felipe Volpone",
    author_email="felipevolpone@gmail.com",
    description=description(),
    license="MIT",
    keywords="appengine framework ray api rest google",
    url="http://github.com/felipevolpone/ray",
    packages=find_packages(exclude=['tests']),
    long_description="Check on github: http://github.com/felipevolpone/ray",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    entry_points='''
        [console_scripts]
        ray=ray.commandline:interface
    '''
)
