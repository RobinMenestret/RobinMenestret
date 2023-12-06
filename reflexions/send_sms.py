from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf3e59f37af44b087c77765894e615229"
# Your Auth Token from twilio.com/console
auth_token  = "4c46e633a914a940e110bc9ba902a6e3"

client = Client(account_sid, auth_token)

# c'est le numéro de test de la sandbox WhatsApp
from_whatsapp_number='whatsapp:+14155238886' 
# remplacez ce numéro avec votre propre numéro WhatsApp
to_whatsapp_number='whatsapp:+33608156468' 
client.messages.create(
    body="lalllalalalalalalalalal", 
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

#whatsapp:+33626283719