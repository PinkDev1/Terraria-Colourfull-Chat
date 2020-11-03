from distutils.core import setup
import py2exe
import os

def addCleanDataRecursively(dataDir, folderName):
	allCleanData = str(addDataRecursively(dataDir, folderName))
	
	#Purge all double quote (") characters
	allCleanData = allCleanData.replace('\"', '')

	#Replace cuadruple \\\\ artifacts with \\
	allCleanData = allCleanData.replace('\\\\\\\\','\\\\')

	#Remove "[" at the start, and "]" at the end.
	#These characters were added for some reason
	allCleanData = (allCleanData[1:])[:-1]

	print("\n\nData has been purged. The new data is: \n\n")
	print(str(allCleanData))

	return allCleanData


#yeah, this is big brain time
def addDataRecursively(dataDir, folderName):

	allData = []

	for file in os.listdir(dataDir):
		f1 = dataDir + "\\" + file
		if(os.path.isdir(f1)):
			#https://stackoverflow.com/questions/33141595/how-can-i-remove-everything-in-a-string-until-a-characters-are-seen-in-python
			#https://www.geeksforgeeks.org/python-find-last-occurrence-of-substring/
			#hmm spaguetty
			nestedFolderName = (f1[(f1.rindex('\\')):])[1:]

			#Get data recursively, replicating the file structure
			recursiveData = str(addDataRecursively(f1, (folderName + "\\" + nestedFolderName)))

			#Remove problematic "[" and "]" characters
			recursiveData = (recursiveData[1:])[:-1]

			allData.append(recursiveData)

		else:
			f2 = (str(folderName), [f1])
			allData.append(f2)
			print("Appended "+ str(f2))

	print("\nReturning: " + str(allData) + "\n\n\n\n")
	return allData


ahkTemplatesDir = "C:\\Users\\REPLACE-ME-WITH-YOUR-USERNAME\\Documents\\GitHub\\terrariaColorfullChat\\python37venv\\Lib\\site-packages\\ahk\\templates"

ahkTemplates = addCleanDataRecursively(ahkTemplatesDir, "templates")

setup(
		console=['TerrariaRainbowChat.py'],
		options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'optimize': 2}},
		zipfile = None,
		data_files = ahkTemplates,
		name='Terraria Colourfull Chat',
		version='1.0.2',
	)