import tkinter as tk
from tkinter import messagebox
import threading
import time

class CyberClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Clicker 2")
        self.root.geometry("800x600")  # Set default window size
        self.root.minsize(600, 400)  # Minimum size for responsiveness

        # Game state variables
        self.score = 0
        self.score_increment = 1
        self.auto_clicker_count = 0
        self.keyboard_count = 0
        self.sdcard_count = 0
        self.flash_drive_count = 0
        self.running = True

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        self.root.configure(bg="#e8ffe7")

        # Create a grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

        # Title
        title_label = tk.Label(self.root, text="Cyber Clicker 2", font=("Knewave", 24, "underline"), bg="#e8ffe7", fg="#3E3E3E")
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Score Display
        self.score_label = tk.Label(self.root, text=f"Computer Chips: {self.score}", font=("Arial", 14), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid", padx=10, pady=5)
        self.score_label.grid(row=1, column=0, pady=10, sticky="ew", padx=10)

        self.pps_label = tk.Label(self.root, text=f"Points per Second: 0", font=("Arial", 14), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid", padx=10, pady=5)
        self.pps_label.grid(row=1, column=2, pady=10, sticky="ew", padx=10)

        # Clicker Button
        self.clicker_button = tk.Button(self.root, text="Click Me!", font=("Arial", 16), bg="#20da29", fg="white", activebackground="#1d8b13", activeforeground="white", command=self.on_click)
        self.clicker_button.grid(row=1, column=1, pady=20)

        # Counts Display
        self.counts_frame = tk.Frame(self.root, bg="#e8ffe7")
        self.counts_frame.grid(row=2, column=0, padx=10, pady=10, sticky="n")

        self.auto_clicker_count_label = tk.Label(self.counts_frame, text=f"👆 Auto Clicker Count: {self.auto_clicker_count}", font=("Arial", 12), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid", padx=10, pady=5)
        self.auto_clicker_count_label.pack(pady=5)

        self.mouse_count_label = tk.Label(self.counts_frame, text=f"🖱️ Mouse Count: 0", font=("Arial", 12), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid", padx=10, pady=5)
        self.mouse_count_label.pack(pady=5)

        self.sdcard_count_label = tk.Label(self.counts_frame, text=f"💾 SD-Card Count: {self.sdcard_count}", font=("Arial", 12), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid", padx=10, pady=5)
        self.sdcard_count_label.pack(pady=5)

        self.keyboard_count_label = tk.Label(self.counts_frame, text=f"⌨️ Keyboard Count: {self.keyboard_count}", font=("Arial", 12), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid", padx=10, pady=5)
        self.keyboard_count_label.pack(pady=5)

        self.flash_drive_count_label = tk.Label(self.counts_frame, text=f"💽 30-Gig Flash-Drive Count: {self.flash_drive_count}", font=("Arial", 12), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid", padx=10, pady=5)
        self.flash_drive_count_label.pack(pady=5)

        # Upgrade Buttons
        self.upgrades_frame = tk.LabelFrame(self.root, text="Upgrades", font=("Arial", 14, "bold"), bg="#bffebd", fg="#1d8b13", bd=3, relief="solid")
        self.upgrades_frame.grid(row=2, column=2, padx=10, pady=10, sticky="n")

        self.auto_clicker_button = tk.Button(self.upgrades_frame, text="👆 Auto Clicker\n(50 Chips)", font=("Arial", 12), bg="#20da29", fg="white", activebackground="#1d8b13", activeforeground="white", command=lambda: self.purchase_upgrade(2))
        self.auto_clicker_button.grid(row=0, column=0, padx=10, pady=10)

        self.mouse_button = tk.Button(self.upgrades_frame, text="🖱️ Mouse\n(100 Chips)", font=("Arial", 12), bg="#20da29", fg="white", activebackground="#1d8b13", activeforeground="white", command=lambda: self.purchase_upgrade(1))
        self.mouse_button.grid(row=0, column=1, padx=10, pady=10)

        self.sdcard_button = tk.Button(self.upgrades_frame, text="💾 SD Card\n(350.5 Chips)", font=("Arial", 12), bg="#20da29", fg="white", activebackground="#1d8b13", activeforeground="white", command=lambda: self.purchase_upgrade(4))
        self.sdcard_button.grid(row=1, column=0, padx=10, pady=10)

        self.keyboard_button = tk.Button(self.upgrades_frame, text="⌨️ Keyboard\n(500.25 Chips)", font=("Arial", 12), bg="#20da29", fg="white", activebackground="#1d8b13", activeforeground="white", command=lambda: self.purchase_upgrade(3))
        self.keyboard_button.grid(row=1, column=1, padx=10, pady=10)

        self.flash_drive_button = tk.Button(self.upgrades_frame, text="💽 Flash Drive\n(2000 Chips)", font=("Arial", 12), bg="#20da29", fg="white", activebackground="#1d8b13", activeforeground="white", command=lambda: self.purchase_upgrade(5))
        self.flash_drive_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Quit Button
        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 12), bg="#ff6666", fg="white", activebackground="#cc0000", activeforeground="white", command=self.quit_game)
        self.quit_button.grid(row=3, column=1, pady=10)

        # Start auto-updating the game state
        self.update_game()

    def on_click(self):
        self.score += self.score_increment
        self.update_score_display()

    def update_score_display(self):
        self.score_label.config(text=f"Computer Chips: {self.score}")
        self.update_pps_display()

    def update_pps_display(self):
        total_pps = (0.5 * self.auto_clicker_count) + (3 * self.keyboard_count) + (2.32 * self.sdcard_count) + (10 * self.flash_drive_count)
        self.pps_label.config(text=f"Points per Second: {total_pps:.1f}")

    def purchase_upgrade(self, upgrade_type):
        if upgrade_type == 1 and self.score >= 100:
            self.score -= 100
            self.score_increment += 2
        elif upgrade_type == 2 and self.score >= 50:
            self.score -= 50
            self.auto_clicker_count += 1
        elif upgrade_type == 3 and self.score >= 500.25:
            self.score -= 500.25
            self.keyboard_count += 1
        elif upgrade_type == 4 and self.score >= 350.5:
            self.score -= 350.5
            self.sdcard_count += 1
        elif upgrade_type == 5 and self.score >= 2000:
            self.score -= 2000
            self.flash_drive_count += 1
        else:
            messagebox.showwarning("Not Enough Chips", "You don't have enough chips for this upgrade!")
        self.update_score_display()

    def auto_clicker_thread(self):
        while self.running:
            if self.auto_clicker_count > 0:
                self.score += 0.5 * self.auto_clicker_count
                self.update_score_display()
            time.sleep(1)

    def keyboard_thread(self):
        while self.running:
            if self.keyboard_count > 0:
                self.score += 3 * self.keyboard_count
                self.update_score_display()
            time.sleep(1)

    def sdcard_thread(self):
        while self.running:
            if self.sdcard_count > 0:
                self.score += 2.32 * self.sdcard_count
                self.update_score_display()
            time.sleep(1)

    def flash_drive_thread(self):
        while self.running:
            if self.flash_drive_count > 0:
                self.score += 10 * self.flash_drive_count
                self.update_score_display()
            time.sleep(1)

    def update_game(self):
        # Start background threads for upgrades
        threading.Thread(target=self.auto_clicker_thread, daemon=True).start()
        threading.Thread(target=self.keyboard_thread, daemon=True).start()
        threading.Thread(target=self.sdcard_thread, daemon=True).start()
        threading.Thread(target=self.flash_drive_thread, daemon=True).start()

    def quit_game(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberClicker(root)
    root.mainloop()
