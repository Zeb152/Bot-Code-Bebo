### Created by Zeb Games (Zeb152) March 9, 2022
### 
#This is a simple email bot that sends a ton of emails to the recipient. In May, 2022, Google recently removed the 3rd party login services. To get this code to work, you will need to enable 2 factor authentication and set up an app   password. If you need help setting up your gmail account to work for this script, see this -> https://www.letscodemore.com/blog/smtplib-smtpauthenticationerror-username-and-password-not-accepted/
###
### NOTE:  THIS BOT IS MADE FOR ONLY FUN PURPOSES, AND SHOULD NOT BE USED TO HARM ANYONE IN ANYWAY.
#  I DO NOT PROMOTE ANY MALICIOUS ACTIVITY USED WITH THIS. PLEASE DO NOT USE IT IF YOU ARE PLANNING TO HARM ANYONE.
###


#Import the needed libraries
import smtplib
from time import sleep


#VARIABLES =============================================

#initiate the server
smtp_server = "smtp.gmail.com"

#find port
port = 587

#login info> CHANGE FOR YOUR OWN PERSONAL NEEDS
sender_email = "FIRSTEMAILACCOUNT@gmail.com"
password = 'UNIQUE 16 DIGIT CODE HERE' #that email's 16 digit code

#BACKUP EMAIL FOR LOGIN
backup_email = 'SECONDEMAILACCOUNT@gmail.com'
backup_password = 'UNIQUE 16 DIGIT CODE HERE' #that email's 16 digit code

#Count the amount of emails that were sent
amount_sent = 0

botEmail = 0

#we will use this to check if this is the error
errorUnable = ['Daily user sending quota exceeded.']

#define server variable
server = smtplib.SMTP(smtp_server,port)

#END OF VARIABLES ===========================================



#MAIN SCRIPT ==========================================

#Get Email address input for the reciever
userInput = input('Reciever Email (if it is for gmail, you don\'t need to add @gmail.com)> ')

#check to see if @gmail.com is NOT in the reciever email input - if not, add it
gmailCheck = "@gmail.com"

for word in userInput:
	if word not in gmailCheck:
		userInput = userInput + "@gmail.com"


#commonly used email - type 'd' to use it - saved -- CHANGE IF YOU WANT A DEFAULT RECIEVER
if userInput == 'default':
	receiver_email = 'YOURDEFAULTEMAIL@gmail.com'

else:
	receiver_email = userInput

#Get Message input
message = input('Message> ')

#add an ending to the message
message = 'Hello! This is Bebo Bot! I am programmed in Python to send emails! MESSAGE> <' + message + '>'

#Amount of emails to send input
amount = input('Amount of emails to send> ')



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
      
      message = message + '  '
      #seeing if the 1st or 2nd email is signed in
      if botEmail == 0:
      	sendMessage()
      if botEmail == 1:
      	sendMessage_other()
      
      #Change the amount set to one number above so it can show the number email it is
      amount_sent = amount_sent + 1
      
      #append the random digit to the message
      
      #Print the message of the email with the number of which one it is (ex: 2. MESSAGE> Hello World)
      print(str(amount_sent) + '. MESSAGE> ' + message + '} SENT')
      
    #check if errors
    except Exception as e:
    	
    	#looking at the words in errorUnable
      for word in errorUnable:
      	#If the words are in the error
        if word in str(e):
          
          #calculating the amount of emails to send left
          amount = int(amount) - int(amount_sent)
          
          #check to see which account is logged in
          if botEmail == 0:
          	email_of_bot_string = 'main'
          if botEmail == 1:
          	email_of_bot_string = 'alt'
          
          #print error and ask which account
          altMain = input('Unable to send, sending limit on Gmail met on ' + email_of_bot_string + ' account. Log in with alt account or main? (a/m)> ')
          
          if altMain == 'a':
          	botEmail = 1
          	serverConnect_other()
          	send()
          if altMain == 'm':
          	botEmail = 0
          	serverConnect()
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
		print('Logged in with alternate account.')
		
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
		print('Logged in with main account.')
		
	except Exception as e:
		print(e)



#END OF FUNCTIONS ====================================================



#Connect to the SMTP Server
serverConnect()

#notify user on what is happening
print('Sending...')

#Call the sending function
send()



#COLCLUSION ===================================================

#once loop is finished, quit the SMTP server 
server.quit() 

#print how many emails sent to recipent
print('Sent ' + str(amount) + ' emails sucessfully.')

#Exit the script
exit()




