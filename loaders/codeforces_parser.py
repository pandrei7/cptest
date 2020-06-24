from html.parser import HTMLParser

from .test_data import TestData

class CodeforcesParser(HTMLParser):
  """A class which can parse Codeforces webpages for testcase data."""

  def __init__(self):
    HTMLParser.__init__(self)
    self.in_input = False
    self.in_output = False
    self.in_pre = False
    self.curr_input = ''
    self.curr_output = ''
    self.tests = []

  def add_current_test(self):
    # Newer Codeforces tests start with a newline. Remove it if it exists.
    input_data = self.curr_input[self.curr_input.find('\n', 0, 1) + 1:]
    output_data = self.curr_output[self.curr_output.find('\n', 0, 1) + 1:]
    curr_test = TestData(input_data, output_data)

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

  def get_tests(self, html):
    """Parses the given HTML code and returns a list of testcases."""
    self.tests.clear()
    self.feed(self.clean_html(html))
    return self.tests

  def clean_html(self, html):
    """Prepares HTML code to be parsed."""
    return (html.replace('<br />', '\n')
                .replace('<br/>', '\n')
                .replace('<br>', '\n'))
