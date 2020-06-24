import os
import subprocess

class CcRunner:
  """A common runner for C++ programs"""
  def run(self, source, in_file, out_file, timeout=60):
    """Runs a given executable with the provided parameters."""
    return subprocess.run([os.path.join('.', source)],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)

  def get_default_source(self):
    """Returns a useful default name for a C++ executable."""
    return 'main'
