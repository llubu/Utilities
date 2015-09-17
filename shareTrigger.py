#pip install googlefinance

from googlefinance import getQuotes
import json


print json.dumps(getQuotes('PANW'), indent=2)
