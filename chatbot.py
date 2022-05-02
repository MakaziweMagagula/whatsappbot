from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
#from gsheet_func import *

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    incoming = request.form.get('Body','').lower()
    #user = request.form.get('Body')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if len(incoming) > 1 :  
        resp.message("What do you think of my WhatsApp Questions application?")
        
    if 'a' or 'e' or 'i' or 'o' or 'u' in incoming:
        file = open("responses.txt","a")
        file.write(incoming +"\n")
        file.close()
        responded = True
        resp.message("If you want to continue enter 1 else enter 0 to exit")
    elif incoming == 0 and responded:
        resp.message("Thank you for the feedback! Have a Good day")
    if not responded:
        resp.message("What do you think of my WhatsApp Questions application?")
   
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)