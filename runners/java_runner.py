import subprocess

class JavaRunner:
  def run(self, source, in_file, out_file, timeout=60):
    return subprocess.run(['java', source],
                          stdin=in_file,
                          stdout=out_file,
                          timeout=timeout)
