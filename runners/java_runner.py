import subprocess

class JavaRunner:
  def run(self, source, in_file, out_file, timeout=5000):
    return subprocess.run(['java', source],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)
