import os
import sys

try:
    URL = sys.argv[1]
    myCmd = 'curl' + ' ' + URL
    os.system(myCmd)
except IndexError:
    print("you need a url")
except Exception:
    print("something else went wrong")
else:
    print("it worked")
finally:
    print("do something else")
