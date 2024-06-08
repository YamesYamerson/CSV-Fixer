import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def process_csv(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Write the DataFrame to a new CSV file
        df.to_csv(output_file, index=False)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        output_path = file_path.replace('.csv', '_processed.csv')
        process_csv(file_path, output_path)
        messagebox.showinfo("Success", f"File processed and saved as {output_path}")
        download_button.config(state=tk.NORMAL)
        download_button.output_path = output_path

def download_file():
    download_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if download_path:
        pd.read_csv(download_button.output_path).to_csv(download_path, index=False)
        messagebox.showinfo("Success", f"File saved as {download_path}")

# Create the main window
root = tk.Tk()
root.title("CSV Processor")

# Create and place the upload button
upload_button = tk.Button(root, text="Upload CSV File", command=upload_file)
upload_button.pack(pady=20)

# Create and place the download button, initially disabled
download_button = tk.Button(root, text="Download Processed File", command=download_file, state=tk.DISABLED)
download_button.pack(pady=20)

# Run the application
root.mainloop()
