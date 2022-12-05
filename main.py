import os
import requests
import pandas as pd
import json
from parseur_api import ParseurAPI

p = ParseurAPI()
  
mailboxes = p.list_mailboxes()
# df = pd.read_json('list_mailboxes.json')
print(mailboxes)


