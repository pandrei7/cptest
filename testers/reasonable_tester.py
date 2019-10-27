from .tester_base import TesterBase

class ReasonableTester(TesterBase):
  def solved_correctly(self, correct_path):
    with open(self.output_path, 'r') as fin:
      output = fin.read().strip()
    with open(correct_path, 'r') as fin:
      correct = fin.read().strip()
    return output == correct
