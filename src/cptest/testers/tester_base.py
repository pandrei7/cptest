import os
import subprocess

from abc import ABC, abstractmethod

class TesterBase:
  """An abstract base class for simple testers

  Provides a common algorithm which runs the given source against
  the given testcases, and prints the test verdicts.

  Subclasses must implement the `solved_correctly` method. They can
  also override the other methods of this class, which act as hooks.
  """

  def __init__(self, runner, timeout, output_path):
    """Sets the common parameters of a `TesterBase`.

    Args:
      runner : the runner object used to execute a source
      timeout (int) : the time limit allowed for each test run
      output_path (str) : the name of the file used to hold user output
    """
    self.runner = runner
    self.timeout = timeout
    self.output_path = output_path

  def test_all(self, source, test_dir):
    """Runs a source against all tests in a given directory,
    and prints the verdicts.
    """
    test_names = self.get_test_names(test_dir)
    print(f'Testing {len(test_names)} tests')

    for name in test_names:
      input_path = os.path.join(test_dir, name) + '.in'
      correct_path = os.path.join(test_dir, name) + '.out'
      print(f'Test {name}: ', end='')
      print(self.get_verdict(source, input_path, correct_path))

  def get_test_names(self, test_dir):
    """Returns the list of names (without extension)
    of the test files held in a given directory.
    """
    return sorted(
        name
        for (name, ext) in map(os.path.splitext, os.listdir(test_dir))
        if ext == '.in'
    )

  def get_verdict(self, source, input_path, correct_path):
    """Runs a source on a given test and returns the verdict string."""
    try:
      self.run_source(source, input_path, self.output_path)
    except subprocess.TimeoutExpired:
      return 'TLE'
    return 'ok' if self.solved_correctly(correct_path) else 'WRONG'

  def run_source(self, source, input_path, output_path):
    """Runs a given source, piping I/O through the given files."""
    with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
      self.runner.run(source, fin, fout, self.timeout)

  @abstractmethod
  def solved_correctly(self, correct_path):
    """Checks if the output of the source matches the correct output.

    The correct output is held in the `correct_path` file.

    The user output was obtained during the previous run of the source.
    It's held in the `output_path` file (attribute of `TesterBase`).

    All subclasses must implement this method.
    """
    pass
