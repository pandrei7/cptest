import filecmp

from .tester_base import TesterBase

class StrictTester(TesterBase):
  def solved_correctly(self, correct_path):
    return filecmp.cmp(self.output_path, correct_path)
