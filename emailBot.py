# THIS BOT IS CREATED BY ZEB GAMES (ZEB152) ON MARCH 9, 2022
#
# NOTE: THIS BOT IS MADE FOR ONLY FUN PURPOSES, AND SHOULD NOT BE USED TO HARM ANYONE IN ANYWAY.
# I DO NOT PROMOTE ANY MALICIOUS ACTIVITY USED WITH THIS. PLEASE DO NOT USE IT IF YOU ARE PLANNING TO HARM ANYONE.
#
#


import smtplib
from time import sleep



#VARIABLES =============================================

#initiate the server
smtp_server = "smtp.gmail.com"

#find port
port = 587

#login info> CHANGE IF SENDING THE CODE TO SOMEONE
sender_email = "yourmainemail@gmail.com"
password = 'yourmainpassword'

#BACKUP EMAIL FOR LOGIN
backup_email = 'yoursecondemail@gmail.com'
backup_password = 'yoursecondemailpassword'

#Count the amount of emails that were sent
amount_sent = 0

#we will use this to check if this is the error
errorUnable = ['Daily user sending quota exceeded.']

#define server variable
server = smtplib.SMTP(smtp_server,port)

#END OF VARIABLES ===========================================



#MAIN SCRIPT ==========================================

#Get Email address input for the reciever
userInput = input('Reciever email> ')

#I added this in case you wanted to just type n to input a stored email to send it to
if userInput == 'n':
	receiver_email = 'commonemailreceiver@gmail.com'

else:
	receiver_email = userInput

#Get Message input
message = input('Message> ')

#add an ending to the message
message = 'Hello! This is Bebo Bot! I am programmed in Python to send emails! MESSAGE> <' + message + '>'

#Amount of emails to send input
amount = input('Amount of emails to send> ')



print('Sending...')

botEmail = 0

#END OF MAIN SCRIPT =========================================





#START OF FUNCTIONS ===============================================

def send(): 
	#call all of our variables from before
  global message
  global amount_sent
  global digits
  global amount
  global botEmail
  #Start a loop for however many times the inputed amount was
  for i in range(int(amount)):
  	
    #we are using try so we can see if an error pops up
    try:
      
      #seeing if the 1st or 2nd email is signed in
      if botEmail == 0:
      	sendMessage()
      if botEmail == 1:
      	sendMessage_other()
      
      #Change the amount set to one number above so it can show the number email it is
      amount_sent = amount_sent + 1
      
      #append the random digit to the message
      message = message + ''
      
      #Print the message of the email with the number of which one it is (ex: 2. MESSAGE> Hello World)
      print(str(amount_sent) + '. MESSAGE> ' + message)
      
    #check if errors
    except Exception as e:
      
    	#looking at the words in errorUnable
      for word in errorUnable:
        
      	#If the words are in the error
        if word in str(e):
          
        	#turn the bot email to the alt
          botEmail = 1
          
          #print error
          print('Unable to send, sending limit on Gmail met. Logging in with alt bot account. ')
          
          #calculating the amount of emails to send left
          amount = int(amount) - int(amount_sent)
          
          #connect the the alt account server
          serverConnect_other()
          
          #send message
          send()
          
        #if the error isnt what is shown above, move on
        else:
        	#continue out of for loop
          break
          
      #print error
      print('ERROR FROM CODE> <' + str(e) + '>')
      
      #print what code is doing
      print('Retrying in 30 seconds...')
      
      #calculate the amount of emails to send left
      amount = int(amount) - int(amount_sent)
      
      #wait 30 seconds
      sleep(30)
      
      #set bot email to main
      botEmail = 0
      
      #connect to main account
      serverConnect()
      
      #resend message
      send()
      


def sendMessage():
	#send email from main bot account
  server.sendmail(sender_email, receiver_email, message)
		
def sendMessage_other():
	#send email from alt bot account
  server.sendmail(backup_email, receiver_email, message)
	
		
	
def serverConnect_other():
	try:
		#Connect to the server
		server.connect('smtp.gmail.com', '587')

		#initialize
		server.ehlo()

		#start smtplib system
		server.starttls()

		#initialize
		server.ehlo()

		#Login to SMTPLIB Gmail account
		server.login(backup_email, backup_password)
		print('Logged in with alternate bot email.')
		
	except Exception as e:
		print(e)


def serverConnect():
	try:
		#Connect to the server
		server.connect('smtp.gmail.com', '587')

		#initialize
		server.ehlo()

		#start smtplib system
		server.starttls()

		#initialize
		server.ehlo()

		#Login to SMTPLIB Gmail account
		server.login(sender_email, password)
		print('Logged in')
		
	except Exception as e:
		print(e)



#END OF FUNCTIONS ====================================================



#Connect to the SMTP Server
serverConnect()

#Call the sending function
send()



#COLCLUSION ===================================================

#once loop is finished, quit the SMTP server 
server.quit() 

#print how many emails sent to recipent
print('Sent ' + str(amount) + ' emails sucessfully.')

#Exit the script
exit()






