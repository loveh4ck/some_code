import os
import time

def getchromepid():
	result = os.popen('''FOR /F "tokens=2 " %i IN ('tasklist^|find "chrome.exe"') DO @echo %i''').read()
	return result
def killchrome(pid):
	os.system('taskkill /f /pid '+pid)

while True:
	old_chromepid = getchromepid()
	time.sleep(120)
	new_chromepid = getchromepid()
	line = old_chromepid.split("\n")
	for pid in line:
		if pid in new_chromepid:
			killchrome(pid)
		else:
			pass
