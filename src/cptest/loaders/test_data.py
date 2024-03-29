from typing import NamedTuple

class TestData(NamedTuple):
  """Represents all data which comprises a testcase."""
  input_data: str
  output_data: str

  # Tell pytest to ignore this class.
  __test__ = False
