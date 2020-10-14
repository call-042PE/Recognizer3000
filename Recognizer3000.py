import time,os,sys

isText,isData,isRsrc,isBss,isIdata,isEdata = False,False,False,False,False,False

os.system("cls")

print("""

  _____                            _             ____   ___   ___   ___  
 |  __ \                          (_)           |___ \ / _ \ / _ \ / _ \ 
 | |__) |___  ___ ___   __ _ _ __  _ _______ _ __ __) | | | | | | | | | |
 |  _  // _ \/ __/ _ \ / _` | '_ \| |_  / _ \ '__|__ <| | | | | | | | | |
 | | \ \  __/ (_| (_) | (_| | | | | |/ /  __/ |  ___) | |_| | |_| | |_| |
 |_|  \_\___|\___\___/ \__, |_| |_|_/___\___|_| |____/ \___/ \___/ \___/ 
                        __/ |                                            
                       |___/                                             

	""")


class CVars:
	def __init__(self):
		self.isExe = False
		self.UPX = False
		self.isNet = False
		self.VMP = False
		self.Pyinstaller = False
		self.cxFreeze = False
		self.Delphi = False
		self.Enigma = False
		self.Jar = False
		self.ConfuserEx = False
		self.Other = False
		self.Mpress = False
		self.Vars = False
		self.Inno = False

class CColor:
	Red = '\033[91m'
	Green = '\u001b[32m'
	Yellow = '\u001b[33m'
	Blue = '\u001b[34m'
	Cyan = '\u001b[36m'
	White = '\033[0m'


def SectionLookup(line): #define a function for finding if the software use enigma protector
	global isText,isData,isRsrc,isBss,isIdata,isEdata
	#in every enigma protected program the only pe section are .data and .rsrc the other are blank name
	if ".text" in line:
		isText = True
	if ".data" in line:
		isData = True
	if ".rsrc" in line:
		isRsrc = True
	if ".bss" in line:
		isBss = True
	if ".idata" in line:
		isIdata = True
	if ".edata" in line:
		isEdata = True
	if isText == False and isBss == False and isIdata == False and isEdata == False and isData == True and isRsrc == True:
		return True
	else:
		return False
	'''if(mode == "Other"):
		if isText == False and isBss == False and isIdata == False and isEdata == False and isData == False and isRsrc == False:
			return True
		else:
			return False'''

def Analyse(filetoanalyse):
	file = open(filetoanalyse,"r",errors="ignore")
	Vars = CVars()
	Color = CColor()

	for line in file:
		if "MZ" in line:
			Vars.isExe = True
		if "UPX0" in line or "UPX!" in line:
			Vars.UPX = True
		if "NETFramework" in line:
			Vars.isNet = True
		if "base_library.zip" in line:
			Vars.Pyinstaller = True
		if "PyMem_RawMalloc" in line:
			Vars.cxFreeze = True
		if "vmp0" in line:
			Vars.VMP = True
		if SectionLookup(line) == True:
			Vars.Enigma = True
		if "MZP" in line and Vars.isExe != True:
			Vars.Delphi = True
		if "Inno Setup Setup" in line:
			Vars.Inno = True
		if "PK" in line and Vars.isExe != True and Vars.Delphi != True:
			Vars.Jar = True
		if "ConfuserEx v1.0.0" in line:
			Vars.ConfuserEx = True
		if "MPRESS" in line:
			Vars.Mpress = True

	if(Vars.isExe != True):
		print("[*] Not executable file, escaping... [*]")
		time.sleep(2)

	if(Vars.isExe == True):
		#detect type of compiler/library
		if(Vars.isNet == True):
			print(f"{Color.Red}[*] Library: .NET [*]{Color.White}")
		elif(Vars.Pyinstaller == True):
			print(f"{Color.Red}[*] Library: PyInstaller [*]{Color.White}")
		elif(Vars.cxFreeze == True):
			print(f"{Color.Red}[*] Library: cxFreeze [*]{Color.White}")
		elif(Vars.Delphi == True):
			print(f"{Color.Red}[*] Library: Borland Delphi [*]{Color.White}")
		elif(Vars.Jar == True):
			print(f"{Color.Red}[*] Library: Zip(Jar/Apk) [*]{Color.White}")
		elif(Vars.Inno == True):
			print(f"{Color.Red}[*] Library: Inno Setup [*]{Color.White}")
		else:
			print(f"{Color.Red}[*] Compiler: Natif/C++ [*]{Color.White}")

		#detect packer/obfuscator
		if(Vars.UPX == True):
			print(f"{Color.Green}[*] Packer/Obfuscator: UPX [*]{Color.White}")
			print(f"{Color.Yellow}[*] How to unpack it: https://www.youtube.com/watch?v=2DWzJ8WhNPo{Color.White}")
		if(Vars.VMP == True):
			print(f"{Color.Green}[*] Packer/Obfuscator: VMP [*]{Color.White}")
		if(Vars.Enigma == True):
			print(f"{Color.Green}[*] Packer/Obfuscator: Enigma [*]{Color.White}")
		if(Vars.ConfuserEx == True):
			print(f"{Color.Green}[*] Packer/Obfuscator: ConfuserEx [*]{Color.White}")
			print(f"{Color.Yellow}[*] How to unpack it: https://www.youtube.com/watch?v=80MzgB0lnjM{Color.White}")
		if(Vars.Mpress == True):
			print(f"{Color.Green}[*] Packer/Obfuscator: MPRESS [*]{Color.White}")
			print(f"{Color.Yellow}[*] How to unpack it(dont work for all version): https://forum.tuts4you.com/topic/34146-mpress-v219-x32x64-for-newbies/")

	input("Press enter to quit...")
try:
	Analyse(sys.argv[1])
except IndexError:
	print("recognizer3000.py <file>")
	time.sleep(2)