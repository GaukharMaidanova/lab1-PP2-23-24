import datetime
current = datetime.datetime.today()
yesterday = current - datetime.timedelta(days=1)
tomorrow = current + datetime.timedelta(days=1)
print("Today: ", current)
print("Yesterday: ", yesterday)
print("Tomorrow: ", tomorrow)