import flickrapi
import sys,os
import re
import time
start_time = time.time()



api_key = 'a4205485797b3b1905b3780f3594b052'
api_secret = '0380966305339999'
count = 0
flickr = flickrapi.FlickrAPI(api_key, api_secret)
(token, frob) = flickr.get_token_part_one(perms='write')
if not token: raw_input("Press ENTER after you authorized this program")
flickr.get_token_part_two((token, frob))
def func(progress, done):
    if done:
        print "Done uploading"
    else:
        print "At %s%%" % progress




		
root = "/Users/Nish/Sorted Photos"
path = os.path.join(root, "")



for path, subdirs, files in os.walk(root):
	
    	for name in files:
		imagepath = os.path.join(path, name)
		
        	if name.startswith('.'):
				print "Invalid File Type on "+name
				
		else:
				if "jpg" in imagepath:

				

					count = int(count)
					flickr.upload(filename=imagepath, callback=func)
					print "Uploaded "+name
					count = count + 1
					count = str(count)
					os.remove(imagepath)
					elapsed_time = time.time() - start_time
					elapsed_time = elapsed_time / 60
					average_per_photo = elapsed_time / int(count)
					average_per_photo = average_per_photo * 60
					elapsed_time = round(elapsed_time, 1)
					elapsed_time = str(elapsed_time)
					print "Uploaded "+count+" photos in "+elapsed_time+" minutes"+" --  Average of "+str(round(average_per_photo,2))+" sec per photo"
					

