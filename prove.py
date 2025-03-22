import tkinter as tk

root = tk.Tk()
root.title("Tris - Tic Tac Toe")
root.geometry("400x450")



# def on_click(r, c):
#     print(f"Ciao")
#
# buttons = [[None for _ in range(3)] for _ in range(3)]
#
# for i in range(3):
#     for j in range(3):
#         buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
#         buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

root.mainloop()  # Avvia la GUI