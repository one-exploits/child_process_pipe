import os
def parentchild():
	n = os.fork()
	if n > 0:
		
		print("Parent process: Parent returned child id",n)
		os.system("iftop")
	else:
		print("\n\n\n\t\t  W  E  L  C  O  M  E\n\n");
		print("we are in child processs....")
		print(f"child process id using os.gepid() Function {os.getpid()} \n");
		print("Fork() function returned in child == zero **",n);
		#input()
		os.system("top")

# Driver code
parentchild()