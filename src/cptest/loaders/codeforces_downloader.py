from urllib.request import urlopen
from urllib import request


class CodeforcesDownloader:
    def download_html(self, contest_id, problem_id):
        """Downloads the HTML code of a given problem's webpage."""
        url = f'http://codeforces.com/contest/{contest_id}/problem/{problem_id}'
        # Needed to impersonate Mozilla browser to avoid getting blocked.
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req).read().decode('utf-8')
        #  print('got', resp)
        return resp
