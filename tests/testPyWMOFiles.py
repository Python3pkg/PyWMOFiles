# -*- coding: utf-8 -*-
import unittest
import datetime

import PyWMOFiles

class TestBUFR(unittest.TestCase):
  def testISIC01(self):
    with PyWMOFiles.BUFR.Reader('sample/ISIC01.bufr') as bufr:
      version = bufr.version
      data = bufr.data
      date = bufr.date

    self.assertEqual(version, 4)
    self.assertEqual(len(data[0]), 105)
    self.assertEqual(date, datetime.datetime(year=2015, month=2, day=16, hour=15))

  def testISIL01(self):
    with PyWMOFiles.BUFR.Reader('sample/ISIL01.bufr') as bufr:
      version = bufr.version
      data = bufr.data
      date = bufr.date

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TestBUFR))
  return suite
