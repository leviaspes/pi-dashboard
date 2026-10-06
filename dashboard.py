#!/usr/bin/env python3
"""
Minimalistic Tkinter Dashboard for Raspberry Pi 2
Displays time and date on LCD monitor with dark UI and light text
"""

import tkinter as tk
from datetime import datetime
import sys

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#1a1a1a')
        self.root.bind('<Escape>', self.quit_app)
        
        # Hide cursor
        self.root.config(cursor='none')
        
        # Main container
        main_frame = tk.Frame(root, bg='#1a1a1a')
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Time label
        self.time_label = tk.Label(
            main_frame,
            text='',
            font=('Arial', 200, 'bold'),
            fg='#e0e0e0',
            bg='#1a1a1a'
        )
        self.time_label.pack(pady=20, expand=True)
        
        # Date label
        self.date_label = tk.Label(
            main_frame,
            text='',
            font=('Arial', 75),
            fg='#a0a0a0',
            bg='#1a1a1a'
        )
        self.date_label.pack(pady=20, expand=True)
        
        # Start the update loop
        self.update_display()
    
    def update_display(self):
        """Update time and date every 1000ms (1 second)"""
        now = datetime.now()
        
        # Format time as HH:MM:SS
        time_str = now.strftime('%H:%M:%S')
        self.time_label.config(text=time_str)
        
        # Format date as Day, Month DD, YYYY
        date_str = now.strftime('%A, %B %d, %Y')
        self.date_label.config(text=date_str)
        
        # Schedule next update in 1000ms
        self.root.after(1000, self.update_display)
    
    def quit_app(self, event=None):
        """Exit the application"""
        self.root.quit()
        sys.exit(0)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Pi Dashboard')
    
    dashboard = Dashboard(root)
    root.mainloop()
