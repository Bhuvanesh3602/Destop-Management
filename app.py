import threading
import speech_to_text
import text_to_speech
import action as a

try:
    from tkinter import *
    from tkinter import ttk
    from PIL import Image, ImageTk
    GUI_AVAILABLE = True
except ModuleNotFoundError:
    GUI_AVAILABLE = False

def on_enter(e, btn, hover_color):
    btn['background'] = hover_color

def on_leave(e, btn, original_color):
    btn['background'] = original_color

def ask_action():
    user_msg = entry.get().strip()
    if not user_msg:
        return
    
    text.config(state=NORMAL)
    text.insert(END, "You: " + user_msg + "\n", "user")
    text.see(END)
    text.config(state=DISABLED)
    entry.delete(0, END)
    threading.Thread(target=lambda: a.Action(user_msg)).start()

def send_action():
    ask_action()

def delete_text():
    text.config(state=NORMAL)
    text.delete("1.0", END)
    text.config(state=DISABLED)

def mic_action():
    if GUI_AVAILABLE:
        text.config(state=NORMAL)
        text.insert(END, "🎙 Listening...\n", "system")
        text.config(state=DISABLED)
        threading.Thread(target=listen_and_respond).start()
    else:
        print("Listening...")
        listen_and_respond()

def listen_and_respond():
    data = speech_to_text.recognize_speech_from_mic()
    text.config(state=NORMAL)
    text.insert(END, "You (mic): " + data + "\n", "user")
    text.config(state=DISABLED)
    text.see(END)
    a.Action(data)

if GUI_AVAILABLE:
    root = Tk()
    root.title("🤖 AI Desktop Assistant")
    root.geometry("700x800")
    root.resizable(False, False)
    root.config(bg="#0f0f1e")

    # Header Frame with Gradient Effect
    header_frame = Frame(root, bg="#1a1a2e", height=120)
    header_frame.pack(fill=X, pady=0)
    
    title_label = Label(header_frame, text="🤖 AI ASSISTANT", 
                       font=("Segoe UI", 28, "bold"), fg="#00d4ff", bg="#1a1a2e")
    title_label.pack(pady=15)
    
    subtitle_label = Label(header_frame, text="Your Personal Desktop Manager", 
                          font=("Segoe UI", 11), fg="#a0a0a0", bg="#1a1a2e")
    subtitle_label.pack()

    # Status Indicator
    status_frame = Frame(root, bg="#0f0f1e")
    status_frame.pack(pady=10)
    
    status_dot = Label(status_frame, text="●", font=("Arial", 20), fg="#00ff88", bg="#0f0f1e")
    status_dot.pack(side=LEFT, padx=5)
    
    status_label = Label(status_frame, text="Online & Ready", 
                        font=("Segoe UI", 10), fg="#00ff88", bg="#0f0f1e")
    status_label.pack(side=LEFT)

    # Chat Display Frame
    chat_frame = Frame(root, bg="#16213e", bd=0)
    chat_frame.pack(padx=30, pady=15, fill=BOTH, expand=True)
    
    # Scrollbar
    scrollbar = Scrollbar(chat_frame, bg="#1a1a2e", troughcolor="#0f0f1e")
    scrollbar.pack(side=RIGHT, fill=Y)
    
    text = Text(chat_frame, font=('Consolas', 11), bg="#16213e", fg="#ffffff", 
                wrap=WORD, bd=0, padx=15, pady=15, yscrollcommand=scrollbar.set,
                insertbackground="#00d4ff", selectbackground="#00d4ff", selectforeground="#000000")
    text.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text.yview)
    
    # Text tags for styling
    text.tag_config("user", foreground="#00d4ff", font=('Consolas', 11, 'bold'))
    text.tag_config("system", foreground="#00ff88", font=('Consolas', 11, 'italic'))
    text.config(state=DISABLED)

    # Input Frame
    input_frame = Frame(root, bg="#0f0f1e")
    input_frame.pack(padx=30, pady=10, fill=X)
    
    entry = Entry(input_frame, font=("Segoe UI", 13), bg="#1a1a2e", fg="#ffffff", 
                 insertbackground="#00d4ff", bd=0, relief=FLAT)
    entry.pack(fill=X, ipady=12, padx=2, pady=2)
    entry.bind('<Return>', lambda e: send_action())

    # Button Frame
    button_frame = Frame(root, bg="#0f0f1e")
    button_frame.pack(pady=20)
    
    btn_style = {
        "font": ("Segoe UI", 11, "bold"),
        "cursor": "hand2",
        "bd": 0,
        "relief": FLAT,
        "width": 12,
        "height": 2
    }
    
    # ASK Button
    btn_ask = Button(button_frame, text="💬 ASK", bg="#6c5ce7", fg="white", 
                    command=ask_action, activebackground="#5f4dd1", **btn_style)
    btn_ask.grid(row=0, column=0, padx=8)
    btn_ask.bind("<Enter>", lambda e: on_enter(e, btn_ask, "#5f4dd1"))
    btn_ask.bind("<Leave>", lambda e: on_leave(e, btn_ask, "#6c5ce7"))
    
    # SEND Button
    btn_send = Button(button_frame, text="📤 SEND", bg="#00b894", fg="white", 
                     command=send_action, activebackground="#00a383", **btn_style)
    btn_send.grid(row=0, column=1, padx=8)
    btn_send.bind("<Enter>", lambda e: on_enter(e, btn_send, "#00a383"))
    btn_send.bind("<Leave>", lambda e: on_leave(e, btn_send, "#00b894"))
    
    # MIC Button
    btn_mic = Button(button_frame, text="🎤 MIC", bg="#fd79a8", fg="white", 
                    command=mic_action, activebackground="#fc5c8d", **btn_style)
    btn_mic.grid(row=0, column=2, padx=8)
    btn_mic.bind("<Enter>", lambda e: on_enter(e, btn_mic, "#fc5c8d"))
    btn_mic.bind("<Leave>", lambda e: on_leave(e, btn_mic, "#fd79a8"))
    
    # DELETE Button
    btn_delete = Button(button_frame, text="🗑️ CLEAR", bg="#ff7675", fg="white", 
                       command=delete_text, activebackground="#ff5e5e", **btn_style)
    btn_delete.grid(row=0, column=3, padx=8)
    btn_delete.bind("<Enter>", lambda e: on_enter(e, btn_delete, "#ff5e5e"))
    btn_delete.bind("<Leave>", lambda e: on_leave(e, btn_delete, "#ff7675"))

    # Footer
    footer_label = Label(root, text="Powered by Python | Voice & Text Enabled", 
                        font=("Segoe UI", 9), fg="#555555", bg="#0f0f1e")
    footer_label.pack(pady=10)

    root.mainloop()
else:
    print("tkinter is not available in this Python environment. Running in CLI mode.")
    print("Type a message and press Enter. Type 'mic' to use the microphone (requires speech_recognition), or 'quit' to exit.")
    while True:
        try:
            inp = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print('\nExiting.')
            break
        if not inp:
            continue
        if inp.lower() == "quit":
            print("Goodbye")
            break
        if inp.lower() == "mic":
            print("Listening...")
            data = speech_to_text.recognize_speech_from_mic()
            print("You (mic):", data)
            a.Action(data)
            continue
        a.Action(inp)