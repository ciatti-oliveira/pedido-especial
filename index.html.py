import tkinter as tk
import random

# --- Janela principal ---
root = tk.Tk()
root.title("Pedido especial 💕")
root.geometry("500x400")
root.configure(bg="#ffc8e0")
root.resizable(False, False)

# --- Pergunta ---
label = tk.Label(
    root,
    text="Quer namorar comigo?",
    font=("Poppins", 20, "bold"),
    bg="#ffc8e0",
    fg="#3a1a2a",
)
label.pack(pady=60)

# --- Botão "Sim" ---
def clicou_sim():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(
        root,
        text="Eu sabia! 💖",
        font=("Poppins", 24, "bold"),
        bg="#ffc8e0",
        fg="#3a1a2a",
    ).pack(expand=True)

btn_sim = tk.Button(
    root,
    text="Sim",
    font=("Arial", 12, "bold"),
    bg="#f4a3b8",
    command=clicou_sim,
)
btn_sim.place(x=170, y=200, width=70, height=35)

# --- Botão "Não" (foge do mouse) ---
btn_nao = tk.Button(
    root,
    text="Não",
    font=("Arial", 12, "bold"),
    bg="#f4a3b8",
)
btn_nao.place(x=270, y=200, width=70, height=35)

def fugir(event):
    largura = root.winfo_width() - 70
    altura = root.winfo_height() - 35
    novo_x = random.randint(0, largura)
    novo_y = random.randint(0, altura)
    btn_nao.place(x=novo_x, y=novo_y)

# Quando o mouse encosta no botão, ele pula pra outro lugar
btn_nao.bind("<Enter>", fugir)

root.mainloop()