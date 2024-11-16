import tkinter as tk
import datetime
import threading
import sys
import winsound
from tkinter import messagebox

class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Uygulaması")

        # GUI bileşenleri
        self.time_label = tk.Label(root, text="Alarm Zamanı (dd.mm.yyyy HH:MM:SS):", font=("Helvetica", 12))
        self.time_label.pack(pady=5)

        self.time_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.time_entry.pack(pady=5)

        self.message_label = tk.Label(root, text="Alarm Açıklaması:", font=("Helvetica", 12))
        self.message_label.pack(pady=5)

        self.message_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.message_entry.pack(pady=5)

        self.set_button = tk.Button(root, text="Alarm Kur", command=self.alarm_kur, font=("Helvetica", 12))
        self.set_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Çıkış", command=self.cikis, font=("Helvetica", 12))
        self.exit_button.pack(pady=10)

        self.alarm_thread = None

    def alarm_kur(self):
        alarm_zamani_str = self.time_entry.get()
        try:
            alarm_zamani = datetime.datetime.strptime(alarm_zamani_str, "%d.%m.%Y %H:%M:%S")
            alarm_aciklamasi = self.message_entry.get()
            self.alarm_thread = threading.Thread(target=self.alarm_cal, args=(alarm_zamani, alarm_aciklamasi))
            self.alarm_thread.start()
            messagebox.showinfo("Alarm Kuruldu", f"Alarm kuruldu:\n{alarm_zamani_str}\nMesaj: {alarm_aciklamasi}")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir tarih ve saat formatı girin (dd.mm.yyyy HH:MM:SS)")

    def alarm_cal(self, alarm_zamani, alarm_aciklamasi):
        while True:
            suan = datetime.datetime.now()
            if suan >= alarm_zamani:
                messagebox.showinfo("Alarm", f"Alarm Zamanı Geldi!\n{alarm_aciklamasi}")
                winsound.Beep(440, 2000)  # 440 Hz frekansta 2 saniyelik bir bip sesi
                break

    def cikis(self):
        if self.alarm_thread and self.alarm_thread.is_alive():
            messagebox.showwarning("Uyarı", "Çıkış yapmadan önce alarm thread'ini sonlandırın.")
        else:
            self.root.destroy()

root = tk.Tk()
app = AlarmApp(root)
root.mainloop()
