#!/usr/bin/env python

import os
from setuptools import setup, find_packages


description = 'Implementation of paper "Computing Optimal Monitoring Strategy for Detecting Terrorist Plots"'
authors = 'Deep Jahan Grewal, Noor Pratap Singh, Luv Agarwal, Shreekavithaa Parupalli'
authors_email = 'deepjahan.grewal@research.iiit.ac.in, parupallishreekavithaa@gmail.com, noorpratap.singh@research.iiit.ac.in, luvagarwal.q@gmail.com'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='TerroristPlotDetection',
      version='1.0',
      description=description,
      author=authors,
      author_email=authors_email,
      url='https://github.com/luviiit/TerroristPlotDetection',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests',]),
      install_requires=['networkx'],
      long_description=read('README.md'),
     )