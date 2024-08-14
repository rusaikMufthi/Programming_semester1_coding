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


def calculate_cost():
    athlete_name = input("Enter athlete's name: ")

    # Plan select
    while True:
        print("Select training plan:")
        for idx, plan in enumerate(TRAINING_PLANS, start=1):
            print(f"{idx}. {plan}")
        try:
            plan_choice = int(input("Enter your choice: "))
            if plan_choice in (1, 2, 3):
                selected_plan = list(TRAINING_PLANS.keys())[plan_choice - 1]
                break
            else:
                print("Invalid training plan. Please re-enter.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Weight input and categorization
    while True:
        try:
            current_weight = float(input("Enter current weight in kilograms (kg): "))
            if current_weight < 66:
                print("You are not eligible for this program. Gain weight & re-enter.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

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

    print(f"Your weight is {weight_category}")

    # Competition input
    while True:
        try:
            num_competitions = int(input("Enter number of competitions entered this month: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Cost calc
    private_coaching_hours = 0
    weekly_sessions = TRAINING_PLANS[selected_plan]['sessions_per_week']
    weekly_fee = TRAINING_PLANS[selected_plan]['weekly_fee']
    total_training_fee = (weekly_fee / weekly_sessions) * 4
    total_private_coaching_cost = private_coaching_hours * PRIVATE_COACHING_RATE
    total_competition_fees = num_competitions * COMPETITION_ENTRY_FEE
    total_cost = total_training_fee + total_private_coaching_cost + total_competition_fees

    # coaching input
    while True:
        add_coaching = input("Do you want to add private coaching hours? (yes/no): ").lower()
        if add_coaching == 'yes':
            while True:
                try:
                    pch = int(input("Enter number of hours of private coaching (0-5): "))
                    if 0 <= pch <= 5:
                        total_private_coaching_cost = (private_coaching_hours + pch) * PRIVATE_COACHING_RATE
                        total_cost = total_training_fee + total_private_coaching_cost + total_competition_fees
                        break
                    else:
                        print("Private coaching hours cannot exceed 5 per week. Please re-enter.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            break
        elif add_coaching == 'no':
            result(athlete_name, total_training_fee, total_private_coaching_cost, total_competition_fees, total_cost,
                   current_weight, selected_plan, weight_category)
            save_to_file(athlete_name, selected_plan, current_weight, selected_plan, num_competitions,
                         private_coaching_hours, total_training_fee, total_private_coaching_cost,
                         total_competition_fees,
                         total_cost)
            read_file()
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no' only!")

    while True:
        if 81 <= current_weight <= 100 and add_coaching == 'yes':
            print("Current weight is within the competition category. You are eligible for this.")
            if selected_plan == "Beginner" and num_competitions > 0:
                print("Beginner athletes cannot enter competitions. Please re-enter.")
                break

        else:
            print("Current weight is above the competition category. You are not eligible for this.")

            # Output results
            print(f"\nAthlete: {athlete_name}")
            print(f"Current weight: {current_weight} kg")
            print(f"Monthly training cost: Rs. {total_training_fee:.2f}")
            print(f"Private coaching cost: Rs. {total_private_coaching_cost:.2f}")
            print(f"Competition cost: Rs. {total_competition_fees:.2f}")
            print(f"Total monthly cost: Rs. {total_cost:.2f}")
            break

        # Result display
        result_state = input("Do you want to see your competition details (yes/no)?")
        if result_state == "yes":
            result(athlete_name, total_training_fee, total_private_coaching_cost, total_competition_fees,
                   total_cost,
                   current_weight, selected_plan, weight_category)
            save_to_file(athlete_name, selected_plan, current_weight, selected_plan, num_competitions,
                         private_coaching_hours, total_training_fee, total_private_coaching_cost,
                         total_competition_fees,
                         total_cost)
            read_file()
            break
        elif result_state == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no' only!")


def result(athlete_name, total_training_fee, total_private_coaching_cost, total_competition_fees, total_cost,
           current_weight, selected_plan, weight_category):
    print("\nAthlete's Name:", athlete_name)
    print("Breakdown of Costs:")
    print(f"- Monthly Training Fees: Rs. {total_training_fee:.2f}")
    print(f"- Private Coaching Cost: Rs. {total_private_coaching_cost:.2f}")
    print(f"- Competition Fees: Rs. {total_competition_fees:.2f}")
    print(f"Total Cost for the Month: Rs. {total_cost:.2f}")
    print(f"Current weight: {current_weight} kg")
    print(f"Competition Category: {weight_category}")
    print(f"Selected Plan: {selected_plan}")
    print("<-Above competition details in athlete_records.txt->")

def save_to_file(name, plan, weight, category, num_competitions, private_hours, training_fee, coaching_cost,
                 competition_fees, total_cost):
    with open('athlete_records.txt', 'a') as file:
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
        file.write(f"Comparison of Current Weight ({weight} kg) with {category} Category\n")
        file.write("-----------------------------------------\n\n")

def read_file():
    file = open("athlete_records.txt", "r")
    file_data = file.read()
    while True:
        read_state = input("Do you want to Athlete Records? (yes/no)")
        if read_state == "yes":
            print(file_data)
            break
        elif read_state == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no' only!")

if __name__ == "__main__":
    calculate_cost()
    while True:
        calc_state = input("Do you want to add another athlete? (yes/no)")
        if calc_state == "yes":
            calculate_cost()
        elif calc_state == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no' only!")