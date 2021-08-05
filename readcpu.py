name='/proc/cpuinfo'
fobj=open(name)
s=fobj.read()
print(s)
fobj.close()
