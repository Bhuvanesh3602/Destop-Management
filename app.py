import threading
import speech_to_text
import text_to_speech
import action as a
import datetime
import time

try:
    from tkinter import *
    from tkinter import ttk, messagebox
    from PIL import Image, ImageTk
    GUI_AVAILABLE = True
except ModuleNotFoundError:
    GUI_AVAILABLE = False

is_listening = False

def animate_status():
    colors = ["#00ff88", "#00dd77", "#00bb66", "#00dd77"]
    idx = 0
    while True:
        if is_listening:
            status_dot.config(fg=colors[idx % len(colors)])
            status_label.config(text="🎤 Listening...", fg=colors[idx % len(colors)])
        else:
            status_dot.config(fg="#00ff88")
            status_label.config(text="✓ Online & Ready", fg="#00ff88")
        idx += 1
        time.sleep(0.3)
        root.update()

def update_time():
    current = datetime.datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text=current)
    root.after(1000, update_time)

def on_enter(e, btn, hover_color):
    btn['background'] = hover_color
    btn['font'] = ("Segoe UI", 12, "bold")

def on_leave(e, btn, original_color):
    btn['background'] = original_color
    btn['font'] = ("Segoe UI", 11, "bold")

def ask_action():
    user_msg = entry.get().strip()
    if not user_msg:
        messagebox.showwarning("Empty Input", "Please type a message!")
        return
    
    text.config(state=NORMAL)
    text.insert(END, "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", "separator")
    text.insert(END, "👤 You: ", "user_label")
    text.insert(END, user_msg + "\n", "user")
    text.see(END)
    text.config(state=DISABLED)
    entry.delete(0, END)
    threading.Thread(target=lambda: a.Action(user_msg)).start()

def send_action():
    ask_action()

def delete_text():
    result = messagebox.askyesno("Clear Chat", "Are you sure you want to clear the chat?")
    if result:
        text.config(state=NORMAL)
        text.delete("1.0", END)
        text.insert(END, "🤖 Chat cleared. How can I help you?\n", "assistant")
        text.config(state=DISABLED)

def mic_action():
    global is_listening
    if GUI_AVAILABLE:
        is_listening = True
        text.config(state=NORMAL)
        text.insert(END, "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", "separator")
        text.insert(END, "🎙️ Listening... Speak now!\n", "system")
        text.config(state=DISABLED)
        threading.Thread(target=listen_and_respond).start()
    else:
        print("Listening...")
        listen_and_respond()

def listen_and_respond():
    global is_listening
    data = speech_to_text.recognize_speech_from_mic()
    is_listening = False
    text.config(state=NORMAL)
    text.insert(END, "👤 You (mic): ", "user_label")
    text.insert(END, data + "\n", "user")
    text.config(state=DISABLED)
    text.see(END)
    a.Action(data)

def show_help():
    help_text = """🎯 QUICK COMMANDS:
    
• Say 'Hello' or 'Hi'
• Ask 'What time is it?'
• Say 'Open YouTube'
• Say 'Tell me a joke'
• Say 'Search Python'
• Say 'Open Calculator'
• Say 'What is the date?'
    
Press MIC button and speak!"""
    messagebox.showinfo("Help - Voice Commands", help_text)

def show_about():
    about_text = """🤖 AI Desktop Assistant v2.0
    
A powerful voice-enabled desktop manager
built with Python.

Features:
✓ Voice Recognition
✓ Text-to-Speech
✓ Web Automation
✓ System Control
✓ Smart Commands

Developed with ❤️ using Python"""
    messagebox.showinfo("About", about_text)

if GUI_AVAILABLE:
    root = Tk()
    root.title("🤖 AI Desktop Assistant Pro")
    root.geometry("900x850")
    root.resizable(False, False)
    root.config(bg="#0a0a0f")

    # Top Menu Bar
    menu_bar = Frame(root, bg="#1a1a2e", height=40)
    menu_bar.pack(fill=X)
    
    menu_label = Label(menu_bar, text="☰ MENU", font=("Segoe UI", 10, "bold"), 
                      fg="#00d4ff", bg="#1a1a2e", cursor="hand2")
    menu_label.pack(side=LEFT, padx=20, pady=8)
    
    help_btn = Label(menu_bar, text="❓ Help", font=("Segoe UI", 10), 
                    fg="#ffffff", bg="#1a1a2e", cursor="hand2")
    help_btn.pack(side=RIGHT, padx=10, pady=8)
    help_btn.bind("<Button-1>", lambda e: show_help())
    
    about_btn = Label(menu_bar, text="ℹ️ About", font=("Segoe UI", 10), 
                     fg="#ffffff", bg="#1a1a2e", cursor="hand2")
    about_btn.pack(side=RIGHT, padx=10, pady=8)
    about_btn.bind("<Button-1>", lambda e: show_about())
    
    time_label = Label(menu_bar, text="", font=("Segoe UI", 10), 
                      fg="#00ff88", bg="#1a1a2e")
    time_label.pack(side=RIGHT, padx=20, pady=8)

    # Header Frame
    header_frame = Frame(root, bg="#1a1a2e", height=100)
    header_frame.pack(fill=X)
    
    title_label = Label(header_frame, text="🤖 AI ASSISTANT PRO", 
                       font=("Segoe UI", 32, "bold"), fg="#00d4ff", bg="#1a1a2e")
    title_label.pack(pady=10)
    
    subtitle_label = Label(header_frame, text="Your Intelligent Desktop Manager | Voice & Text Enabled", 
                          font=("Segoe UI", 11), fg="#a0a0a0", bg="#1a1a2e")
    subtitle_label.pack()

    # Status Bar
    status_frame = Frame(root, bg="#16213e", height=40)
    status_frame.pack(fill=X, pady=5)
    
    status_dot = Label(status_frame, text="●", font=("Arial", 16), fg="#00ff88", bg="#16213e")
    status_dot.pack(side=LEFT, padx=20)
    
    status_label = Label(status_frame, text="✓ Online & Ready", 
                        font=("Segoe UI", 10, "bold"), fg="#00ff88", bg="#16213e")
    status_label.pack(side=LEFT)
    
    version_label = Label(status_frame, text="v2.0", 
                         font=("Segoe UI", 9), fg="#666666", bg="#16213e")
    version_label.pack(side=RIGHT, padx=20)

    # Chat Container
    chat_container = Frame(root, bg="#0a0a0f")
    chat_container.pack(padx=25, pady=10, fill=BOTH, expand=True)
    
    # Chat Display Frame
    chat_frame = Frame(chat_container, bg="#16213e", bd=2, relief=RIDGE)
    chat_frame.pack(fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(chat_frame, bg="#1a1a2e", troughcolor="#0f0f1e", width=15)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    text = Text(chat_frame, font=('Consolas', 11), bg="#16213e", fg="#ffffff", 
                wrap=WORD, bd=0, padx=20, pady=20, yscrollcommand=scrollbar.set,
                insertbackground="#00d4ff", selectbackground="#00d4ff", 
                selectforeground="#000000", spacing1=5, spacing3=5)
    text.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text.yview)
    
    # Text styling tags
    text.tag_config("user", foreground="#00d4ff", font=('Consolas', 11))
    text.tag_config("user_label", foreground="#00d4ff", font=('Consolas', 12, 'bold'))
    text.tag_config("system", foreground="#00ff88", font=('Consolas', 11, 'italic'))
    text.tag_config("assistant", foreground="#ffd700", font=('Consolas', 11, 'bold'))
    text.tag_config("separator", foreground="#333333")
    
    text.insert(END, "🤖 Welcome to AI Assistant Pro!\n", "assistant")
    text.insert(END, "Type a message or click MIC to speak...\n\n", "system")
    text.config(state=DISABLED)

    # Input Container
    input_container = Frame(root, bg="#0a0a0f")
    input_container.pack(padx=25, pady=10, fill=X)
    
    input_frame = Frame(input_container, bg="#1a1a2e", bd=2, relief=RIDGE)
    input_frame.pack(fill=X)
    
    entry = Entry(input_frame, font=("Segoe UI", 13), bg="#1a1a2e", fg="#ffffff", 
                 insertbackground="#00d4ff", bd=0, relief=FLAT)
    entry.pack(fill=X, ipady=15, padx=15, pady=10)
    entry.bind('<Return>', lambda e: send_action())
    entry.focus()

    # Button Container
    button_container = Frame(root, bg="#0a0a0f")
    button_container.pack(pady=15)
    
    # Row 1 Buttons
    btn_row1 = Frame(button_container, bg="#0a0a0f")
    btn_row1.pack(pady=5)
    
    btn_style = {
        "font": ("Segoe UI", 11, "bold"),
        "cursor": "hand2",
        "bd": 0,
        "relief": FLAT,
        "width": 14,
        "height": 2
    }
    
    btn_send = Button(btn_row1, text="📤 SEND", bg="#00b894", fg="white", 
                     command=send_action, activebackground="#00a383", **btn_style)
    btn_send.grid(row=0, column=0, padx=10)
    btn_send.bind("<Enter>", lambda e: on_enter(e, btn_send, "#00a383"))
    btn_send.bind("<Leave>", lambda e: on_leave(e, btn_send, "#00b894"))
    
    btn_mic = Button(btn_row1, text="🎤 VOICE", bg="#fd79a8", fg="white", 
                    command=mic_action, activebackground="#fc5c8d", **btn_style)
    btn_mic.grid(row=0, column=1, padx=10)
    btn_mic.bind("<Enter>", lambda e: on_enter(e, btn_mic, "#fc5c8d"))
    btn_mic.bind("<Leave>", lambda e: on_leave(e, btn_mic, "#fd79a8"))
    
    btn_delete = Button(btn_row1, text="🗑️ CLEAR", bg="#ff7675", fg="white", 
                       command=delete_text, activebackground="#ff5e5e", **btn_style)
    btn_delete.grid(row=0, column=2, padx=10)
    btn_delete.bind("<Enter>", lambda e: on_enter(e, btn_delete, "#ff5e5e"))
    btn_delete.bind("<Leave>", lambda e: on_leave(e, btn_delete, "#ff7675"))
    
    btn_help = Button(btn_row1, text="❓ HELP", bg="#6c5ce7", fg="white", 
                     command=show_help, activebackground="#5f4dd1", **btn_style)
    btn_help.grid(row=0, column=3, padx=10)
    btn_help.bind("<Enter>", lambda e: on_enter(e, btn_help, "#5f4dd1"))
    btn_help.bind("<Leave>", lambda e: on_leave(e, btn_help, "#6c5ce7"))

    # Footer
    footer_frame = Frame(root, bg="#1a1a2e", height=35)
    footer_frame.pack(fill=X, side=BOTTOM)
    
    footer_label = Label(footer_frame, text="⚡ Powered by Python | 🎤 Voice Enabled | 🔒 100% Local", 
                        font=("Segoe UI", 9), fg="#666666", bg="#1a1a2e")
    footer_label.pack(pady=8)

    # Start time update
    update_time()
    
    root.mainloop()
else:
    print("="*50)
    print("🤖 AI ASSISTANT - CLI MODE")
    print("="*50)
    print("Commands: 'mic' for voice | 'quit' to exit")
    print("="*50)
    while True:
        try:
            inp = input("\n👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print('\n👋 Exiting. Goodbye!')
            break
        if not inp:
            continue
        if inp.lower() == "quit":
            print("👋 Goodbye!")
            break
        if inp.lower() == "mic":
            print("🎤 Listening...")
            data = speech_to_text.recognize_speech_from_mic()
            print(f"👤 You (mic): {data}")
            a.Action(data)
            continue
        a.Action(inp)