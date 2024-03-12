import pytest

from dabdemo.add_one import *

class TestAddOne(object):

  def test_add_one(self):
    assert 2 == add_one()
