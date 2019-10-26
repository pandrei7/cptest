import subprocess

class PythonRunner:
  def run(self, source, in_file, out_file, timeout=5000):
    return subprocess.run(['python3', source],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)
