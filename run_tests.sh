#!/bin/sh

cd test && python3 unit_tests.py ${@}  && robot fasta.robot # && python3 test_fasta.py
