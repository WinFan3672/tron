 
def tronTextEditor(path=""):
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import Menu
    from tkinter import filedialog
    from tkinter import simpledialog
    class Tron:
        def __init__(self, master):
            self.file_path = None
            self.master = master
            self.scrollbar = tk.Scrollbar(master)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Create the text widget and link the scrollbar to it
            self.text = tk.Text(master, bg="#002240", fg="white", insertbackground="white", yscrollcommand=self.scrollbar.set)
            self.text.bind("<Control-a>", self.select_all_text)
            self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Configure the scrollbar to work with the text widget
            self.scrollbar.config(command=self.text.yview)

            self.master.title("Tron :: Text Editor")
            self.master.geometry("500x700")

            self.menu_bar = tk.Menu(self.master)
            self.master.config(menu=self.menu_bar)

            self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
            self.menu_bar.add_cascade(label="File", menu=self.file_menu)
            self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
            self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
            self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
            self.file_menu.add_command(label="Save As", command=self.save_file_as, accelerator="Ctrl+Shift+S")
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.exit_application, accelerator="Ctrl+Q")

            self.edit_menu = tk.Menu(self.menu_bar, tearoff=False)
            self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
            self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="Ctrl+X")
            self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="Ctrl+C")
            self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste_text)
            self.edit_menu.add_separator()
            self.edit_menu.add_command(label="Select All", command=self.select_all_text, accelerator="Ctrl+A")
            self.edit_menu.add_command(label="Undo", command=self.undo_text, accelerator="Ctrl+Z")
            self.edit_menu.add_command(label="Redo", command=self.redo_text, accelerator="Ctrl+Y")
            self.edit_menu.add_separator()
            self.edit_menu.add_command(label="Go to Line", command=self.go_to_line, accelerator="Ctrl+G")
            
            help_menu = Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label="Help", menu=help_menu)
            help_menu.add_command(label="Help", command=self.show_help_info)
            help_menu.add_command(label="About Tron", command=self.show_about, accelerator="Shift+F1")
            self.master.bind("<Shift-F1>", self.show_about)

            self.master.bind("<Control-n>", lambda event: self.new_file())
            self.master.bind("<Control-a>", lambda event: self.select_all_text())
            self.master.bind("<Control-o>", lambda event: self.open_file())
            self.master.bind("<Control-s>", lambda event: self.save_file())
            self.master.bind("<Control-S>", lambda event: self.save_file_as())
            self.master.bind("<Control-q>", lambda event: self.exit_application())
            self.master.bind("<Shift-F1>", lambda event: self.show_about())
            self.master.bind("<Control-x>", lambda event: self.cut_text())
            self.master.bind("<Control-c>", lambda event: self.copy_text())
            self.master.bind("<Control-v>", lambda event: self.paste_text())
            self.master.bind("<Control-z>", lambda event: self.undo_text())
            self.master.bind("<Control-y>", lambda event: self.redo_text())
            self.master.bind("<Control-g>", lambda event: self.go_to_line())
            self.master.bind("<Shift-F1>", lambda event: self.show_about())
        def new_file(self):
            print("[TRON] File New")
            self.text.delete("1.0", "end")

        def open_file(self):
            file_path = filedialog.askopenfilename()
            print("[TRON] File Opened DialogWise:",file_path)
            if file_path:
                with open(file_path, "r") as file:
                    file_contents = file.read()
                    self.text.delete("1.0", "end")
                    self.text.insert("1.0", file_contents)

        def save_file(self):
            print("[TRON] Saved File")
            if self.file_path:
                with open(self.file_path, "w") as file:
                    file_contents = self.text.get("1.0", "end-1c")
                    file.write(file_contents)
            else:
                self.save_file_as()

        def save_file_as(self):
            file_path = filedialog.asksaveasfilename()
            print("[TRON] Saved File To",file_path)
            if file_path:
                with open(file_path, "w") as file:
                    file_contents = self.text.get("1.0", "end-1c")
                    file.write(file_contents)
                    self.file_path = file_path

        def show_about(self):
            message = "Tronzn\nText Editor: Rapid and Organised Notes\nv1.0.0\n\nTron is a general-purpose text editor made in Tkinter.\n(c) 2023 WinFan3672, some rights reserved.\nMIT License.\nCode generated with ChatGPT."
            width = max(len(line) for line in message.split("\n")) * 10
            messagebox.showinfo("About", message)


        def open_file_with_name(self, file_path=None):
            print("[TRON] Opened file manual",str(file_path))
            if file_path:
                with open(file_path, "r") as file:
                    file_contents = file.read()
                    self.text.delete("1.0", "end")
                    self.text.insert("1.0", file_contents)
                    self.file_path = file_path

        def run(self):
            self.master.mainloop()
        def cut_text(self):
            print("[TRON] Cut Text")
            self.text.event_generate("<<Cut>>")
        def copy_text(self):
            print("[TRON] Copied Text")
            self.text.event_generate("<<Copy>>")

        def paste_text(self):
            print("[TRON] Pasted Text")
            self.text.event_generate("<<Paste>>")

        def select_all_text(self, event=None):
            print("[TRON] SelectAlltext")
            self.text.tag_add(tk.SEL, "1.0", tk.END)
            self.text.mark_set(tk.INSERT, "1.0")
            self.text.see(tk.INSERT)

        def undo_text(self):
            if self.text.edit_modified():
                def undo_text(self):
                    try:
                        self.text.edit_undo()
                        print("[TRON] UndoAction")
                        self.text.edit_modified(False)
                    except:
                        print("[FAIL] UndoAction")

            else:
                print("[FAIL] UndoAction: undo stack is empty")


        def redo_text(self):
            try:
                self.text.edit_redo()
                print("[TRON] RedoAction")
            except:
                print("[FAIL] RedoAction")
        def show_help_info(self):
            help_text = "Tron Text Editor\n\nTo use Tron, use the menus at the top for operations such as opening files (also supports keyboard shortcuts as shown.)"
            messagebox.showinfo("Help", help_text)
        def go_to_line(self):
            line = simpledialog.askinteger("Go to Line", "Enter line number:")
            print("[TRON] WentToLine",line)
            if line:
                self.text.mark_set("insert", f"{line}.0")
                self.text.see("insert")

        def exit_application(self):
            print("[TRON] Exit Tron")
            print("Thanks for using Tron!")
            self.master.destroy()
    # Create a Tkinter root window
    root = tk.Tk()

    # Create a Tron object
    editor = Tron(root)

    # Run the Tron editor
    if path == "":
        editor.run()
    else:
        if os.path.isfile(path):
            editor.open_file_with_name(path)
            editor.run()
        else:
            editor.run()
    return editor
tronTextEditor()
