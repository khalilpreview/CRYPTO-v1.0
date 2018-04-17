#Khalil Preview software
#Opensource Software
#Crypto 1.0

#Libs work with it on this Software
from tkinter import *
from PIL import Image
from tkinter import ttk
from random import *

#key for encrypt and decrypt fonction
key = '0123456789abcdefghijklmnopqrstuvwxyz&éàç@=+-*/²<>.~#{[|`\^'
keypass =  randrange(0, 10000000000000)

#encrypt function

def encrypt(n,plaintext):
	result =''
	for l in plaintext.lower():
		try:
			i=(key.index(l)+ n) % 58
			result += key[i]
		except ValueError:
			result +=l

	return result.lower()
#fonction for tkinter and encrypt fonction
def instr ():
	text = str(ent1.get())
	encrupto = encrypt(keypass, text)
	ent2.delete(0,"end")
	ent2.insert(0,encrupto)

#decrypt function

def decrypt(n, ciphertext):
	result = ''
	for l in ciphertext:
		try:
			i=(key.index(l) - n) % 58
			result += key[i]
		except ValueError:
			result +=l

	return result
#fonction for tkinter and decrypt fonction
def instr1 ():
	text = str(ent3.get())
	keypass_conct = int(entre.get())
	decrypto = decrypt(keypass_conct , text)
	ent4.delete(0,"end")
	ent4.insert(0,decrypto)

#fonction of fen for reading
def fen():
	root = Tk()
	root.title("Crypto help center")
	root.maxsize(450,300)
	root.minsize(450,100)
	root.configure(bg='black')
	tex00 = Label(root , text ='===> Welcome <===',fg = 'white',bg='black' )
	tex01 = Label(root , text ='1- To copy => Crtl + c',fg = 'white',bg='black' )
	tex02 = Label(root , text ='2- To past => Crtl + v',fg = 'white',bg='black' )
	tex03 = Label(root , text ='All rights reserved . This programme created by khalil Preview ,',fg = 'white',bg='black' )
	tex04 = Label(root , text ='it\'s an open source Project  ',fg = 'white',bg='black' )
	tex05 = Label(root , text ='Preview Software Terms of Services',fg = 'red',bg='black' )
	tex06 = Label(root , text ='Thank you for using Preview websites , products , services and software\n'
							   'By using our Software , you agree to these terms .\n'
							   'please read them carefully .',fg = 'white',bg='black' )
	tex07 = Label(root , text ='Use of our Software',fg = 'red',bg='black' )
	tex08 = Label(root , text ='You must follow any policies and terms made available to you by Preview \n'
							   'in order to use Preview software. please only use our \n'
							   'software legally and lawfully.\n'
							   'you will be personally liable if you don\'t use our software lawfully .',fg = 'white',bg='black' )
	tex00.pack()
	tex01.pack()
	tex02.pack()
	tex03.pack()
	tex04.pack()
	tex05.pack()
	tex06.pack()
	tex07.pack()
	tex08.pack()
	root.mainloop()


#fenetre du programme primaire
fen1 = Tk()
fen1.title("Crypto 1.1")
fen1.iconbitmap('favicon.ico')
fen1.minsize(320,660)
fen1.maxsize(320,660)
fen1.configure(bg='black')
tex1 = Label(fen1 , text = '===>>> Welcome To Crypto  <<<===', fg = 'white',bg='black')
tex1.pack(side= 'top')
tex2 = Label(fen1 , text= ' * Let Talk Safely * ',fg='white',bg='black' )
tex2.pack(side='top')
tex3 = Label(fen1 , text='Enter to Encrypt >>>' , fg ='white' , bg = 'black')
tex3.pack(side= 'top' )

ent1 = Entry(fen1 , width= 40 )   #entrée du text pour encrypté
ent1.pack(side ='top')

tex4 = Label(fen1 , text='Copy the Encrypted >>>',fg = 'white' , bg ='black')
tex4.pack(side ='top')

ent2 = Entry(fen1 , width= 40, bg='gold') #la sortie du text encrypté
ent2.pack(side='top')

bou1 = Button(fen1 , text='encrypt' , command=instr)#button pour encrypté
bou1.pack(side='top',pady=40)

tex5 = Label(fen1 , text='Enter to Decrypt >>>',fg='white', bg='black')
tex5.pack()

ent3 = Entry(fen1 , width= 40)#text entry pour décrypté
ent3.pack(side='top')

tex6 = Label(fen1 , text='Copy the  Decrypt >>>', bg='black',fg='white')
tex6.pack(side='top')

ent4 = Entry(fen1 ,width = 40,bg='gold')#text sortie pour décrypté
ent4.pack(side='top')

espace = Label(fen1 , text='   ',fg='white', bg='black')#vide text pour l'espasce
espace.pack()

entre = Entry(fen1 ,width = 25 ,bg='black',fg = 'red')#entrié for code offsef
entre.pack()

bou2 = Button(fen1 , text='decerypt', command=instr1)#button pour décrypté le text
bou2.pack(side='top' ,pady=10 )

bou3 = Button(fen1 , text='For Reading', command=fen)#button pour affichier la fenétre
bou3.pack(side='top', pady = 10 )

tex8 =  Label(fen1 , text=' This days the enternet is not safe    \n'
						  ' For this we need to talk safely it\'s \n '
						  'a personel thiks and our freedom \n'
					      ' \n'
						  ' \n'
						  ' ',fg='red', bg='black')
tex8.pack()

keypassgenerate = Text(fen1,  height=1,bg='black',fg='red')#keypass affichage
keypassgenerate.insert(1.0 , keypass)
keypassgenerate.config(width = 14 , font = ('times',25,'bold'))
keypassgenerate.pack()

photo = PhotoImage(file ="logo.png")
img = Label(fen1 , image = photo , bg ='black')
img.photo = photo
img.pack()

# Keep a reference!
# (or don’t and see what happens)





fen1.mainloop()

















