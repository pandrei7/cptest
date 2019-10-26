import errno
import os

from .test_data import TestData

class ForceWriter:
  def write_tests(self, tests, dest):
    self.create_and_clear(dest)
    for (i, test) in enumerate(tests):
      input_path = os.path.join(dest, f'{i}.in')
      output_path = os.path.join(dest, f'{i}.out')

      with open(input_path, 'w') as fout:
        fout.write(test.input_data + '\n\0')
      with open(output_path, 'w') as fout:
        fout.write(test.output_data)

  def create_and_clear(self, dest):
    os.makedirs(dest, exist_ok=True)

    for filename in os.listdir(dest):
      path = os.path.join(dest, filename)
      os.remove(path)
