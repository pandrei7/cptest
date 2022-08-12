import argparse
import os
import shutil
import subprocess

from . import loaders
from . import runners
from . import testers

# The name of the directory which will hold the test data
TESTS_DIR = 'cp-tests'
# The name of the file used to store the user's output
TESTS_OUT = '.cp_output'
# The time limit for each test run
TIMEOUT = 10

def load(args):
  """Downloads the testcases of the given problem."""
  loader = loaders.get_loader(args.site_id)
  loader.load_tests(args.contest_id, args.problem_id, TESTS_DIR)


def run(args):
  """Tests the user's source and prints the results."""
  runner = runners.get_runner(args.lang_id)
  tester = testers.ReasonableTester(runner, TIMEOUT, TESTS_OUT)

  # If no explicit source was specified, use a default one.
  if not args.source:
    args.source = runner.get_default_source()
  tester.test_all(args.source, TESTS_DIR)


def clean(args):
  """Removes all files used for testing from the current directory."""
  try:
    if os.path.exists(TESTS_DIR):
      shutil.rmtree(TESTS_DIR)
    if os.path.exists(TESTS_OUT):
      os.remove(TESTS_OUT)
    print('The directory is clean.')
  except OSError as e:
    print(f'Error: {e.filename} - {e.strerror}')


def update(args):
  """Updates the program to the latest version."""
  # Updating is done by pulling the latest changes from the repo.
  main_dir = os.path.dirname(os.path.realpath(__file__))
  print(f'Pulling the latest version to {main_dir}')

  os.chdir(main_dir)
  subprocess.run(['git', 'pull'])


def version(args):
  """Prints the current version of the program."""
  print('v1.2')


def main():
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers()

  # Parser for the 'load' command.
  parser_load = subparsers.add_parser('load', help='download testcases')
  parser_load.add_argument('site_id', help='abbreviation for the website')
  parser_load.add_argument('contest_id', help='id of the contest in the url')
  parser_load.add_argument('problem_id', help='id of the problem in the url')
  parser_load.set_defaults(func=load)

  # Parser for the 'run' command.
  parser_run = subparsers.add_parser('run', help='run tests')
  parser_run.add_argument('lang_id', help='language of the source to be tested')
  parser_run.add_argument('source',
                          help='executable or source file to be tested '
                               '(language-specific defaults are available)',
                          nargs='?', default=None)
  parser_run.set_defaults(func=run)

  # Parser for the 'clean' command.
  parser_clean = subparsers.add_parser('clean', help='remove cptest files')
  parser_clean.set_defaults(func=clean)

  # Parser for the 'update' command.
  parser_update = subparsers.add_parser('update', help='get the latest version')
  parser_update.set_defaults(func=update)

  # Parser for the 'version' command.
  parser_version = subparsers.add_parser('version',
                                         help='print the current version')
  parser_version.set_defaults(func=version)

  # If no command is chosen, print the help message.
  # This might change once Python 3.7 is supported.
  args = parser.parse_args()
  try:
    args.func(args)
  except AttributeError:
    parser.print_help()
  except Exception as e:
    print(e)


if __name__ == '__main__':
  main()
