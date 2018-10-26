from testipbase import *
import sys

testipbase_obj = testipbase()

ip = sys.argv[1]
data = testipbase_obj.lookup(ip)
print data

if data['status']==200:
    for key in data['response']:
        print(key,data['response'][key])
else:
    print(data['response'])
