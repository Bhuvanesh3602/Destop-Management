import threading
import speech_to_text
import text_to_speech
import action as a

try:
    from tkinter import *
    from PIL import Image, ImageTk
    GUI_AVAILABLE = True
except ModuleNotFoundError:
    GUI_AVAILABLE = False
def ask_action():
    user_msg = entry.get().strip()
    if not user_msg:
        return
    
    text.config(state=NORMAL)
    text.insert(END, "You: " + user_msg + "\n")
    text.see(END)
    text.config(state=DISABLED)
    entry.delete(0, END)

    # Run voice logic in a thread
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
        text.insert(END, "🎙 Listening...\n")
        text.config(state=DISABLED)
        threading.Thread(target=listen_and_respond).start()
    else:

        print("Listening...")
        listen_and_respond()

def listen_and_respond():

    data = speech_to_text.recognize_speech_from_mic()
    text.config(state=NORMAL)
    text.insert(END, "You (mic): " + data + "\n")
    text.config(state=DISABLED)
    text.see(END)

    a.Action(data)
if GUI_AVAILABLE:

    root = Tk()
    root.title("AI Assistant")
    root.geometry("550x675")
    root.resizable(False, False)
    root.config(bg="#6F8FAF")

    frame = LabelFrame(root, padx=30, pady=15, borderwidth=3, relief="raised", bg="#BFD7ED")
    frame.pack(pady=20)

    title_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 18, "bold"), fg="#356696", bg="#BFD7ED")
    title_label.pack(pady=10)

    try:
        img = Image.open(r"image/Screenshot 2024-11-21 220903.png")
        img = img.resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        image_label = Label(frame, image=photo, bg="#BFD7ED")
        image_label.photo = photo
        image_label.pack(pady=10)
    except Exception:

        pass

    text = Text(root, font=('Courier', 10, 'bold'), bg="#356696", fg="white", wrap=WORD)
    text.place(x=85, y=380, width=380, height=100)
    text.config(state=DISABLED)

    entry = Entry(root, justify=CENTER, font=("Arial", 12))
    entry.place(x=100, y=500, width=350, height=30)

    btn_width = 120
    btn_height = 45
    gap = 20
    start_x = (550 - (4*btn_width + 3*gap)) // 2  

    Button1 = Button(root, text="ASK", bg="#356696", fg="white", font=("Arial", 12, "bold"),
                     command=ask_action, cursor="hand2", borderwidth=3, relief=SOLID)
    Button1.place(x=start_x, y=560, width=btn_width, height=btn_height)

    Button2 = Button(root, text="SEND", bg="#356696", fg="white", font=("Arial", 12, "bold"),
                     command=send_action, cursor="hand2", borderwidth=3, relief=SOLID)
    Button2.place(x=start_x + btn_width + gap, y=560, width=btn_width, height=btn_height)

    Button3 = Button(root, text="DELETE", bg="#356696", fg="white", font=("Arial", 12, "bold"),
                     command=delete_text, cursor="hand2", borderwidth=3, relief=SOLID)
    Button3.place(x=start_x + 2*(btn_width + gap), y=560, width=btn_width, height=btn_height)

    Button4 = Button(root, text="🎤 MIC", bg="#356696", fg="white", font=("Arial", 12, "bold"),
                     command=mic_action, cursor="hand2", borderwidth=3, relief=SOLID)
    Button4.place(x=start_x + 3*(btn_width + gap), y=560, width=btn_width, height=btn_height)

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
        # Regular text input
        a.Action(inp)