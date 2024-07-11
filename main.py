import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import time
import os

from lexico import generar_log_lexico,error_lex
from sintactico import analisis_semantico_sintactico,error_sym

class AnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyzer")
        self.root.geometry("1280x720")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TButton", padding=6, relief="flat", background="#6200EE", foreground="#FFFFFF")
        self.style.configure("TFrame", background="#F5F5F5")
        self.style.configure("TLabel", background="#F5F5F5", foreground="#212121")
        self.style.configure("TText", background="#FFFFFF")
        self.style.configure("TListbox", background="#FFFFFF")
        self.style.configure("Vertical.TScrollbar", background="#6200EE")
        self.style.configure("Horizontal.TScrollbar", background="#6200EE")

        self.create_widgets()

    def create_widgets(self):
        # Editor de Código
        self.editor_frame = ttk.Frame(self.root)
        self.editor_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")

        self.editor_label = ttk.Label(self.editor_frame, text="Editor de Código")
        self.editor_label.pack()

        self.editor_scroll_y = ttk.Scrollbar(self.editor_frame, orient=tk.VERTICAL)
        self.editor_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.editor_scroll_x = ttk.Scrollbar(self.editor_frame, orient=tk.HORIZONTAL)
        self.editor_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.code_editor = tk.Text(self.editor_frame, wrap=tk.NONE, width=90, height=20,
                                   yscrollcommand=self.editor_scroll_y.set, xscrollcommand=self.editor_scroll_x.set)
        self.code_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.editor_scroll_y.config(command=self.code_editor.yview)
        self.editor_scroll_x.config(command=self.code_editor.xview)

        # Botones
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

        self.run_button = ttk.Button(self.button_frame, text="Ejecutar", command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.save_button = ttk.Button(self.button_frame, text="Guardar", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.load_button = ttk.Button(self.button_frame, text="Cargar archivo", command=self.load_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.run_button.bind("<Enter>", lambda e: self.run_button.configure(style="Hover.TButton"))
        self.run_button.bind("<Leave>", lambda e: self.run_button.configure(style="TButton"))

        self.save_button.bind("<Enter>", lambda e: self.save_button.configure(style="Hover.TButton"))
        self.save_button.bind("<Leave>", lambda e: self.save_button.configure(style="TButton"))

        self.load_button.bind("<Enter>", lambda e: self.load_button.configure(style="Hover.TButton"))
        self.load_button.bind("<Leave>", lambda e: self.load_button.configure(style="TButton"))

        # Estilos
        self.style.configure("TButton", background="#6200EE", foreground="#FFFFFF")
        self.style.map("Hover.TButton",
                       background=[("active", "#B39DDB")])

        # Analizador Léxico
        self.lexical_frame = ttk.Frame(self.root)
        self.lexical_frame.grid(row=0, column=3, padx=10, pady=10, rowspan=2, sticky="nsew")

        self.lexical_label = ttk.Label(self.lexical_frame, text="Analizador Léxico")
        self.lexical_label.pack()

        self.lexical_scroll_y = ttk.Scrollbar(self.lexical_frame, orient=tk.VERTICAL)
        self.lexical_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.lexical_scroll_x = ttk.Scrollbar(self.lexical_frame, orient=tk.HORIZONTAL)
        self.lexical_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.lexical_list = tk.Listbox(self.lexical_frame, width=40, height=20,
                                       yscrollcommand=self.lexical_scroll_y.set, xscrollcommand=self.lexical_scroll_x.set)
        self.lexical_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lexical_scroll_y.config(command=self.lexical_list.yview)
        self.lexical_scroll_x.config(command=self.lexical_list.xview)

        # Analizador Semántico y Sintáctico
        self.analysis_frame = ttk.Frame(self.root)
        self.analysis_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.semantic_frame = ttk.Frame(self.analysis_frame)
        self.semantic_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        self.semantic_label = ttk.Label(self.semantic_frame, text="Analizador Semántico")
        self.semantic_label.pack()

        self.semantic_scroll_x = ttk.Scrollbar(self.semantic_frame, orient=tk.HORIZONTAL)
        self.semantic_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.semantic_scroll_y = ttk.Scrollbar(self.semantic_frame, orient=tk.VERTICAL)
        self.semantic_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.semantic_list = tk.Listbox(self.semantic_frame, width=50, height=10,
                                        yscrollcommand=self.semantic_scroll_y.set, xscrollcommand=self.semantic_scroll_x.set)
        self.semantic_list.pack(fill=tk.BOTH, expand=True)

        self.syntactic_frame = ttk.Frame(self.analysis_frame)
        self.syntactic_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        self.syntactic_label = ttk.Label(self.syntactic_frame, text="Analizador Sintáctico")
        self.syntactic_label.pack()

        self.syntactic_scroll_x = ttk.Scrollbar(self.syntactic_frame, orient=tk.HORIZONTAL)
        self.syntactic_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.syntactic_scroll_y = ttk.Scrollbar(self.syntactic_frame, orient=tk.VERTICAL)
        self.syntactic_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.syntactic_list = tk.Listbox(self.syntactic_frame, width=50, height=10,
                                         yscrollcommand=self.syntactic_scroll_y.set, xscrollcommand=self.syntactic_scroll_x.set)
        self.syntactic_list.pack(fill=tk.BOTH, expand=True)

        # Configurar redimensionamiento
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=1)

        self.editor_frame.grid_columnconfigure(0, weight=1)
        self.lexical_frame.grid_columnconfigure(0, weight=1)
        self.lexical_frame.grid_rowconfigure(0, weight=1)
        self.analysis_frame.grid_columnconfigure(0, weight=1)
        self.analysis_frame.grid_columnconfigure(1, weight=1)
    def show_no_errors_popup(self,message):
        messagebox.showinfo("Información", message)
    def run_code(self):
        # Aquí va el código para ejecutar el análisis léxico, sintáctico y semántico.
        code = self.code_editor.get("1.0", tk.END)

        self.lexical_list.delete(0, tk.END)
        self.semantic_list.delete(0, tk.END)
        self.syntactic_list.delete(0, tk.END)

        tokens = generar_log_lexico(code)
        log_sem, log_syn = analisis_semantico_sintactico(code)
        errores = False
        for token in tokens:
            self.lexical_list.insert(tk.END, token)

        for line in log_sem:
            self.semantic_list.insert(tk.END, line)
            if "Error" in line:
                errores = True
        for line in log_syn:
            self.syntactic_list.insert(tk.END, line)
            if "Error" in line:
                errores = True
        if (len(log_sem) == 0) and not(errores):
            self.show_no_errors_popup("No se encontraron errores")
        else:
            self.show_no_errors_popup("Revisa los errores encontrados")

    def save_file(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")

        # Crear la carpeta de destino en la raíz
        nombre_carpeta = f"{timestamp}-analizador"
        folder_path = os.path.join(os.getcwd(), nombre_carpeta)
        os.makedirs(folder_path, exist_ok=True)
        # Guardar el contenido del editor de código
        code_path = os.path.join(folder_path, f"{timestamp}-codigo.txt")
        with open(code_path, 'w') as file:
            file.write(self.code_editor.get("1.0", tk.END))

        # Guardar el analizador léxico
        lexical_path = os.path.join(folder_path, f"{timestamp}-analizador-lexico.txt")
        with open(lexical_path, 'w') as file:
            for item in self.lexical_list.get(0, tk.END):
                file.write(f"{item}\n")

        # Guardar el analizador semántico
        semantic_path = os.path.join(folder_path, f"{timestamp}-analizador-semantico.txt")
        with open(semantic_path, 'w') as file:
            for item in self.semantic_list.get(0, tk.END):
                file.write(f"{item}\n")

        # Guardar el analizador sintáctico
        syntactic_path = os.path.join(folder_path, f"{timestamp}-analizador-sintactico.txt")
        with open(syntactic_path, 'w') as file:
            for item in self.syntactic_list.get(0, tk.END):
                file.write(f"{item}\n")
        self.show_no_errors_popup(f"Se creó la carpeta {nombre_carpeta} en la raiz")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.code_editor.delete("1.0", tk.END)
                self.code_editor.insert(tk.END, file.read())

    def filter_errors(self):
        tokens = generar_log_lexico(self.code_editor.get("1.0", tk.END))
        self.lexical_list.delete(0, tk.END)
        for token in tokens:
            if "error" in token.lower():
                self.lexical_list.insert(tk.END, token)
if __name__ == "__main__":
    root = tk.Tk()
    app = AnalyzerApp(root)
    root.mainloop()
