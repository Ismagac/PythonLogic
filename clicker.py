import pyautogui
import keyboard
import time
import threading
import sys
from tkinter import Tk, Label, Button, Scale, Frame, StringVar, OptionMenu, Checkbutton, IntVar, Entry

class AutoClicker:
    def __init__(self):
        self.running = False
        self.click_thread = None
        self.click_count = 0
        self.paused = False
        
        # Configuraciones predeterminadas
        self.cps = 10  # clicks por segundo
        self.button = "left"  # botón del mouse para hacer clic
        self.fixed_position = False
        self.x_pos = 0
        self.y_pos = 0
        
        # Teclas de acceso rápido
        self.start_key = "f6"
        self.stop_key = "f7"
        self.pause_key = "f8"
        
        # Registrar teclas de acceso rápido
        keyboard.add_hotkey(self.start_key, self.toggle_clicking)
        keyboard.add_hotkey(self.stop_key, self.stop_clicking)
        keyboard.add_hotkey(self.pause_key, self.toggle_pause)
        
    def click(self):
        while self.running:
            if not self.paused:
                if self.fixed_position:
                    pyautogui.click(self.x_pos, self.y_pos, button=self.button)
                else:
                    pyautogui.click(button=self.button)
                
                self.click_count += 1
                
            time.sleep(1.0 / self.cps)
    
    def start_clicking(self):
        if not self.running:
            self.running = True
            self.click_thread = threading.Thread(target=self.click)
            self.click_thread.daemon = True
            self.click_thread.start()
            print(f"Auto-clicker iniciado. CPS: {self.cps}")
    
    def stop_clicking(self):
        self.running = False
        if self.click_thread and self.click_thread.is_alive():
            self.click_thread.join(timeout=1)
        print(f"Auto-clicker detenido. Clics totales: {self.click_count}")
    
    def toggle_clicking(self):
        if not self.running:
            self.start_clicking()
        else:
            self.stop_clicking()
    
    def toggle_pause(self):
        self.paused = not self.paused
        print("Auto-clicker pausado" if self.paused else "Auto-clicker reanudado")
    
    def set_cps(self, cps):
        self.cps = float(cps)
        print(f"CPS establecido a {self.cps}")
    
    def set_button(self, button):
        self.button = button
        print(f"Botón del mouse establecido a {self.button}")
    
    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y
        print(f"Posición de clic establecida en ({self.x_pos}, {self.y_pos})")

class AutoClickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")
        self.root.geometry("300x400")
        
        self.clicker = AutoClicker()
        
        # Marco para CPS
        cps_frame = Frame(root)
        cps_frame.pack(pady=10, fill="x", padx=20)
        
        Label(cps_frame, text="Clics por segundo:").pack(anchor="w")
        
        self.cps_scale = Scale(cps_frame, from_=0.1, to=20, resolution=0.1, orient="horizontal")
        self.cps_scale.set(self.clicker.cps)
        self.cps_scale.pack(fill="x")
        self.cps_scale.bind("<ButtonRelease-1>", self.update_cps)
        
        # Marco para botón del mouse
        button_frame = Frame(root)
        button_frame.pack(pady=10, fill="x", padx=20)
        
        Label(button_frame, text="Botón del mouse:").pack(anchor="w")
        
        self.button_var = StringVar(root)
        self.button_var.set(self.clicker.button)
        
        button_options = ["left", "right", "middle"]
        button_menu = OptionMenu(button_frame, self.button_var, *button_options, command=self.update_button)
        button_menu.pack(fill="x")
        
        # Marco para control de posición
        pos_frame = Frame(root)
        pos_frame.pack(pady=10, fill="x", padx=20)
        
        self.fixed_pos_var = IntVar()
        
        Checkbutton(pos_frame, text="Usar posición fija", variable=self.fixed_pos_var, 
                   command=self.toggle_fixed_position).pack(anchor="w")
        
        pos_input_frame = Frame(pos_frame)
        pos_input_frame.pack(fill="x", pady=5)
        
        Label(pos_input_frame, text="X:").pack(side="left")
        self.x_entry = Entry(pos_input_frame, width=6)
        self.x_entry.pack(side="left", padx=5)
        self.x_entry.insert(0, "0")
        
        Label(pos_input_frame, text="Y:").pack(side="left")
        self.y_entry = Entry(pos_input_frame, width=6)
        self.y_entry.pack(side="left", padx=5)
        self.y_entry.insert(0, "0")
        
        Button(pos_frame, text="Obtener posición actual", command=self.get_current_position).pack(fill="x", pady=5)
        
        # Marco para botones de control
        control_frame = Frame(root)
        control_frame.pack(pady=10, fill="x", padx=20)
        
        Button(control_frame, text="Iniciar (F6)", command=self.start_clicking).pack(fill="x", pady=2)
        Button(control_frame, text="Detener (F7)", command=self.stop_clicking).pack(fill="x", pady=2)
        Button(control_frame, text="Pausar/Reanudar (F8)", command=self.toggle_pause).pack(fill="x", pady=2)
        
        # Marco para contador de clics
        counter_frame = Frame(root)
        counter_frame.pack(pady=10, fill="x", padx=20)
        
        self.counter_var = StringVar()
        self.counter_var.set("Clics: 0")
        Label(counter_frame, textvariable=self.counter_var).pack()
        
        # Actualizar contador periódicamente
        self.update_counter()
        
    def update_cps(self, event=None):
        self.clicker.set_cps(self.cps_scale.get())
        
    def update_button(self, button):
        self.clicker.set_button(button)
        
    def toggle_fixed_position(self):
        if self.fixed_pos_var.get() == 1:
            self.set_position()
        else:
            self.clicker.fixed_position = False
            
    def get_current_position(self):
        x, y = pyautogui.position()
        self.x_entry.delete(0, 'end')
        self.x_entry.insert(0, str(x))
        self.y_entry.delete(0, 'end')
        self.y_entry.insert(0, str(y))
        self.set_position()
        
    def set_position(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            self.clicker.set_position(x, y)
            self.clicker.fixed_position = True
            self.fixed_pos_var.set(1)
        except ValueError:
            print("Valores de posición inválidos")
            
    def start_clicking(self):
        self.clicker.start_clicking()
        
    def stop_clicking(self):
        self.clicker.stop_clicking()
        
    def toggle_pause(self):
        self.clicker.toggle_pause()
        
    def update_counter(self):
        self.counter_var.set(f"Clics: {self.clicker.click_count}")
        self.root.after(100, self.update_counter)

if __name__ == "__main__":
    # Necesitas instalar estas dependencias:
    # pip install pyautogui keyboard
    try:
        root = Tk()
        app = AutoClickerGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")