import os

d = os.listdir("./animations")
__all__ = []
for x in d:
	if(x.endswith(".py")):
		__all__.append(x.replace(".py", ""))