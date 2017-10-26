from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)


fid='0B2GsqFJywF-5cjVEMjEza0tvUWM'

f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
f.SetContentFile('PicturesToBeUploaded/nokia1100.jpg')
f.Upload()
	



'''
#Upload in GDrive Directly
f = drive.CreateFile()
f.SetContentFile('document.txt')
f.Upload()

'''
