import subprocess

class JavaRunner:
  """A common runner for Java programs"""
  def run(self, source, in_file, out_file, timeout=60):
    """Runs a Java program given its main class' name and parameters."""
    return subprocess.run(['java', source],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)

  def get_default_source(self):
    """Returns a useful default name for a main Java class."""
    return 'Main'
