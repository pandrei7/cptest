import filecmp
import os
import subprocess

class StrictTester:
  def __init__(self, runner, timeout=10, output_path='.cp_output'):
    self.runner = runner
    self.timeout = timeout
    self.output_path = output_path

  def test_all(self, source, test_dir):
    test_names = self.get_test_names(test_dir)
    print(f'Testing {len(test_names)} tests')

    for name in test_names:
      input_path = os.path.join(test_dir, name) + '.in'
      correct_path = os.path.join(test_dir, name) + '.out'
      print(f'Test {name}: ', end='')
      print(self.get_verdict(source, input_path, correct_path))

  def get_test_names(self, test_dir):
    return sorted(
        name
        for (name, ext) in map(os.path.splitext, os.listdir(test_dir))
        if ext == '.in'
    )

  def get_verdict(self, source, input_path, correct_path):
    try:
      self.run_source(source, input_path, self.output_path)
      is_correct = filecmp.cmp(self.output_path, correct_path)
    except subprocess.TimeoutExpired:
      return 'TLE'
    return 'ok' if is_correct else 'WRONG'

  def run_source(self, source, input_path, output_path):
    with open(input_path, 'r') as fin, open(output_path, 'w') as fout:
      self.runner.run(source, fin, fout, self.timeout)
