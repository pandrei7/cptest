from urllib.request import urlopen

class AtcoderDownloader:
  def download_html(self, contest_id, problem_id):
    url = f'https://atcoder.jp/contests/{contest_id}/tasks/{problem_id}'
    return urlopen(url).read().decode('utf-8')
