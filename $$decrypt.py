﻿def readFile(filename):
    with open(filename,'r', encoding='utf-8') as f:
        global inputext
        print(filename)
        inputext=f.read()


def getPW():
    global passw
    try:
        with open('c:/IMPORTANT','r',encoding='utf-8') as f: 
            passw=f.read()

    except:        
        passw=input('请输入密码：\n')
        with open('c:/IMPORTANT','w',encoding='utf-8') as f:
            f.write(passw)
            os.system('attrib +s +r +h +a c:/IMPORTANT')   

def decrypt(outfile):
        '''indicates that the input text should be number only '''          
        listin = list(inputext)
        listp=list(passw)
        p=[ord(x) for x in listp]
        pw=1
        for x in p:
            pw=x*pw
        pw=str(pw)
        pw=pw[-18:]
        pws='0.'+str(pw)
        pw=float(pws)  
        listin=inputext.split(' ')
        texto=''
        for x in listin:
            pw=pw*(1-pw)*3.93699989893668722729139042
            pws=str(pw)
            pivot= int(pws[-6:-3])
            if x=='':
                texto=texto+' '
            elif x[0]=='\n':
                texto=texto+'\n'
            else:
                texto=texto+chr(int(x)^pivot)
        with open(outfile,'w',encoding='utf-8') as f:
            f.write(texto)
        pass

if __name__ == "__main__":    
    from pathlib import Path as p, PurePath as pp
    if p('./EncryptedFiles').is_dir():    
        for x in p('./EncryptedFiles').iterdir():
            if x.is_file():
                plist=['*.py', '*.txt', '*.js', '*.cpp', '*.c', '*.html','*.json', '*.bat']
                match=False
                for m in plist:
                    if x.match(m):
                        match=True
                        break
                if match:
                    readFile(str(x))
                    getPW()
                    decrypt(str(x.name))     