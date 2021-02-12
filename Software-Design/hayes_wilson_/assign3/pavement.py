#/usr/bin/python

from paver.easy import *
import paver.doctools
import os
import glob
import shutil

@task
def setup():
  sh('python3 setup.py -q install')

@task
def test():
  sh('nosetests --rednose --with-coverage --cover-erase --cover-branches --cover-html --cover-package=src test')
  #sh('nosetests --rednose --with-coverage --cover-erase --cover-branches --cover-html --cover-package=src test')

@task
def clean():
  for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
  for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
  for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
  for pycfile in glob.glob("radon.report"): os.remove(pycfile)
  try:
    shutil.rmtree(os.getcwd() + "/cover")
  except:
    pass

@task
def radon():
  sh('radon cc src/* -a -nb')
  sh('radon cc src/* -a -nb > radon.report')
  if (os.stat("radon.report").st_size != 0):
    raise Exception('radon found complex code')

@task
@needs(['setup', 'clean', 'test', 'radon'])
def default():
  pass

