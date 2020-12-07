import datetime

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

if 6 <= hour < 12:
    print("上午好，现在是{}点{}分".format(hour, minute))
elif 12 <= hour < 18:
    print("下午好，现在是{}点{}分".format(hour, minute))
elif 18 <= hour < 24:
    print("晚上好，现在是{}点{}分".format(hour, minute))

