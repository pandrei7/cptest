import json
import os
from typing import List

from cptest.loaders.codeforces_parser import CodeforcesParser
from cptest.loaders.test_data import TestData

class TestCodeforcesParser:
  def setup_method(self):
    self.parser = CodeforcesParser()
    self.file_prefix = os.path.dirname(os.path.abspath(__file__))

  def test_100d(self):
    html = self.read_html('cf_100_d.html')
    correct_testcases = self.read_testcases('cf_100_d.json')
    testcases = self.parser.get_tests(html)
    assert testcases == correct_testcases, \
      'Problems similar to CF 100D should be parsed correctly'

  def test_1300e(self):
    html = self.read_html('cf_1300_e.html')
    correct_testcases = self.read_testcases('cf_1300_e.json')
    testcases = self.parser.get_tests(html)
    assert testcases == correct_testcases, \
      'Problems similar to CF 1300E should be parsed correctly'

  def read_html(self, filename: str) -> str:
    path = os.path.join(self.file_prefix, 'data', filename)
    with open(path) as fin:
      return fin.read()

  def read_testcases(self, filename: str) -> List[TestData]:
    path = os.path.join(self.file_prefix, 'data', filename)
    with open(path) as fin:
      json_data = json.load(fin)
    return [TestData(**data) for data in json_data]
