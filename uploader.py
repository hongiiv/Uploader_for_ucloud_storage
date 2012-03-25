import urllib2
import httplib
import zlib
import cookielib
import sys
import time
import shutil
import gzip

class ReadWrap(object):
   def __init__(self, file_obj):
      self.file_obj = file_obj
      file_obj.seek(0,2)
      self.tot_size = float(file_obj.tell())
      file_obj.seek(0,0)
      self.read_size = 0
      self.last_print = time.time()

   def read(self, size = -1):
      if (time.time() - self.last_print > 1):
         self.last_print = time.time()
      fval = int(float(self.read_size) / self.tot_size * 1000.0)
      sys.stderr.write("\b\b\b\b\b%3d.%1d%%" % (fval / 10, fval %10))
      sys.stderr.flush()
      r = self.file_obj.read(size)
      self.read_size += len(r)
      return r

   def final_print(self):
      sys.stderr.write("100.0%\n")
      sys.stderr.flush()

   def __getattr__(self, name):
      return getattr(self.file_obj, name)

conn = httplib.HTTPConnection('ssproxy.ucloudbiz.olleh.com', '80')
headers = {}
headers['X-Auth-Token']='Your Tocken'

print headers
print conn
fname=sys.argv[1]
f=file(fname)
file_obj=ReadWrap(f)

path="/v1/AUTH_637fcd45-c87e-4d9a-bfdd-385cff5bc5e7/HONG/%s"%(fname)
conn.request('PUT', path, file_obj, headers)
response=conn.getresponse()
print response.read()
