import datetime
from pytz import timezone
from gr3ybot_settings import LOCALTZ, LOGFILE, ECHO_LOG, timeformat

def log(text):
	localnow = datetime.datetime.now(timezone(LOCALTZ))
	with open(LOGFILE, 'a+') as g:
		g.write("{0} --==-- {1}\r\n".format(localnow.strftime(timeformat),text))
		if ECHO_LOG: print "{0} --==-- {1}".format(localnow.strftime(timeformat),text)
	g.close()
