import psutil
import os
import json
import threading
import time
from datetime import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import Meter
from tkinter import messagebox
import subprocess

# --- إعدادات ---
default_limit_mb = 250  # 250 جيجا
DATA_FILE = "data.json"
INTERFACE_NAME = "Ethernet"  # غيّر حسب الاتصال
CHECK_INTERVAL = 3  # تحديث كل 3 ثواني

program_location = os.path.dirname(__file__)

# --- حساب استهلاك النظام ---
def get_data_usage(interface):
    counters = psutil.net_io_counters(pernic=True)
    if interface in counters:
        stats = counters[interface]
        total_bytes = stats.bytes_sent + stats.bytes_recv
        return total_bytes / (1024 * 1024 * 1024)  # بالميغابايت
    return 0

#base = get_data_usage(INTERFACE_NAME)
#data = {
#    "base_total_mb": base,
#    "usage_mb": 0,
#    "limit_mb": default_limit_mb,
#    "start_date": datetime.now().strftime("%Y-%m-%d"),  
#    }

# --- تحميل/حفظ ---
def load_data():
    it_is = True
    while it_is:    
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
            it_is = False
        except (json.decoder.JSONDecodeError,KeyError):
        # أول مرة نشغل البرنامج
            save_data(data)
        except FileNotFoundError:
            print(program_location)
            subprocess.run(f"echo {data} > {program_location}/data.json", shell=True)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# --- قطع الإنترنت ---
def disable_network(interface):
    os.system(f'netsh interface set interface "{interface}" admin=disabled')

# --- المراقبة ---
def monitor_usage(meter: Meter):
    data = load_data()

    # حفظ القيمة الأساسية عند أول تشغيل
    if "base_total_mb" not in data:
        data["base_total_mb"] = get_data_usage(INTERFACE_NAME)
        save_data(data)

    while True:
        current_total = get_data_usage(INTERFACE_NAME)
        used = max(current_total - data["base_total_mb"])
        data["usage_mb"] = used
        save_data(data)

        percent = min((used / data["limit_mb"]) * 100, 100)

        meter.configure(
            amountused=used,
            amounttotal=data["limit_mb"],
            subtext=f"{used:.1f}MB من {data['limit_mb']}MB"
        )

        if used >= data["limit_mb"]:
            messagebox.showwarning("انتباه", "تم تجاوز الحد! سيتم قطع الإنترنت.")
            disable_network(INTERFACE_NAME)
            break

        time.sleep(CHECK_INTERVAL)

data = load_data()
used = int(data["usage_mb"] / 1000)
# --- الواجهة ---
def main():
    
    app = ttk.Window(title="مراقبة الإنترنت", themename="solar", size=(350, 400))

    ttk.Label(app, text="استهلاك الإنترنت", font=("Arial", 20)).pack(pady=10)

    meter = Meter(
        app,
        bootstyle=SECONDARY,
        interactive=False,
        textright="%",
        stripethickness=10,
        metersize=280,
        amountused=used,
        amounttotal=default_limit_mb
    )
    meter.pack(pady=20)

    #threading.Thread(target=monitor_usage, args=(meter,), daemon=True).start()

    app.mainloop()

if __name__ == "__main__":
    main()