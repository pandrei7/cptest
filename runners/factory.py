from .c_runner import CRunner
from .cc_runner import CcRunner
from .java_runner import JavaRunner
from .python_runner import PythonRunner
from .rust_runner import RustRunner

C_LANG_IDS = ['c']
CC_LANG_IDS = ['cc', 'c++', 'cpp']
JAVA_LANG_IDS = ['java']
PYTHON_LANG_IDS = ['python', 'py']
RUST_LANG_IDS = ['rust', 'rs']

def get_runner(lang_id):
  if lang_id in C_LANG_IDS:
    return CRunner()
  if lang_id in CC_LANG_IDS:
    return CcRunner()
  if lang_id in JAVA_LANG_IDS:
    return JavaRunner()
  if lang_id in PYTHON_LANG_IDS:
    return PythonRunner()
  if lang_id in RUST_LANG_IDS:
    return RustRunner()

  raise RuntimeError(f'Source language not supported: "{lang_id}"')
