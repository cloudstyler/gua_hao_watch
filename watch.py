import os, requests, datetime
url = "https://www.bczyyy.com/api/registration/freeClinicLeftNum"
sckey = os.getenv("SCKEY")
try:
    slots = requests.get(url, timeout=5).json().get("data", {})
except Exception as e:
    slots = {"error": str(e)}
msg = f"{datetime.datetime.now():%m-%d %H:%M} 无号"
for day, (left, total) in slots.items():
    if left > 0:
        msg = f"{day} 有号！剩余 {left}/{total}"
if sckey:
    requests.get(f"https://sctapi.ftqq.com/{sckey}.send", params={"title":"义诊室提醒","desp":msg})
print(msg)