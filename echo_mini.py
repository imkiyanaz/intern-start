from datetime import datetime

def clock():
    return datetime.now().strftime("%H:%M")

def calc(a, b):
    return a + b

rules = {
    "hello": "سلام! من Echo-mini هستم 👋",
    "price": "مبلغ 10 دلار است",
    "help": "hello, price, time, add, name, bye",
    "name": "من یک Echo-mini هستم که خودم ساختم!"
}

print("Echo-mini روشن شد! برای خروج bye بنویس.")

while True:
    msg = input("تو: ").strip().lower()

    if msg == "bye":
        print("Echo-mini: خداحافظ 👋")
        break
    elif msg in rules:
        print("Echo-mini:", rules[msg])
    elif msg == "time":
        print("Echo-mini:", clock())
    elif msg == "add":
        print("Echo-mini:", calc(3, 5))
    else:
        print("Echo-mini: متوجه نشدم")