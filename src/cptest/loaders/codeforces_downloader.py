from urllib.request import urlopen

class CodeforcesDownloader:
  def download_html(self, contest_id, problem_id):
    """Downloads the HTML code of a given problem's webpage."""
    url = f'http://codeforces.com/contest/{contest_id}/problem/{problem_id}'
    return urlopen(url).read().decode('utf-8')
