import errno
import os

from .test_data import TestData

class ForceWriter:
  """A class which can store testcases on the computer

  It's called a "force" writer because if the files already
  exist on the computer, they are overwritten.
  """

  def write_tests(self, tests, dest):
    """Stores testcases in a given destination directory.

    The testcase files are numbered and can have the '.in' extension
    for inputs, or the '.out' extension for outputs.

    The directory's content is overwritten.
    """
    self.create_and_clear(dest)
    for (i, test) in enumerate(tests):
      input_path = os.path.join(dest, f'{i}.in')
      output_path = os.path.join(dest, f'{i}.out')

      with open(input_path, 'w') as fout:
        fout.write(test.input_data)
      with open(output_path, 'w') as fout:
        fout.write(test.output_data)

  def create_and_clear(self, dest):
    """Creates the `dest` directory or removes its contents."""
    os.makedirs(dest, exist_ok=True)

    for filename in os.listdir(dest):
      path = os.path.join(dest, filename)
      os.remove(path)
