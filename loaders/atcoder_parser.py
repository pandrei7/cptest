from html.parser import HTMLParser

from .test_data import TestData

class AtcoderParser(HTMLParser):
  """A class which can parse AtCoder webpages for testcase data."""

  def __init__(self):
    HTMLParser.__init__(self)
    self.in_input = False
    self.in_output = False
    self.in_h3 = False
    self.in_pre = False
    self.curr_input = ''
    self.curr_output = ''
    self.should_read_pre = False
    self.tests = []

  def add_current_test(self):
    input_data = self.curr_input.replace('\r\n', '\n')
    output_data = self.curr_output.replace('\r\n', '\n')
    curr_test = TestData(input_data, output_data)

    self.tests.append(curr_test)
    self.curr_input = ''
    self.curr_output = ''

  def handle_starttag(self, tag, attrs):
    self.in_h3 = (tag == 'h3')
    self.in_pre = (tag == 'pre')

  def handle_data(self, data):
    if self.in_pre:
      if self.in_input:
        self.curr_input = data
      elif self.in_output:
        self.curr_output = data
    elif self.in_h3:
      self.in_input = data.startswith('Sample Input')
      self.in_output = data.startswith('Sample Output')

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
    self.feed(html)
    return self.tests
