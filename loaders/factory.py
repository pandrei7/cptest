from .atcoder_downloader import AtcoderDownloader
from .atcoder_parser import AtcoderParser
from .codeforces_downloader import CodeforcesDownloader
from .codeforces_parser import CodeforcesParser

from .force_writer import ForceWriter
from .scraping_loader import ScrapingLoader

ATCODER_ID = 'at'
CODEFORCES_ID = 'cf'

def get_loader(site_id):
  if site_id == ATCODER_ID:
    return ScrapingLoader(AtcoderDownloader(),
                          AtcoderParser(),
                          ForceWriter())

  if site_id == CODEFORCES_ID:
    return ScrapingLoader(CodeforcesDownloader(),
                          CodeforcesParser(),
                          ForceWriter())

  raise RuntimeError('Website not supported')
