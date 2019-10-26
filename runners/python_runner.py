import subprocess

class PythonRunner:
  def run(self, source, in_file, out_file, timeout=60):
    return subprocess.run(['python3', source],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)