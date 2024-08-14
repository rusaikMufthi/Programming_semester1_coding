import tkinter as tk
from tkinter import messagebox, simpledialog

TRAINING_PLANS = {
    'Beginner': {
        'sessions_per_week': 2,
        'weekly_fee': 2000
    },
    'Intermediate': {
        'sessions_per_week': 3,
        'weekly_fee': 5000
    },
    'Elite': {
        'sessions_per_week': 5,
        'weekly_fee': 7000
    }
}
PRIVATE_COACHING_RATE = 500
COMPETITION_ENTRY_FEE = 2500

class JudoFeeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Judo Training Fee Calculator")
        self.geometry("400x300")

        # Labels and Inputs
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter athlete's name:").pack()
        self.athlete_name_entry = tk.Entry(self)
        self.athlete_name_entry.pack()

        tk.Label(self, text="Select training plan:").pack()
        self.plan_var = tk.StringVar(value="Select Plan")
        self.plan_menu = tk.OptionMenu(self, self.plan_var, *TRAINING_PLANS.keys())
        self.plan_menu.pack()

        tk.Label(self, text="Enter current weight (kg):").pack()
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        tk.Label(self, text="Enter number of competitions:").pack()
        self.competitions_entry = tk.Entry(self)
        self.competitions_entry.pack()

        tk.Label(self, text="Private coaching hours (0-5):").pack()
        self.coaching_hours_entry = tk.Entry(self)
        self.coaching_hours_entry.pack()

        # Calculate button
        self.calculate_button = tk.Button(self, text="Calculate Cost", command=self.calculate_cost)
        self.calculate_button.pack()

    def calculate_cost(self):
        try:
            athlete_name = self.athlete_name_entry.get()
            selected_plan = self.plan_var.get()
            current_weight = float(self.weight_entry.get())
            num_competitions = int(self.competitions_entry.get())
            private_coaching_hours = int(self.coaching_hours_entry.get())

            if private_coaching_hours < 0 or private_coaching_hours > 5:
                raise ValueError("Private coaching hours must be between 0 and 5.")

            if current_weight < 66:
                messagebox.showinfo("Error", "You are not eligible for this program. Gain weight and re-enter.")
                return

            if selected_plan == "Select Plan":
                messagebox.showinfo("Error", "Please select a training plan.")
                return

            # Weight categorization
            if current_weight < 73:
                weight_category = "Flyweight"
            elif current_weight < 81:
                weight_category = "Lightweight"
            elif current_weight < 90:
                weight_category = "Light-Middleweight"
            elif current_weight < 100:
                weight_category = "Middleweight"
            elif current_weight == 100:
                weight_category = "Light-Heavyweight"
            else:
                weight_category = "Heavyweight"

            # Cost calculation
            weekly_sessions = TRAINING_PLANS[selected_plan]['sessions_per_week']
            weekly_fee = TRAINING_PLANS[selected_plan]['weekly_fee']
            total_training_fee = (weekly_fee / weekly_sessions) * 4
            total_private_coaching_cost = private_coaching_hours * PRIVATE_COACHING_RATE
            total_competition_fees = num_competitions * COMPETITION_ENTRY_FEE
            total_cost = total_training_fee + total_private_coaching_cost + total_competition_fees

            # Display results
            result_text = (
                f"Athlete's Name: {athlete_name}\n"
                f"Selected Plan: {selected_plan}\n"
                f"Current Weight: {current_weight} kg\n"
                f"Weight Category: {weight_category}\n"
                f"Monthly Training Fee: Rs. {total_training_fee:.2f}\n"
                f"Private Coaching Cost: Rs. {total_private_coaching_cost:.2f}\n"
                f"Competition Fees: Rs. {total_competition_fees:.2f}\n"
                f"Total Monthly Cost: Rs. {total_cost:.2f}"
            )
            messagebox.showinfo("Calculation Result", result_text)

            self.save_to_file(athlete_name, selected_plan, current_weight, weight_category, num_competitions, private_coaching_hours, total_training_fee, total_private_coaching_cost, total_competition_fees, total_cost)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def save_to_file(self, name, plan, weight, category, num_competitions, private_hours, training_fee, coaching_cost, competition_fees, total_cost):
        with open('Tkinter_athlete_records.txt', 'a') as file:
            file.write(f"Athlete's Name: {name}\n")
            file.write(f"Training Plan: {plan}\n")
            file.write(f"Current Weight: {weight} kg\n")
            file.write(f"Competition Weight Category: {category}\n")
            file.write(f"Number of Competitions Entered: {num_competitions}\n")
            file.write(f"Private Coaching Hours: {private_hours}\n")
            file.write(f"Breakdown of Costs:\n")
            file.write(f"- Training Fees: Rs. {training_fee:.2f}\n")
            file.write(f"- Private Coaching Cost: Rs. {coaching_cost:.2f}\n")
            file.write(f"- Competition Fees: Rs. {competition_fees:.2f}\n")
            file.write(f"Total Cost for the Month: Rs. {total_cost:.2f}\n")
            file.write("-----------------------------------------\n\n")

if __name__ == "__main__":
    app = JudoFeeCalculator()
    app.mainloop()
