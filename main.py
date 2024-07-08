import tkinter as tk
from tkinter import filedialog, scrolledtext

class AnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyzer")
        self.root.geometry("1280x720")

        self.create_widgets()

    def create_widgets(self):
        # Editor de Código
        self.editor_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN, bg="lightgrey")
        self.editor_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")

        self.editor_label = tk.Label(self.editor_frame, text="Editor de Código", bg="lightgrey")
        self.editor_label.pack()

        self.editor_scroll_y = tk.Scrollbar(self.editor_frame, orient=tk.VERTICAL)
        self.editor_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.editor_scroll_x = tk.Scrollbar(self.editor_frame, orient=tk.HORIZONTAL)
        self.editor_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.code_editor = tk.Text(self.editor_frame, wrap=tk.NONE, width=90, height=20, bg="white",
                                   yscrollcommand=self.editor_scroll_y.set, xscrollcommand=self.editor_scroll_x.set)
        self.code_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.editor_scroll_y.config(command=self.code_editor.yview)
        self.editor_scroll_x.config(command=self.code_editor.xview)

        # Botones
        self.button_frame = tk.Frame(self.root, bg="lightgrey")
        self.button_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

        self.run_button = tk.Button(self.button_frame, text="Ejecutar", command=self.run_code, bg="grey")
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Guardar", command=self.save_file, bg="grey")
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.button_frame, text="Cargar archivo", command=self.load_file, bg="grey")
        self.load_button.pack(side=tk.LEFT, padx=5)

        # Analizador Léxico
        self.lexical_frame = tk.Frame(self.root, bd=2, relief=tk.SUNKEN, bg="black")
        self.lexical_frame.grid(row=0, column=3, padx=10, pady=10, rowspan=2, sticky="nsew")

        self.lexical_label = tk.Label(self.lexical_frame, text="Analizador Léxico", bg="black", fg="white")
        self.lexical_label.pack()

        self.lexical_scroll_y = tk.Scrollbar(self.lexical_frame, orient=tk.VERTICAL)
        self.lexical_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.lexical_scroll_x = tk.Scrollbar(self.lexical_frame, orient=tk.HORIZONTAL)
        self.lexical_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.lexical_list = tk.Listbox(self.lexical_frame, width=40, height=20, bg="white",
                                       yscrollcommand=self.lexical_scroll_y.set, xscrollcommand=self.lexical_scroll_x.set)
        self.lexical_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lexical_scroll_y.config(command=self.lexical_list.yview)
        self.lexical_scroll_x.config(command=self.lexical_list.xview)

        # Analizador Semántico y Sintáctico
        self.analysis_frame = tk.Frame(self.root, bg="lightgrey")
        self.analysis_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.semantic_frame = tk.Frame(self.analysis_frame, bd=2, relief=tk.SUNKEN, bg="black")
        self.semantic_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        self.semantic_label = tk.Label(self.semantic_frame, text="Analizador Semántico", bg="black", fg="white")
        self.semantic_label.pack()

        self.semantic_scroll_x = tk.Scrollbar(self.semantic_frame, orient=tk.HORIZONTAL)
        self.semantic_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.semantic_output = scrolledtext.ScrolledText(self.semantic_frame, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED, bg="black", fg="white",
                                                         xscrollcommand=self.semantic_scroll_x.set)
        self.semantic_output.pack(fill=tk.BOTH, expand=True)

        self.semantic_scroll_x.config(command=self.semantic_output.xview)

        self.syntactic_frame = tk.Frame(self.analysis_frame, bd=2, relief=tk.SUNKEN, bg="black")
        self.syntactic_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        self.syntactic_label = tk.Label(self.syntactic_frame, text="Analizador Sintáctico", bg="black", fg="white")
        self.syntactic_label.pack()

        self.syntactic_scroll_x = tk.Scrollbar(self.syntactic_frame, orient=tk.HORIZONTAL)
        self.syntactic_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.syntactic_output = scrolledtext.ScrolledText(self.syntactic_frame, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED, bg="black", fg="white",
                                                          xscrollcommand=self.syntactic_scroll_x.set)
        self.syntactic_output.pack(fill=tk.BOTH, expand=True)

        self.syntactic_scroll_x.config(command=self.syntactic_output.xview)

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

    def run_code(self):
        # Aquí va el código para ejecutar el análisis léxico, sintáctico y semántico.
        code = self.code_editor.get("1.0", tk.END)

        # Ejemplo de análisis léxico básico (esto debe ser reemplazado por el análisis real)
        tokens = code.split()
        self.lexical_list.delete(0, tk.END)
        for token in tokens:
            self.lexical_list.insert(tk.END, f"Lexema: {token}, Token: TOKEN_TYPE")

        # Ejemplo de resultados de análisis sintáctico y semántico
        self.semantic_output.config(state=tk.NORMAL)
        self.semantic_output.delete("1.0", tk.END)
        self.semantic_output.insert(tk.END, "Resultados del análisis semántico")
        self.semantic_output.config(state=tk.DISABLED)

        self.syntactic_output.config(state=tk.NORMAL)
        self.syntactic_output.delete("1.0", tk.END)
        self.syntactic_output.insert(tk.END, "Resultados del análisis sintáctico")
        self.syntactic_output.config(state=tk.DISABLED)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.code_editor.get("1.0", tk.END))

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.code_editor.delete("1.0", tk.END)
                self.code_editor.insert(tk.END, file.read())

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalyzerApp(root)
    root.mainloop()
