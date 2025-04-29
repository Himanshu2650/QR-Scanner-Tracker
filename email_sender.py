import smtplib
from email.message import EmailMessage

def send_email(attachment_path):
    msg = EmailMessage()
    msg['Subject'] = 'Walk Tracker Report'
    msg['From'] = 'himanshukumaranand3670@gmail.com'
    msg['To'] = ["thakuranand2650@gmail.com"]

    msg.set_content('Please find attached the walk tracker report.')

    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename='WalkReport.pdf')

    # Using TLS (recommended)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('himanshukumaranand3670@gmail.com', 'ocki cuvx xlxp phva')
        smtp.send_message(msg)




# import os
# import smtplib
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# def send_email(attachment_path):
#     subject ="QR Code Based Guard Patrol Report"

        
#     sender_email = " "
#     receiver_To_email = [" "]
        
#     # Create a multipart message and set headers
#     rcpt = receiver_To_email 
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = ",".join(receiver_To_email)
#     msg["Subject"] = subject

#     part=MIMEText("Attached herewith is the QR Code Based Guard Patrol Report for your reference.")
#     msg.attach(part)

#     try:
#         with open(attachment_path, "rb") as attachment:
#             part = MIMEBase("application", "octet-stream")
#             part.set_payload(attachment.read())
#             encoders.encode_base64(part)
#             part.add_header(
#                 "Content-Disposition",
#                 f"attachment; filename= {os.path.basename(attachment_path)}",
#             )
#             msg.attach(part)
#     except Exception as e:
#         print(f"Error attaching file: {e}")
#         return
            
#     text = msg.as_string()
#     server = smtplib.SMTP("kdcvgaweb02d.corp.bharatpetroleum.com", 25)
#     server.connect("kdcvgaweb02d.corp.bharatpetroleum.com",25)
        
#     server.sendmail(sender_email, rcpt, text)
#     server.quit()
    