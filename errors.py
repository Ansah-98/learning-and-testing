import traceback

try:
    raise Exception("this is the message")
except:
    message  = open('err.txt', 'w')
    message.write(traceback.format_exc())
    content = message
    message.close()

