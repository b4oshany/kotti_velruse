import os, re
from setuptools import setup, find_packages

name = 'kotti_velruse'

here = os.path.abspath(os.path.dirname(__file__))
init_file = os.path.join(here, name, '__init__.py')
version_re = "\s*__version__\s*=\s*((\"([^\"]|\\\\\")*\"|'([^']|\\\\')*'))"
version = re.search(version_re, open(init_file).read()).groups()[0][1:-1]

README  = open(os.path.join(here, 'README')).read()
AUTHORS = open(os.path.join(here, 'AUTHORS')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

long_description = (
    README
    + '\n' +
    AUTHORS
    + '\n' +
    CHANGES
)

setup_requires = [
    'setuptools_git >= 1.0',
    ]

install_requires = [
    'Kotti',
    'velruse==1.1.2',
    'openid-selector',
    ]

dependency_links = [
    'https://github.com/b4oshany/velruse/tarball/master#egg=velruse-1.1.2'
]


setup(name=name,
      version=version,
      description="Kotti authentication with Velruse: OpenID, OAuth2, Google, Yahoo, Live, Facebook, Twitter and others",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Pylons",
          "Framework :: Pyramid",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: Software Development :: User Interfaces",
      ],
      keywords='pyramid kotti authentication velruse openid oauth2 google yahoo live facebook twitter',
      author='Richard Gomes',
      author_email='rgomes.info@gmail.com',
      url='http://kotti_velruse.readthedocs.org',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      dependency_links=dependency_links,
      setup_requires=setup_requires,
      install_requires=install_requires,

      #TODO
      #entry_points={
      #    'fanstatic.libraries': [
      #        'kotti_tagcloud = kotti_tagcloud.fanstatic:library',
      #    ],
      #},
      #message_extractors={
      #    'kotti_tagcloud': [
      #        ('**.py', 'lingua_python', None),
      #        ('**.zcml', 'lingua_xml', None),
      #        ('**.pt', 'lingua_xml', None),
      #    ]
      #},

      )
