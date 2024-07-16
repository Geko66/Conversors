import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pillow_heif

def select_heic_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("HEIC files", "*.heic")])
    if file_paths:
        heic_files_label.config(text=", ".join(file_paths))

def select_output_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        output_dir_label.config(text=dir_path)

def convert_heic_to_jpg(heic_paths, output_dir):
    try:
        for heic_path in heic_paths:
            heif_image = pillow_heif.read_heif(heic_path)
            image = Image.frombytes(
                heif_image.mode, 
                heif_image.size, 
                heif_image.data,
                "raw",
                heif_image.mode,
                heif_image.stride,
            )
            output_path = f"{output_dir}/{heic_path.split('/')[-1].replace('.heic', '.jpg')}"
            image.save(output_path, "JPEG")
        messagebox.showinfo("Success", f"Images saved to {output_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert images: {e}")

def convert_button_clicked():
    heic_paths = heic_files_label.cget("text").split(", ")
    output_dir = output_dir_label.cget("text")

    if "No files selected" in heic_paths or output_dir == "No directory selected":
        messagebox.showwarning("Warning", "Please select HEIC files and an output directory")
        return

    convert_heic_to_jpg(heic_paths, output_dir)

# Create the main window
root = tk.Tk()
root.title("HEIC to JPG Converter")

# Create and place widgets
heic_files_label = tk.Label(root, text="No files selected")
heic_files_button = tk.Button(root, text="Select HEIC Files", command=select_heic_files)

output_dir_label = tk.Label(root, text="No directory selected")
output_dir_button = tk.Button(root, text="Select Output Directory", command=select_output_directory)

convert_button = tk.Button(root, text="Convert to JPG", command=convert_button_clicked)

heic_files_label.pack(pady=10)
heic_files_button.pack(pady=10)
output_dir_label.pack(pady=10)
output_dir_button.pack(pady=10)
convert_button.pack(pady=20)

# Start the main event loop
root.mainloop()
