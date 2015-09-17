# This script checks the price of a share at a frequency
# specified in 'freq(seconds)' and emails the details if
# absolute price difference is greater then 'trigger'.
#
#currently configured for NYSE

from googlefinance import getQuotes
import json
import smtplib
import time
from email.mime.text import MIMEText
from datetime import datetime
from pytz import timezone

# variables
symbol = "PANW"
trigger = 1
freq = 600
srcmail = "send@gmail.com"
dstmail = 'rcv@gmail.com'
smtpServer = 'smtp.gmail.com:587'
password = "*******"
lastValue = 0
data = []

while (1):
    eastern = timezone('US/Eastern')
    nycTime = datetime.now(eastern).time()
    nyseStart = nycTime.replace(hour=9, minute=25, second=0, microsecond=0)
    nyseShutdown = nycTime.replace(hour=20, minute=0, second=0, microsecond=0)

    if ((nycTime > nyseShutdown) or (nycTime < nyseStart)):
	    break

    data = (getQuotes(symbol))
    datastr = json.dumps(data, indent=2)

    price = float(data[0]['LastTradePrice'])

    print json.dumps(data, indent=2)

    if lastValue >= 0:
        lastValue = price
    elif (1 <= (abs(lastValue - price))):
        msg = MIMEText("PANW - LastPrice= " + str(lastValue) + '\n' + datastr + "\n")
        msg['Subject'] = 'Trigger PANW. %s' % str(price)
        msg['From'] = srcmail
        msg['To'] = dstmail
        server = smtplib.SMTP(smtpServer)
        server.ehlo()
        server.starttls()
        server.login(srcmail,password)
        server.sendmail(srcmail, [dstmail], msg.as_string())
	print "mail sent"
    time.sleep(freq)
