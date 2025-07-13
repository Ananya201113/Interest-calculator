import tkinter as tk

def calculate_interest():
    try:
        P = float(entry_principal.get())
        R = float(entry_rate.get())
        T = float(entry_time.get())

        # Simple Interest
        si = (P * R * T) / 100

        # Compound Interest
        ci = P * ((1 + R / 100) ** T) - P

        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")
    except:
        result_label.config(text="Please enter valid numbers!")

# GUI setup
root = tk.Tk()
root.title("Interest Calculator")
root.configure(bg="#f0f8ff") 
root.geometry("350x250")


tk.Label(root, text="Principal:").grid(row=0, column=0)
tk.Label(root, text="Rate (%):").grid(row=1, column=0)
tk.Label(root, text="Time (years):").grid(row=2, column=0)

entry_principal = tk.Entry(root)
entry_rate = tk.Entry(root)
entry_time = tk.Entry(root)

entry_principal.grid(row=0, column=1)
entry_rate.grid(row=1, column=1)
entry_time.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
