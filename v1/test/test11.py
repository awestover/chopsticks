#!/usr/bin/env python
from subprocess import Popen,PIPE,STDOUT,call

proc=Popen('pwd', shell=True, stdout=PIPE, )
output=proc.communicate()[0]
print(output) 