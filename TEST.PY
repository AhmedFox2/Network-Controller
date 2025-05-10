import json
import psutil
import tkinter as tk
import ttkbootstrap as ttk

# إجمالي سعة الإنترنت المتاحة (بالجيجابايت)
TOTAL_GB = 250

# ملف لحفظ الاستخدام
json_file = "internet_usage.json"

# تحميل البيانات من الملف إذا كانت موجودة
def load_data():
    try:
        with open(json_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"gb_sent": 0, "gb_received": 0, "gb_total_used": 0}

# حفظ البيانات في الملف
def save_data(data):
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

# تحديث استخدام الإنترنت
def update_usage():
    net_io = psutil.net_io_counters()
    
    # تحويل البيانات إلى جيجابايت
    data["gb_sent"] = net_io.bytes_sent / (1024 ** 3)
    data["gb_received"] = net_io.bytes_recv / (1024 ** 3)
    data["gb_total_used"] = data["gb_sent"] + data["gb_received"]
    
    save_data(data)
    update_meter()

# تحديث meter في الواجهة
def update_meter():
    remaining_gb = max(0, TOTAL_GB - data["gb_total_used"])

    meter['amountused'] = data["gb_total_used"]
    meter.configure(subtext=f"Remaining: {remaining_gb:.2f} GB")
    
    root.after(1000, update_usage)  # تحديث كل ثانية

# تحميل البيانات الأولية
data = load_data()

# إنشاء الواجهة
root = ttk.Window(themename="solar")
root.title("مراقبة استخدام الإنترنت")
root.geometry("400x400")

meter = ttk.Meter(root, metersize=280, amountused=data["gb_total_used"], amounttotal=TOTAL_GB, subtext=f"Remaining: {TOTAL_GB - data["gb_total_used"]} GB", interactive=False, stripethickness=10)
meter.pack(pady=55)

# بدء التحديث
#update_usage()

root.mainloop()