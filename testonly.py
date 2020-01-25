with open('deleteme.txt','w') as file:
	file.write("some text")

with open('deleteme2.txt','w') as file:
	file.write("somebody else's text")

import os
os.rename('deleteme2.txt','deleteme.txt')
