from urllib.request import urlopen

class AtcoderDownloader:
  """A class which can download AtCoder webpages"""

  def download_html(self, contest_id, problem_id):
    """Downloads the HTML code of a given problem's webpage."""
    url = f'https://atcoder.jp/contests/{contest_id}/tasks/{problem_id}'
    return urlopen(url).read().decode('utf-8')
