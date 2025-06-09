from setuptools import setup, find_packages
from glob import glob

import bioinfo

setup(
    name = bioinfo.__projectname__,
    version = bioinfo.__release__,
    packages = find_packages(),
    author = bioinfo.__authors__,
    description = bioinfo.__description__,
    license = "GPLv2",
    keywords = "biopython split fasta concat",
    entry_points = {
        'console_scripts': [
            'splitfasta = bioinfo.fasta:main'
            #'sequence_concat = bioinfo.sequence_concat:main',
            #'sequence_files_concat = bioinfo.sequence_files_concat:main',
            #'sequence_split = bioinfo_old.sequence_split:main',
            #'cat_sequences = bioinfo.cat_sequences:main',
            #'phyml_seqrename = bioinfo.phyml_seqrename:main',
            #'raxmlrunner = bioinfo.raxmlrunner:main',
            #'phymlrunner = bioinfo.phymlrunner:main',
            #'seaview_phyml_renamer = bioinfo.seaview_phyml_renamer:main',
        ],
    },
)
