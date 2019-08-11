import os 
import glob 

def __pycache__Deleter() :
	BASE_DIR = os.getcwd()
	CACHE_DIR = os.path.join(BASE_DIR, "__pycache__")

	if os.path.exists(CACHE_DIR) :
		os.chdir(CACHE_DIR)
		files = glob.glob("*")
		for particular_file in files :
			os.remove(particular_file)
		os.chdir(BASE_DIR)
		os.rmdir("__pycache__")