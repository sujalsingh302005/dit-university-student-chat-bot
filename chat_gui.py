import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import subprocess
import requests
import json
import queue

# =====================================
# FAST + SMART MODEL
# =====================================
MODEL = "mistral"

# =====================================
# VOICE QUEUE (NO OVERLAP)
# =====================================
speech_queue = queue.Queue()

def speech_worker():
    while True:
        text = speech_queue.get()
        subprocess.run(["say", "-v", "Alex", text])
        speech_queue.task_done()

threading.Thread(target=speech_worker, daemon=True).start()

def speak(text):
    speech_queue.put(text)

# =====================================
# AI RESPONSE
# =====================================
def stream_ai(user_input):

    prompt = f"""
You are DIT University (Dehradun Institute of Technology) Student Assistant.

Answer clearly and naturally.
Reply ONLY to the user message.
Do not repeat yourself.

User: {user_input}
Assistant:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": True,
            "options": {
                "num_predict": 80,
                "temperature": 0.6
            }
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode())
            yield data.get("response", "")

# =====================================
# UI — CLEAN LIGHT MODE
# =====================================
root = tk.Tk()
root.title("DIT University Student Chat Bot")
root.geometry("650x750")
root.configure(bg="white")

header = tk.Label(
    root,
    text="DIT University Student Chat Bot",
    font=("Helvetica",18,"bold"),
    bg="#f1f5f9",
    fg="black",
    pady=15
)
header.pack(fill=tk.X)

chat = ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Helvetica",12),
    bg="white",
    fg="black",
    insertbackground="black",
    bd=0
)
chat.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
chat.config(state=tk.DISABLED)

# USER BUBBLE
chat.tag_config(
    "user",
    background="#2563eb",
    foreground="white",
    lmargin1=220,
    lmargin2=220,
    spacing1=12,
    spacing3=18
)

# BOT BUBBLE
chat.tag_config(
    "bot",
    background="#e5e7eb",
    foreground="black",
    lmargin1=10,
    lmargin2=10,
    spacing1=12,
    spacing3=18
)

# =====================================
# MESSAGE DISPLAY
# =====================================
def add_user(msg):
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, "\nYou:\n"+msg+"\n", "user")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

def add_bot(text):
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, "\nDIT Assistant:\n"+text+"\n", "bot")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

# =====================================
# BOT REPLY
# =====================================
def bot_reply(msg):

    add_user(msg)

    sentence_buffer = ""

    for token in stream_ai(msg):

        sentence_buffer += token

        if "." in sentence_buffer:
            end = sentence_buffer.find(".") + 1
            sentence = sentence_buffer[:end]

            speak(sentence)
            add_bot(sentence)

            sentence_buffer = sentence_buffer[end:]

    if sentence_buffer.strip():
        speak(sentence_buffer)
        add_bot(sentence_buffer)

# =====================================
# SEND MESSAGE
# =====================================
def send(event=None):

    msg = entry.get().strip()
    if not msg:
        return

    entry.delete(0, tk.END)

    threading.Thread(
        target=bot_reply,
        args=(msg,),
        daemon=True
    ).start()

# =====================================
# INPUT AREA
# =====================================
bottom = tk.Frame(root, bg="#f1f5f9")
bottom.pack(fill=tk.X, pady=10)

entry = tk.Entry(
    bottom,
    font=("Helvetica",13),
    bg="white",
    fg="black",
    insertbackground="black",
    relief="solid",
    bd=1
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, ipady=10)
entry.bind("<Return>", send)

send_btn = tk.Button(
    bottom,
    text="Send",
    command=send,
    bg="#2563eb",
    fg="white",
    font=("Helvetica",12,"bold"),
    relief="flat",
    padx=15
)
send_btn.pack(side=tk.RIGHT, padx=10)

root.mainloop()