import argparse
import os
import shutil

import loaders
import runners
import testers

TESTS_DIR = 'cp-tests'
TESTS_OUT = '.cp_output'
TIMEOUT = 10

def load(args):
  loader = loaders.get_loader(args.site_id)
  loader.load_tests(args.contest_id, args.problem_id, TESTS_DIR)


def run(args):
  runner = runners.get_runner(args.lang_id)
  tester = testers.ReasonableTester(runner, TIMEOUT, TESTS_OUT)

  # If no explicit source was specified, use a default one.
  if not args.source:
    args.source = runner.get_default_source()
  tester.test_all(args.source, TESTS_DIR)


def clean(args):
  try:
    if os.path.exists(TESTS_DIR):
      shutil.rmtree(TESTS_DIR)
    if os.path.exists(TESTS_OUT):
      os.remove(TESTS_OUT)
    print('The directory is clean.')
  except OSError as e:
    print(f'Error: {e.filename} - {e.strerror}')


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
