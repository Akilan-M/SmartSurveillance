from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)



drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'0B2GsqFJywF-5cjVEMjEza0tvUWM' in parents and trashed=false"}).GetList()
for file1 in file_list:
	print 'title: %s, id: %s' % (file1['title'], file1['id'])
