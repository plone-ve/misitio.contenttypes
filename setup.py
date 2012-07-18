from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='misitio.contenttypes',
      version=version,
      description="All the custom content types for misitio website",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='content types product package misitio website',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/plone-ve/misitio.contenttypes',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['misitio'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          'plone.formwidget.namedfile',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': ['plone.app.testing'],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
