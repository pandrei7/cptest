from urllib.request import urlopen
from html.parser import HTMLParser
import argparse
import os
import subprocess

class CfTest():
  def __init__(self, input_data, output_data):
    self.input_data = input_data
    self.output_data = output_data

  def __repr__(self):
    return 'input:\n%s\nouput:\n%s' % (self.input_data, self.output_data)

  def test_correct_answer(answer):
    return answer == self.output_data


class CfTestParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.in_input = False
    self.in_output = False
    self.in_pre = False
    self.curr_input = ''
    self.curr_output = ''
    self.tests = []

  def add_current_test(self):
    curr_test = CfTest(self.curr_input.strip(), self.curr_output.strip())
    self.tests.append(curr_test)
    self.curr_input = ''
    self.curr_output  = ''

  def handle_starttag(self, tag, attrs):
    if tag == 'div' and ('class', 'input') in attrs:
      self.in_input = True
      self.in_output = False
    elif tag == 'div' and ('class', 'output') in attrs:
      self.in_output = True
      self.in_input = False
    elif tag == 'pre':
      self.in_pre = True

  def handle_data(self, data):
    if self.in_pre:
      if self.in_input:
        self.curr_input = data
      elif self.in_output:
        self.curr_output = data

  def handle_endtag(self, tag):
    if tag == 'pre':
      self.in_pre = False
      if self.in_input:
        self.in_input = False
      elif self.in_output:
        self.in_output = False
        self.add_current_test()

  def get_tests(self, html_data):
    self.tests.clear()
    self.feed(html_data)
    return self.tests


def download_page(url, encoding = 'utf-8'):
  return urlopen(url).read().decode(encoding)

def get_cf_tests(url):
  html_data = download_page(url)
  html_data = html_data.replace('<br />', '\n')
  parser = CfTestParser()
  return parser.get_tests(html_data)

def copy_tests(tests):
  for test in enumerate(tests):
    with open('cf-tests/' + str(test[0]) + '.in', 'w') as fout:
      fout.write(test[1].input_data + '\n\0')
    with open('cf-tests/' + str(test[0]) + '.out', 'w') as fout:
      fout.write(test[1].output_data)

def fill_tests(contest_id, letter):
  try:
    os.makedirs('cf-tests')
    url = 'http://codeforces.com/contest/' + str(contest_id) + '/problem/' + letter
    tests = get_cf_tests(url)
    print('Found', len(tests), 'tests')
    copy_tests(tests)
  except OSError:
    print('Found test directory. Stopped downloading tests')
    return

def run_source(language, input_path, output_path):
  with open(input_path) as fin, open(output_path, 'w') as fout:
    if language in ['c', 'c++']:
      subprocess.run(['./main'], stdin = fin, stdout = fout, timeout = 5000)
    elif language == 'python':
      subprocess.run(['python3.6', 'main.py'], stdin = fin, stdout = fout, timeout = 5000)
    elif language == 'java':
      subprocess.run(['java', 'Main'], stdin = fin, stdout = fout, timeout = 5000)
    else:
      raise RuntimeError('Source language not supported')

def test_verdict(output_path, correct_path):
  with open(output_path) as fin:
    user_output = fin.read().strip()
    with open(correct_path) as fin_correct:
      correct_output = fin_correct.read().strip()
      return 'Correct' if user_output == correct_output else 'WRONG'
  return 'ERROR!!!'

def test_source(language):
  test_count = len([name for name in os.listdir('cf-tests')]) // 2
  print('Testing %d tests' % (test_count))

  for i in range(test_count):
    input_path = 'cf-tests/' + str(i) + '.in'
    run_source(language, input_path, '.cf_output')
    print('Test ' + str(i), end = ': ')
    print(test_verdict('cf-tests/' + str(i) + '.out', '.cf_output'))

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('contest_id', help = 'id number of the contest', type = int)
  parser.add_argument('problem_letter', help = 'uppercase letter of the current problem')
  parser.add_argument('language', help = 'language of the source you want to test')
  args = parser.parse_args()

  fill_tests(args.contest_id, args.problem_letter)
  test_source(args.language)

main()
