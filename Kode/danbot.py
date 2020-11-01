import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "THEREALTRUTH.BRITAIN@gmail.com"
receiver_email = "THEREALTRUTH.BRITAIN@gmail.com"
password = "og1flaskerom"
message = """ Subject: Hi there

This message is sent from Python."""
print("stage 1")

# Create a secure SSL context
context = ssl.create_default_context()
print("stage 2")
# Try to log in to server and send email
server = smtplib.SMTP(smtp_server, port)
print("stage 3")
try:
    server.ehlo() # Can be omitted
    print("stage 4.1")
    server.starttls(context=context) # Secure the connection
    print("stage 4.2")
    server.ehlo() # Can be omitted
    print("stage 4.3")
    server.login(sender_email, password)
    print("stage 4.4")
    for x in range(20):
        server.sendmail(sender_email, receiver_email, message + "{x}")
    
    print("stage 4.5")
except Exception as e:
    # Print any error messages to stdout
    print("stage 404")
    print(e)
finally:
    server.quit()
    print("stage 5")