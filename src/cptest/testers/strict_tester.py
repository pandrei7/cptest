import filecmp

from .tester_base import TesterBase

class StrictTester(TesterBase):
  """A tester which wants the user output to be identical
  to the correct output.
  """

  def solved_correctly(self, correct_path):
    # If the two files differ somehow, the output is not correct.
    return filecmp.cmp(self.output_path, correct_path)
