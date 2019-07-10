from distutils.core import setup
setup(
  name = 'pyPheWAS',
  packages = ['pyPheWAS'], # this must be the same as the name above
  version = '2.0.1',
  description = 'MASI Lab Port of PheWAS into Python',
  author = 'MASI Lab',
  author_email = 'bennett.landman@vanderbilt.edu',
  url = 'https://github.com/MASILab/pyPheWAS', # use the URL to the github repo
  download_url = 'https://github.com/MASILab/pyPheWAS/tarball/0.1', # I'll explain this in a second
  keywords = ['PheWAS', 'ICD-9', 'EMR'], # arbitrary keywords
  classifiers = [],
  install_requires=['numpy',
	'matplotlib',
	'scipy',
	'pandas',
	'statsmodels',
        'numexpr',
        'bottleneck',
        'hopcroftkarp',
        'tqdm'
	],
  package_data={
    '':['resources/*.csv']
  },
  scripts=['bin/maximizeControls',
  'bin/pyPhewasLookup',
  'bin/pyPhewasModel',
  'bin/pyPhewasPlot',
  'bin/generateGroups',
  'bin/censorData',
  'bin/convertEventToAge',
  'bin/createGenotypeFile'
  ],
)
