# Utility to check for any new jobs in C:\~Jetmobile\~Jobs folder & display some info about them
# author Abhiroop Dabral
# v 1.0

import os
import re
import datetime

import win32file
import win32event
import win32con
import string

path = r"C:\Program Files\Jetmobile\SecureJet Server Services\Jobs\USER\ABCD" # Path to watch for
#path= r"C:\Users\dZONE\Desktop\py"

change_handle = win32file.FindFirstChangeNotification (path,0,win32con.FILE_NOTIFY_CHANGE_FILE_NAME)

try:

  old_path_contents = dict ([(f, None) for f in os.listdir (path)])
  while 1:
    result = win32event.WaitForSingleObject (change_handle, 500)

    if result == win32con.WAIT_OBJECT_0:
      new_path_contents = dict ([(f, None) for f in os.listdir (path)])
      added = [f for f in new_path_contents if not f in old_path_contents]
      #deleted = [f for f in old_path_contents if not f in new_path_contents]
      #if added: print "Added: ", ", ".join (added)
      #if deleted: print "Deleted: ", ", ".join (deleted)
	  # My open
      for item in added:
       #print item
       match_hdr = re.search(r'\.sjs_hdr$',item,re.M)
       if match_hdr:
         #print "HDR FOUND"
         fullfilename = os.path.join(path, item)
         hdr_file=open(fullfilename,'r')
         #print '__________________________________\n'
         print "Job received on server @:", datetime.datetime.now(), '\n'	 
         for line in hdr_file:
		   if 'ENTITY_MODE' in line: print line,
		   if 'ENTITY_NAME' in line: print line,
		   if 'JOB_NAME' in line: print line,
		   if 'PRINTER_NAME' in line: print line,
		   if 'JOB_TOTAL_PAGES' in line: print line,
		   if 'JOB_NB_COPY' in line: print line,
         print '_______________________________________\n'
         hdr_file.close()       	  
      old_path_contents = new_path_contents
      win32file.FindNextChangeNotification (change_handle)

finally:
  win32file.FindCloseChangeNotification (change_handle)