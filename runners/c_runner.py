import os
import subprocess

class CRunner:
  def run(self, source, in_file, out_file, timeout=5000):
    return subprocess.run([os.path.join('.', source)],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)
