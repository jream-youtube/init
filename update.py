#!/usr/bin/env python3

# If the above shebang is invalid:
#   A) Use my PyEnv Shim: ~/.pyenv/shims/python
#   B) Install Python 3 globally :)
#
#
# Simple Script to pull in GitHub repos from user or org, nothing complex.
# Personally: Using Python 3.6
# ------------------------------------------------------------------------
import os
import json
import requests
from subprocess import Popen, PIPE

name = "jream-youtube"
type = "orgs"  # use: orgs || user
url = "https://api.github.com/%s/%s/repos" % (type, name)

params = {
  "page": 1,
  "per_page": 100
}

class color:
  clear = '\033[0m'
  bold = '\033[1m'

def run():
  print ("[+] Getting Repositories from {0}{1}{2}".format(color.bold, url, color.clear))
  response = requests.get(url=url, params=params)
  data = json.loads(response.text)
  for key, item in enumerate(data[0]):
    if (item == 'name'):
      repo_name = data[0]['name']

      if os.path.isdir("./%s" % repo_name):
        print ("[+] Folder {0}{1}{2} exists, running git pull".format(color.bold, repo_name, color.clear))
        proc = Popen(['git', 'pull'], stdout=PIPE)
      else:
        print ("[*] Folder {0}{1}{2} does not exist, running git clone".format(color.bold, repo_name, color.clear))
        proc = Popen(['git', 'clone', 'git@github.com:%s/%s.git' % (name, repo_name)], stdout=PIPE)

      result = proc.communicate()[0]
      print ("--- Result: {0}{1}{2}\n".format(color.bold, result.decode('utf-8'), color.clear))
      continue
  print ("[+] {0}Complete{1}".format(color.bold, color.clear))


if __name__ == '__main__':
  run()
