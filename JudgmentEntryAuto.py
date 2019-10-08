import win32com, win32com.client, win32gui
import datetime, time, re
import sys, json, os
from os import path

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)


w = WindowMgr()

print("Begin CLS insertion, DO NOT TOUCH KEYBOARD OR MOUSE")
time.sleep(10)

filebase = "enterjudgment"
dt = datetime.datetime.now()
tdate =(dt.strftime("%m%d%Y"))
fileext = ".txt"
fileloc = "\\\\cs_webserver\\C\\Inetpub\\wwwroot\\Oracle1\\Judgments\\EnteredJudgments\\"
#fileloc = "N:\EDI1\JudgmentEntry\Judgments\EnteredJudgments\\";
filename = filebase+tdate+fileext
fullfile = fileloc+filename
fcheck = 0
version = 0;
workingfile = fullfile
workingfilename = filename
currentfile = fullfile
while fcheck ==0:
  if os.path.exists(workingfile):
    print(fullfile + ' exists')
    currentfile = workingfile
    currentfilename = workingfilename
    workingfile = fileloc+filebase+tdate+"_version"+format(version)+fileext
    workingfilename = filebase+tdate+"_version"+format(version)+fileext
    version = version+1
  else:
    print(currentfile + " is the file to be inserted.")
    fcheck = 1
if os.stat(currentfile).st_size == 0:
  print("File is empty. No insert into CLS needed.\nDeleting on exit. Close Window to cancel Delete before exit.\nExiting in 20 seconds.")
  time.sleep(23)
  os.remove(fullfile)
  sys.exit(0)

time.sleep(20)
shell = win32com.client.Dispatch('WScript.Shell')
shell.Run('S:\\ny\\CLSINC\\WBWIN\\BRClient.exe')
time.sleep(7)

shell.SendKeys("{Enter}", 0)
time.sleep(5.1)
print("Work Through Menus")
w.find_window_wildcard(".*CM-.*")
w.set_foreground()

shell.SendKeys("F", 0)
shell.SendKeys("4", 0)
time.sleep(5.1)

pass1 = "PMAN2"
for x in range(5): 
  shell.SendKeys(pass1[x], 0)
shell.SendKeys("{Enter}", 0)
time.sleep(5.1)

w.find_window_wildcard(".*CM-.*")
w.set_foreground()
shell.SendKeys("2", 0)
shell.SendKeys("1", 0)
pass2 = "PEDI"
for x in range(4): 
  shell.SendKeys(pass2[x], 0)
shell.SendKeys("{Enter}", 0)
shell.SendKeys("{Enter}", 0)
shell.SendKeys("{Up}", 0)
shell.SendKeys("{Up}", 0)
time.sleep(5.1)
w.find_window_wildcard(".*Select EDI Type.*")
w.set_foreground()
shell.SendKeys("{Enter}", 0)
shell.SendKeys("1", 0)
shell.SendKeys("{Right}", 0)
locstr = "\\\\cs_webserver\\C\\Inetpub\\wwwroot\\Oracle1\\Judgments\\EnteredJudgments\\"
loclen = len(locstr)
for x in range(loclen): 
  shell.SendKeys(locstr[x],0)
shell.SendKeys("{Enter}", 0)
time.sleep(3.1)

shell.SendKeys("{Enter}", 0)
time.sleep(5.1)
print("Entering Filename")
w.find_window_wildcard(".*Open.*")
w.set_foreground()
#filename = "test" #FOR TESTING ONLY!!

filenamelen = len(currentfilename)
for x in range(filenamelen): 
  shell.SendKeys(currentfilename[x],0)
""" filename = "enterjudgment"
filenamelen = len(filename)
print("Inserting Data")
for x in range(filenamelen): 
  shell.SendKeys(filename[x],0)
dt = datetime.datetime.now()
tdate =(dt.strftime("%m%d%Y"))
w.find_window_wildcard(".*Open.*")
w.set_foreground()
for x in range(8): 
  shell.SendKeys(tdate[x], 0)
fileext = ".txt"
w.find_window_wildcard(".*Open.*")
w.set_foreground()
for x in range(4): 
  shell.SendKeys(fileext[x], 0) """
time.sleep(5.1)

print("Inserting Data")
shell.SendKeys("{Enter}", 0)
time.sleep(5.1)
shell.SendKeys("{Enter}", 0)
time.sleep(5.1)

shell.SendKeys("{Enter}", 0)
time.sleep(200)
w.find_window_wildcard(".*CM-.*")
w.set_foreground()
shell.SendKeys("{Esc}", 0)
shell.SendKeys("{Esc}", 0)

print("Complete")
sys.exit(0)

