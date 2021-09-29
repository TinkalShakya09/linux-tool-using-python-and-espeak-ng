
import os
import smtplib,ssl
import time
from englisttohindi.englisttohindi import EngtoHindi

def EtoHS(mess):
	res=EngtoHindi(mess)
	res1=res.convert
	os.system("espeak-ng -v hi '%s' -s 140 -a 200"%res1)

def EtoHP(mes):
	mes1=EngtoHindi(mes)
	mes2=mes1.convert
	print(mes2)


def mail(voice,inp):
	print()
	if inp=="y":
	    print("That means are you intersted to send the message")
	    os.system("espeak-ng -v en%s 'That means you are intersted to send the message' -a 200 -s 140"%voice)
	    print("Mail id : tinkalshakya8650@gmail.com ")
	    os.system("espeak-ng -v en%s 'This is your Mail id ' -a 200 -s 140"%voice)
	    passwd="Tinkal68"
	    print("Password : T*******")
	    os.system("espeak-ng -v en%s 'This is your password ' -a 200 -s 140"%voice)
	    os.system("espeak-ng -v en%s 'Enter your receiver mail' -a 200 -s 140"%voice)
	    receiver_mail=input("Enter the mail you want to send the message : ")
	    os.system("espeak-ng -v en%s 'Type the Message when you want to sent' -a 200 -s 140"%voice)
	    message=input("Type your Message : ")
	    context=ssl.create_default_context()
	    server= smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)
	    server.login("tinkalshakya8650@gmail.com",passwd)
	    server.sendmail("tinkalshakya8650@gmail.com", receiver_mail, message)
	    server.quit()
	    print("Mail Sended")
	    os.system("espeak-ng -v en%s 'Mail sended successfully' -a 200 -s 140"%voice)
	elif inp=="n":
		print("you are not intersted to send the message")
		os.system("espeak-ng -v en%s 'ops That means you are not intersted to send the message' -a 200 -s 140"%voice)
		
	else:
	    print("Invalid Key! Try again")


def mailHindi(inp):
	print()
	if inp=="y":
	    EtoHS("That means are you intersted to send the message")
	    print("Mail id : tinkalshakya8650@gmail.com ")
	    EtoHS("This is your Mail id ")
	    passwd="Tinkal68"
	    print("Password : T*******")
	    EtoHS("This is your password")
	    EtoHS("Enter your receiver mail")
	    receiver_mail=input("Enter the mail you want to send the message : ")
	    EtoHS("Type the Message when you want to sent")
	    message=input("Type your Message : ")
	    context=ssl.create_default_context()
	    server= smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)
	    server.login("tinkalshakya8650@gmail.com",passwd)
	    server.sendmail("tinkalshakya8650@gmail.com", receiver_mail, message)
	    server.quit()
	    EtoHP("Mail Sended")
	    EtoHS("Mail sended successfully")
	elif inp=="n":
		EtoHP("you are not intersted to send the message")
		EtoHS("That means you are not intersted to send the message")

	else:
	    EtoHP("Invalid Key! Try again")
	    EtoHS("Invalid Key! Try again")
	    
def Interesting_thing(voice):
	print()
	print("\t-----------------------------------------------")
	print("""Show some Interesting Things
	\tPress 1 : Show the running train
	\tPress 2 : Show the Dragon and Cow
	\tPress 3 : Show the Fire
	\tPress 4 : Show the turtle
	\tPress 5 : See the simulating text
	\tPress 6 : exit
	""")
	
	inter_inp=input("what is your choice just Press it : ")
	
	if inter_inp=="1":
		os.system("espeak-ng -v en%s 'ok ' -a 200 -s 140"%voice)
		time.sleep(1)
		os.system("espeak-ng -v en%s 'I wil Show the running train' -a 200 -s 140"%voice)
		os.system("sl")
	elif inter_inp=="2":
		os.system("espeak-ng -v en%s 'excellent ' -a 200 -s 140"%voice)
		time.sleep(1)
		os.system("espeak-ng -v en%s 'I wil Show you the dragon and cow talking to each other ' -a 200 -s 140"%voice)
		os.system("cowsay -f dragon-and-cow Hey cow what are you doing here")
	elif inter_inp=="3":
		os.system("espeak-ng -v en%s 'Greate' -a 200 -s 140"%voice)
		time.sleep(1)
		os.system("espeak-ng -v en%s 'I wil Show you the Fire ' -a 200 -s 140"%voice)
		os.system("aafire")	
	elif inter_inp=="4":
		os.system("espeak-ng -v en%s 'amazing' -a 200 -s 140"%voice)
		time.sleep(1)
		os.system("espeak-ng -v en%s 'I wil Show you the turtle ' -a 200 -s 140"%voice)
		os.system("cowsay -f turtle I Love technology")
	elif inter_inp=="5":
		os.system("echo ' I would like to thankyou for Mr. vimal daga sir for your insightful guidence on the right approach' | pv  			-qL 10")
		os.system("espeak-ng -v en%s 'if You want to show this type of your own text so type yes otherwise no  ' -a 200 -s 			140"%voice)
		text_inp=input("show your own text so type [y/n] : ")
		if text_inp=="y":
			text=input("Enter the text : ")
			os.system("echo ' %s ' | pv -qL 10"%text)
		elif text_inp=="n":
			print("ok! No Problem")
			os.system("espeak-ng -v en%s 'ok! No Problem' -a 200 -s 140"%voice)
		else:
			print("Invalid Key! Try again")
	elif inter_inp=="6":
		os.system("clear")
		print("Thankyou For Visiting........")
		exit()
	else:
		print("Invalid Key! Try again")

def Interesting_thing_Hindi():
	print()
	print("\t-----------------------------------------------")
	EtoHP("Show some Interesting Things")
	print("Show some Interesting Things")
	EtoHP("press 1 : Show the running train")
	EtoHP("press 2 : to see the Dragon and Cow")
	EtoHP("press 3 : to see the burning Fire")
	EtoHP("press 4 : to see the turtle")
	EtoHP("press 5 : See the simulating text")
	EtoHP("press 6 : to come exit")
	EtoHP("Press any key from 1 to 5 in the above table otherwish Press 6 to exit")
	EtoHS("Press any from 1 to 5 in the above table otherwish Press 6 to exit")
	inter_inp=input()
	if inter_inp=="1":
		EtoHS("OK")
		time.sleep(1)
		EtoHS("I show you the running train")
		os.system("sl")
	elif inter_inp=="2":
		EtoHS("espeak-ng -v en%s 'excellent ' -a 200 -s 140"%voice)
		time.sleep(1)
		EtoHS("I Show you the dragon and cow talking to each other ")
		os.system("cowsay -f dragon-and-cow Hey cow what are you doing here")
	elif inter_inp=="3":
		EtoHS("Ok")
		time.sleep(1)
		EtoHS("I'll show you the burning Fire ")
		os.system("aafire")	
	elif inter_inp=="4":
		EtoHS("amazing")
		time.sleep(1)
		EtoHS("I Show you the turtle ")
		os.system("cowsay -f turtle I Love technology")
	elif inter_inp=="5":
		os.system("echo ' I would like to thankyou for Mr. vimal daga sir for your insightful guidence on the right approach' | pv -		-qL 10")
		EtoHS("if You want to show this type of your own text so type yes otherwise type no")
		text_inp=input("show your own text so type [y/n] : ")
		if text_inp=="y":
			text=input("Enter the text : ")
			os.system("echo ' %s ' | pv -qL 10"%text)
		elif text_inp=="n":
			EtoHS("ok! No Problem")
			EtoHP("ok! No Problem")
		else:
			EtoHS("Invalid Key! Try again")
			EtoHP("Invalid Key! Try again")
	elif inter_inp=="6":
		EtoHP("Thankyou For Visiting")
		os.system("clear")
		exit()
	else:
		EtoHS("Invalid Key! Try again")
		EtoHP("Invalid Key! Try again")

def prin():
	print()
	print("\t---------------------------------------------------------")
	print("""\tDo you want to Send the Mail or want to see some interesting things
		 \tPress 1 : Mail send
		 \tPress 2 : Some Interesting things
		 \tPress 3 : exit
	""")
	
def prinH():
	print()
	EtoHP("Do you want to Send the Mail or want to see some interesting things")
	print("Do you want to Send the Mail or want to see some interesting things")
	EtoHP("press 1 : for Mail the send")
	print("press 1 : for Mail the send")
	EtoHP("press 2 : show the Some Interesting things")
	print("press 2 : show the Some Interesting things")
	EtoHP("press 3 : to come exit")
	print("press 3 : to come exit")
	print()
	

print("\t-------------------------------------------------------------------------------------")
print("\t\t\tWelcome to My World")
print("\t-------------------------------------------------------------------------------------")
print()
print("""\tWhich voice you like male voice or female Voice  
         \tPress 1 : Hindi Voice
         \tPress 2 : Female Voice
	 \tPress 3 : Male Voice
         
""")
voice=input("what you want voice  : ")

while True:
	
	 

	if voice=="3":
		prin()
		voic=""
		mail_interest=input("what you want : ")	
		if mail_interest=="1":
			inp=input("If you want to send the message press [n/y] : ")
			mail(voic,inp)

		elif mail_interest=="2":
			while True:
				Interesting_thing(voic)

		elif mail_interest=="3":
			print("Thankyou..............")			
			exit()
		else:
			print("Invalid Key! Try again")

	elif voice=="2":
		prin()
		voic="+f2"
		mail_interest=input("what you want : ")
		if mail_interest=="1":
			inp=input("If you want to send the message press [n/y] : ")
			mail(voic,inp)

		elif mail_interest=="2":
			while True:
				Interesting_thing(voic)

		elif mail_interest=="3":
			print("Thankyou..............")	
			exit()
		else:
			print("Invalid Key! Try again")

	elif voice=="1":
		prinH()
		voic="hi"
		EtoHP("what you want : ")
		EtoHS("Which option did you like")
		mail_interest=input("what you want : ")
		if mail_interest=="1":
			inp=input("If you want to send the message press [n/y] : ")
			mailHindi(inp)

		elif mail_interest=="2":
			while True:
				Interesting_thing_Hindi()

		elif mail_interest=="3":
			EtoHS("Thankyou")
			EtoHP("Thankyou")	
			os.system("clear")
			exit()
		else:
			EtoHS("Invalid Key! Try again")
			EtoHP("Invalid Key! Try again")			
			print("Invalid Key! Try again")
	else:
		print("Invaid Key try again")



