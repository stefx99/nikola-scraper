import os
from sys import version_info


## Python version 
PYTHON_VERSION = version_info.major

## Maximum number or pages to search
SEARCH_ENGINE_RESULTS_PAGES = 5

## HTTP request timeout 
TIMEOUT = 10

## Default User-Agent string 
USER_AGENT = 'search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper'

## Fake User-Agent string - Google desn't like the default user-agent
FAKE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0'

## Proxy server 
PROXY = None

## TOR proxy server 
TOR = 'socks5h://127.0.0.1:9050'

_base_dir = os.getcwd()

## Path to output files 
OUTPUT_DIR = _base_dir + os.sep

FILE_NAME = OUTPUT_DIR + 'processed/' + 'result_'
