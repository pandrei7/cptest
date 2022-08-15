from .tester_base import TesterBase

class ReasonableTester(TesterBase):
  """A tester which wants the user output to be mostly identical
  to the correct output, but accounts for whitespace

  Most contest sites are lenient when it comes to whitespace, allowing
  for things like trailing/leading whitespace. This tester discards such
  whitespace before verifying the correctitude.
  """

  def solved_correctly(self, correct_path):
    # Strip both outputs of whitespace at both ends.
    with open(self.output_path, 'r') as fin:
      output = fin.read().strip()
    with open(correct_path, 'r') as fin:
      correct = fin.read().strip()
    return output == correct
