import os
import os.path

def convert_file(filename):
	try:
		f = open(filename, 'rb')
		s = f.read().decode('cp1252').encode('utf-8').replace('cp1252', 'utf-8', 1)
		f.close()

		f = open(filename, 'wb')
		f.write(s)
		f.close()

	except:
		print("ERROR: Failed to convert file '%s'" % filename)

def convert_all(rootdir):
	files = []

	for parent, dirnames, filenames in os.walk(rootdir):
		for filename in filenames:
			if filename.endswith(".htm") or filename.endswith(".html"):
				files.append(os.path.join(parent, filename))

	for filename in files:
		convert_file(filename)

if __name__ == "__main__":
	convert_all("./")
