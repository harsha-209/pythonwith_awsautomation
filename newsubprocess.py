import subprocess

sp = subprocess.run("java -version",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)



