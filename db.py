"""
Command line utility to:
1. Get the dropbox folders list.
2. Upload the contents of local folder to a specific folder on DB
@author Abhiroop Dabral - abhiroop.dabral@gmail.com
DATE(C,M) 07-27-2014, 07-27-2014
"""

import dropbox
from dropbox import rest as dbrest
import os, sys
from optparse import OptionParser

class Db:
    
    def __init__(self):
	
	access_token = '' # Add the access token for your account

	print "Login NOW >>"

	self.client = dropbox.client.DropboxClient(access_token)
        print 'linked account: ', self.client.account_info()

    def get_flist(self):
	"""
	    List the folder in the DrobBox account linked
	"""
	dblist = self.client.metadata('/')
	content_list = dblist['contents']
	for item in content_list:
	    if item['is_dir'] == True:
	        print item['path'], item['root'], item['size']
    

    def db_upload(self, u_path, l_path):
	"""
	    Upload *all* contents of current local dir to
	    specified DB folder
	    @var: u_path: Name of the DB foler to upload to
	    @var: l_path: Path to the local folder to be uploaded
	"""
        if os.access(l_path, os.R_OK):
	    f_list = os.listdir(l_path)
	    for item in f_list:
		if item == '.DS_Store':
		    continue
		f = open(item, 'rb')
                fullpath = l_path+'/'+item
                upath = u_path + '/' + item
		response = self.client.put_file(upath, f, overwrite=False)
		print 'uploaded:', response


        
	
	      
def main():
    local_path = '/Users/adabral/src/util'
    upload_path = '/test'
    dbobj = Db()
    dbobj.get_flist()
    print upload_path, local_path
    dbobj.db_upload(upload_path, local_path)


	    
if __name__ == '__main__':
    main()







