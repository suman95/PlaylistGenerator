# Folder wise MP3 playlist generator for Rhythmbox / VLC

#!/usr/bin/python3

import os
import os.path
import glob
import urllib
import urllib.parse


def folder_wise(path,title):
	playlist_name = ''.join(e for e in title if e.isalnum())
	fo = open(playlist_name+".pls","w")
	fo.write("[playlist]\n")
	fo.write("X-GNOME-Title={0}\n".format(title))
	l = len(glob.glob1(path,"*.[Mm][Pp]3"))
	fo.write("NumberOfEntries={0}\n".format(l))
	bulk_handle = glob.glob1(path,"*.[Mm][Pp]3")
	
	#
	it = 1
	for file_handle in bulk_handle:
		st = path +"/"+ urllib.parse.quote(file_handle)
		fo.write("File{0}=file://{1}\n".format(it,st))
		fo.write("Title{0}={1}\n".format(it,file_handle))
		it+=1
	fo.close()
	print("Playlist '{0}.pls' at location '{1}' generated sucessfully.".format(playlist_name,os.getcwd()))


if __name__=="__main__":
	path = str(input("Enter path : "))
	if(path[0]=="'"):
		path=path[1:-1]
		if(path[len(path)-1] == "'"):
			path = path[:-1]
	while(os.path.isdir(path) == False):
		print("Invalid Path to folder")
		if(path[0]=="'"):
			path=path[1:-1]
			if(path[len(path)-1] == "'"):
				path = path[:-1]
		path = str(input("Enter path : "))
	title = str(input("Title : "))
	folder_wise(path,title)