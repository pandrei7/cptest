"""This module contains factory functions for creating loaders."""

from .atcoder_downloader import AtcoderDownloader
from .atcoder_parser import AtcoderParser
from .codeforces_downloader import CodeforcesDownloader
from .codeforces_parser import CodeforcesParser

from .force_writer import ForceWriter
from .scraping_loader import ScrapingLoader

# Website name constants used to select a loader.
ATCODER_ID = 'at'
CODEFORCES_ID = 'cf'

def get_loader(site_id):
  """Returns a loader fit for the given website."""
  if site_id == ATCODER_ID:
    return ScrapingLoader(AtcoderDownloader(),
                          AtcoderParser(),
                          ForceWriter())

  if site_id == CODEFORCES_ID:
    return ScrapingLoader(CodeforcesDownloader(),
                          CodeforcesParser(),
                          ForceWriter())

  raise RuntimeError(f'Website not supported: "{site_id}"')
