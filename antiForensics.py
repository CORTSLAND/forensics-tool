'''Copyright (c) 2018 -- CORTLAND MCPHERSON, All Rights Reserved'''


import os
import imp
import sys




def imp_handle():
    try:
        imp.find_module('bcrypt')
        found = True
    except ImportError:
        found = False


def menu():
    while True:
        try:
            choice = int(raw_input("1.Hide\n2.Unhide\n3.Exit..\n"))
            if choice not in (1,2,3):
                raise ValueError
        except ValueError:
            print('\n**********Wrong Input**********\nInput Must Be 1, 2, or 3\n')
            continue
        except NameError:
            print('\n**********Wrong Input**********\nInput Must Be 1, 2, or 3\n')
            continue
        except SyntaxError:
            print('\n**********Wrong Input**********\nInput Must Be 1, 2, or 3\n')
            continue
        else:
            return choice
			
def options():
    while True:
        try:
            menu = int(raw_input("1.(.jpg) images\n2.Exit..\n"))
            if menu not in (1,2):
                raise ValueError
        except ValueError:
            print('\n**********Wrong Input**********\nInput Must Be 1 or 2\n')
            continue
        except NameError:
            print('\n**********Wrong Input**********\nInput Must Be 1 or 2\n')
            continue
        except SyntaxError:
            print('\n**********Wrong Input**********\nInput Must Be 1 or 2\n')
            continue
        else:
            return menu
   
def file_excep():
    while True:
        jpg_path = raw_input('Enter Path folder of .jpg images:')
        if os.path.exists(jpg_path):
            if jpg_path.endswith('/'):
                return jpg_path
            else:
                jpg_path += '/'
                return jpg_path
        else:
            print('\nPath Does Not Exist\n')
            continue

def files(arg2):
    jpgfiles = [f for f in os.listdir(path) if f.endswith('.jpg')]
    return jpgfiles

def encrypt(arg3,arg4):
    pat = [arg4 + s for s in arg3]
    file = {filename: open(filename,'r+') for filename in pat}
    for file in file.values():
        file.write('\xaa\xbb\xdd')
        file.close() 
        
def decrypt(arg2,arg1):
    pat = [arg1 + s for s in arg2]
    file = {filename: open(filename,'r+') for filename in pat}
    for file in file.values():
        file.write('\xff\xd8\xff')
        file.close()
        
def Hidden():
    
    all_file_names = os.listdir(path)
    
    for Ofile in all_file_names:
        if Ofile.endswith('.jpg'):
            New_fileName = '.'+ Ofile
            os.rename(Ofile,New_fileName)

def unHide():
    
    all_file_names = os.listdir(path)
    
    for Ofile in all_file_names:
        if Ofile.startswith('.'):
            New_fileName = Ofile.replace('.','',1)
            os.rename(Ofile,New_fileName)
    
    
def pascheck(pasarg):
    with open(r'/home/user/Desktop/shhh.txt','r+') as strdpass:
        hashes = strdpass.read()
    if bcrypt.hashpw(pasarg,hashes) == hashes:
        return True
    else:
        print('Wrong Password!')
        return False
    strdpass.close()
		
def NewUsrChek():
    paspat = '/home/user/Desktop/shhh.txt'
    if os.path.isfile(paspat) == True:
        return True
    else:
        return False	
		
def newusr(plain):
    hasher = open('/home/user/Desktop/shhh.txt','w+')
    hashed = bcrypt.hashpw(plain,gensalt())
    hasher.write(hashed)
    hasher.close()		
	

'''#########################MAIN#######################'''

while True:
    if imp_handle() == False:
        #install bcrypt if you dont have it
        os.system('sudo npm install')
        os.system('sudo apt-get install -y build-essential python')
    else:
        import bcrypt
        from bcrypt import hashpw, gensalt
        
        
        choice = menu()
        
        if choice == 3:
            sys.exit()
        
        if NewUsrChek() == False and choice == 1 or NewUsrChek() == False and choice == 2:
            passwd = raw_input("Enter new password: ")
            newusr(passwd)
        
        while choice == 1 or choice == 2:
            att = raw_input("Enter Password: ")
            
            if pascheck(att) == True and choice == 1:
                option = options()
                if option == 1:
                    path =  file_excep()
                    aljpg = files(path) ##print .jpg files to user
                    print(aljpg)
                    encrypt(aljpg,path)
                    Hidden()
                    print("\nFiles are now hidden >:)\n\n")
                    choice = 3
                    continue
                else:
                    sys.exit()
            elif pascheck(att) == True and choice == 2:
                option = options()
                if option == 1:
                    path =  file_excep()
                    aljpg = files(path) ##print .jpg files to user
                    print(aljpg)
                    decrypt(aljpg,path)
                    unHide()
                    print("\nFiles are now unhidden >:)\n\n")
                    choice = 3
                    continue
                else:
                    sys.exit()
            else:
                sys.exit()








    

