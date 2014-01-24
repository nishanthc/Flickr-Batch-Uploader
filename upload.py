import flickrapi
import sys,os
import re

# Enter your API Key and Secret here
api_key = ''
api_secret = ''
flickr = flickrapi.FlickrAPI(api_key, api_secret)
(token, frob) = flickr.get_token_part_one(perms='write')
if not token: raw_input("Press ENTER after you authorized this program")
flickr.get_token_part_two((token, frob))
def func(progress, done):
    if done:
        print "Done uploading"
    else:
        print "At %s%%" % progress



# Make a COPY of all your photos to	a new folder then
# Specify the folder here	
root = "/Volumes/TOM/Sorted Photos"
path = os.path.join(root, "")

for path, subdirs, files in os.walk(root):
    for name in files:
		imagepath = os.path.join(path, name)
		
        	if name.startswith('.'):
				print "Invalid File Type on "+name
				
		else:
				if "jpg" in imagepath:

				

				
					print "Uploading "+name
					flickr.upload(filename=imagepath, callback=func)
					print "Uploaded "+name
					os.remove(imagepath)
					print "Deleted "+name


