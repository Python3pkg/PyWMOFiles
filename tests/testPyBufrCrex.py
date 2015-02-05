# -*- coding: utf-8 -*-

import unittest

class TestBUFR(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TestBUFR))
  return suite
