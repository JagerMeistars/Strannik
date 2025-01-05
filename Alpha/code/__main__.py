import tkinter as tk
from tkinter import ttk, messagebox

class StrannikApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Strannik")
        self.root.configure(bg='black')  # Set background color to black

        # Create a style for the combobox
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TCombobox', fieldbackground='black', background='black', foreground='white', borderwidth=5, relief="flat")
        style.map('TCombobox', fieldbackground=[('readonly', 'black')], background=[('readonly', 'black')], foreground=[('readonly', 'white')])
        style.configure('TComboboxPopdownFrame', background='black', foreground='white')
        style.configure('TEntry', fieldbackground='black', background='black', foreground='white', borderwidth=5, relief="flat")
        style.configure('TButton', background='black', foreground='white', borderwidth=5, relief="flat")

        self.create_widgets()

    def create_widgets(self):
        # Language selection
        self.language_label = ttk.Label(self.root, text="Select Language:", background='black', foreground='white')
        self.language_label.pack(pady=5, anchor='w')
        self.language_var = tk.StringVar()
        self.language_combobox = ttk.Combobox(self.root, textvariable=self.language_var, style='TCombobox')
        self.language_combobox['values'] = ('English', 'Русский')
        self.language_combobox.pack(pady=5, anchor='w')

        # Screen resolution selection
        self.resolution_label = ttk.Label(self.root, text="Select Screen Resolution:", background='black', foreground='white')
        self.resolution_label.pack(pady=5, anchor='w')
        self.resolution_var = tk.StringVar()
        self.resolution_combobox = ttk.Combobox(self.root, textvariable=self.resolution_var, style='TCombobox')
        self.resolution_combobox['values'] = ('800x600', '1024x768', '1280x720', '1920x1080')
        self.resolution_combobox.pack(pady=5, anchor='w')

        # Name entry
        self.name_label = ttk.Label(self.root, text="Enter Your Name:", background='black', foreground='white')
        self.name_label.pack(pady=5, anchor='w')
        self.name_entry = ttk.Entry(self.root, style='TEntry')
        self.name_entry.pack(pady=5, anchor='w')

        # Start button
        self.start_button = ttk.Button(self.root, text="Start Game", command=self.start_game, style='TButton')
        self.start_button.pack(pady=20, anchor='w')

    def start_game(self):
        language = self.language_var.get()
        resolution = self.resolution_var.get()
        name = self.name_entry.get()

        if not language or not resolution or not name:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Set the resolution
        width, height = map(int, resolution.split('x'))
        self.root.geometry(f"{width}x{height}")

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Initialize game environment
        self.initialize_game(language, name)

    def initialize_game(self, language, name):
        # Define behavior rules
        behavior_rules = {
            "movement": "Characters can move in four directions: up, down, left, right.",
            "interaction": "Characters can interact with objects and other characters.",
            "inventory": "Characters can pick up and use items."
        }

        # Define narrative structure
        narrative_structure = {
            "intro": "The game begins with the character waking up in a mysterious place.",
            "main_quest": "The character must find a way to escape the place.",
            "side_quests": ["Find hidden items", "Help other characters"],
            "ending": "The game ends when the character finds the exit."
        }

        # Define plot maps
        plot_maps = {
            "starting_area": {
                "description": "A small room with a bed and a door.",
                "connections": ["hallway"]
            },
            "hallway": {
                "description": "A long hallway with several doors.",
                "connections": ["starting_area", "kitchen", "library"]
            },
            "kitchen": {
                "description": "A kitchen with a table and some cabinets.",
                "connections": ["hallway"]
            },
            "library": {
                "description": "A library filled with books.",
                "connections": ["hallway"]
            }
        }

        # Display game screen
        game_frame = tk.Frame(self.root, bg='black')
        game_frame.pack(fill='both', expand=True)

        # Display initial game state
        initial_text = narrative_structure["intro"]
        initial_label = ttk.Label(game_frame, text=initial_text, background='black', foreground='white', font=("Helvetica", 18))
        initial_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = StrannikApp(root)
    root.mainloop()