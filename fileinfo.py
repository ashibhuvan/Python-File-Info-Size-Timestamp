import os
import stat
import time

file_name=raw_input("Enter a file name..")
file_stats=os.stat(file_name)

file_info = {
  'fname': file_name,
  'fzise': file_stats [stat.ST_SIZE],
  'f_lm' : time.strftime("%d/%m%Y %I:%M:%S %p", time.localtime(file_stats[stat.ST_MTIME]))


}
print
print "file name = %(fname)s" % file_info
print "file size is %(fzise)s" % file_info
print "the date is %(f_lm)s" % file_info

