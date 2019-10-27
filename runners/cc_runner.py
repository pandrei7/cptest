import os
import subprocess

class CcRunner:
  def run(self, source, in_file, out_file, timeout=60):
    return subprocess.run([os.path.join('.', source)],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)

  def get_default_source(self):
    return 'main'
