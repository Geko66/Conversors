import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Define una función para convertir HEIC a PNG
def heic_to_png(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, format="PNG")
        print(f"Archivo {input_path} convertido a {output_path}")
    except Exception as e:
        print(f"Error al convertir {input_path} a PNG: {e}")

# Función para seleccionar las imágenes HEIC
def select_heic_files():
    input_files = filedialog.askopenfilenames(filetypes=[("HEIC files", "*.heic")])
    if not input_files:
        return
    for input_file in input_files:
        heic_files.append(input_file)
        update_file_listbox()

# Función para seleccionar la ruta de destino
def select_output_directory():
    output_dir = filedialog.askdirectory()
    if output_dir:
        output_directory.set(output_dir)
        update_file_listbox()

# Función para actualizar la Listbox con las rutas seleccionadas
def update_file_listbox():
    file_listbox.delete(0, tk.END)
    for heic_file in heic_files:
        output_file = f"{output_directory.get()}/{heic_file.split('/')[-1].replace('.heic', '.png')}"
        file_listbox.insert(tk.END, f"De: {heic_file} a: {output_file}")

# Función para convertir las imágenes
def convert_files():
    for heic_file in heic_files:
        output_file = f"{output_directory.get()}/{heic_file.split('/')[-1].replace('.heic', '.png')}"
        heic_to_png(heic_file, output_file)
    heic_files.clear()
    update_file_listbox()
    print("Conversión completada.")

# Crear una ventana de GUI
root = tk.Tk()
root.title("HEIC to PNG Converter")

heic_files = []
output_directory = tk.StringVar()

# Botón para seleccionar archivos HEIC
select_heic_button = tk.Button(root, text="Seleccionar archivos HEIC", command=select_heic_files)
select_heic_button.pack()

# Botón para seleccionar la ruta de destino
select_output_button = tk.Button(root, text="Seleccionar ruta de destino", command=select_output_directory)
select_output_button.pack()

# Listbox para mostrar las rutas seleccionadas
file_listbox = tk.Listbox(root, width=80)
file_listbox.pack()

# Botón para convertir archivos
convert_button = tk.Button(root, text="Convertir archivos", command=convert_files)
convert_button.pack()

# Ejecutar la ventana de GUI
root.mainloop()
