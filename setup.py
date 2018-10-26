from distutils.core import setup
import os

def read(fname):
    """Utility function to get README.rst into long_description.

    ``long_description`` is what ends up on the PyPI front page.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'testipbase',
  packages = ['testipbase'], # this must be the same as the name above
  version = '1.0',
  description = 'Python Client for ipbase.co - a Free Ip Geolocation API',
  author = 'theipguy2018',
  author_email = 'theipguy2018@gmail.com',
  url = 'https://github.com/theipguy/testipbase', # use the URL to the github repo
  download_url = 'https://github.com/theipguy/testipbase/archive/1.0.tar.gz', # I'll explain this in a second
  keywords = ['geolocation', 'ip geolocation', 'ip locate', 'geoip','ip country'], # arbitrary keywords
  long_description=read('README'),
  classifiers = [],
)
