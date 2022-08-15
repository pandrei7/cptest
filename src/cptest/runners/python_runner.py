import subprocess

class PythonRunner:
  """A common runner for Python programs"""
  def run(self, source, in_file, out_file, timeout=60):
    """Runs a given Python script with the provided parameters."""
    return subprocess.run(['python3', source],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)

  def get_default_source(self):
    """Returns a useful default name for a Python script."""
    return 'main.py'
