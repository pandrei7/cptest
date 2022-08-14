import json
import os
from typing import List

from cptest.loaders.atcoder_parser import AtcoderParser
from cptest.loaders.test_data import TestData

class TestCodeforcesParser:
  def setup_method(self):
    self.parser = AtcoderParser()
    self.file_prefix = os.path.dirname(os.path.abspath(__file__))

  def test_abc264_abc264c(self):
    html = self.read_html('at_abc264_abc264c.html')
    correct_testcases = self.read_testcases('at_abc264_abc264c.json')
    testcases = self.parser.get_tests(html)
    assert testcases == correct_testcases, \
      'Problems similar to AT ABC264-C should be parsed correctly'

  def test_agc032_agc032a(self):
    html = self.read_html('at_agc032_agc032a.html')
    correct_testcases = self.read_testcases('at_agc032_agc032a.json')
    testcases = self.parser.get_tests(html)
    assert testcases == correct_testcases, \
      'Problems similar to AT AGC032-A should be parsed correctly'

  def read_html(self, filename: str) -> str:
    path = os.path.join(self.file_prefix, 'data', filename)
    with open(path) as fin:
      return fin.read()

  def read_testcases(self, filename: str) -> List[TestData]:
    path = os.path.join(self.file_prefix, 'data', filename)
    with open(path) as fin:
      json_data = json.load(fin)
    return [TestData(**data) for data in json_data]
