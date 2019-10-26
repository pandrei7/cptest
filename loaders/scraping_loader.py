class ScrapingLoader:
  __slots__ = ['downloader', 'parser', 'writer']

  def __init__(self, downloader, parser, writer):
    self.downloader = downloader
    self.parser = parser
    self.writer = writer

  def load_tests(self, contest_id, problem_id, dest):
    html = self.downloader.download_html(contest_id, problem_id)
    tests = self.parser.get_tests(html)
    self.writer.write_tests(tests, dest)
