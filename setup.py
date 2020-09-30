import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE/"README.md").read_text()

setuptools.setup(
    name="apis-scraper",
    version="1.0.1",
    description="Python web scraper for getting Polish political parties support percentage",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/TheLastGimbus/APiS-Scraper',
    author='TheLastGimbus',
    author_email='mateusz.soszynski@tuta.io',
    license='Apache',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: Polish',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Topic :: Religion',
        'Topic :: Office/Business :: News/Diary'
    ],
    install_requires=(HERE/'requirements.txt').read_text().split('\n')
)
