import tkinter as tk

# Function to validate user credentials
def validate_credentials():
    username = username_entry.get()
    password = password_entry.get()

    # Replace with your logic to validate the user credentials
    # Example: checking against a database or predefined credentials
    if username == "Sai Ram" and password == "Sai.2384":
        # Show the main application window if credentials are valid
        window.deiconify()
        login_window.withdraw()
    elif username == "Devansh" and password == "mishra":
        window.deiconify()
        login_window.withdraw()
    elif username == "Jeevan" and password == "9705":
        window.deiconify()
        login_window.withdraw()
    elif username == "Yashwi" and password == "0012":
        window.deiconify()
        login_window.withdraw()
    elif username == "Nitesh" and password == "Sir":
        window.deiconify()
        login_window.withdraw()
    elif username == "DJ's" and password == "Siri":
        window.deiconify()
        login_window.withdraw()
    else:
        # Show an error message if credentials are invalid
        login_error_label.config(text="Invalid username or password")

# Function to log a workout
def log_workout():
    workout_name = name_entry.get()
    duration = int(duration_entry.get())

    workout_text.insert(tk.END, f"Workout Name: {workout_name}\n")
    workout_text.insert(tk.END, f"Duration: {duration} minutes\n")
    workout_text.insert(tk.END, "------------------------\n")

    # Get corresponding food_taken and water intake based on duration
    food_taken = get_food_taken_for_workout(workout_name, duration)
    water_intake = get_water_intake_for_workout(workout_name)

    # Display food_taken and water intake
    workout_text.insert(tk.END, "Food_taken:\n")
    for meal in food_taken:
        workout_text.insert(tk.END, f"- {meal}\n")

    workout_text.insert(tk.END, f"Water Intake: {water_intake} ml\n")
    workout_text.insert(tk.END, "------------------------\n")

    # Connect with Fitbit API and log the workout
    log_workout_with_fitbit(workout_name, duration)

def log_workout_with_fitbit(workout_name, duration):
    # Replace with your logic to connect with the Fitbit API and log the workout
    # Example: using Fitbit API library or making HTTP requests
    # Here, we simulate the Fitbit integration by printing the workout details
    print(f"Logged workout '{workout_name}' with duration {duration} minutes via Fitbit")

# Function to get food_taken for a workout based on duration
def get_food_taken_for_workout(workout_name, duration):
    if workout_name == "Running":
        if duration <= 15:
            food_taken = ["Banana", "whole grain toast with almond butter", " a small bowl of oatmeal"]
        elif duration <= 30:
            food_taken = ["Protein shake", "Greek yogurt with berries","a turkey wrap with vegetables"]
        else:
            food_taken = ["Whole grain cereal with low-fat milk", "a small turkey sandwich","a fruit smoothie"]
    elif workout_name == "Walking":
        if duration <= 15:
            food_taken = ["Apple slices with peanut butter", "a handful of nuts", " a small granola bar"]
        elif duration <= 30:
            food_taken = ["Whole grain toast with avocado", "a small bowl of muesli with fruits", " boiled egg with whole grain crackers."]
        else:
            food_taken = ["Whole grain cereal with low-fat milk"," a small turkey sandwich", " a fruit smoothie"]
    elif workout_name == "Swimming":
        if duration <= 15:
            food_taken = [" Whole grain cereal with low-fat milk","a fruit smoothie"]
        elif duration <= 30:
            food_taken = ["Grilled fish with steamed vegetables","a protein-rich salad"]
        else:
            food_taken = ["a chicken and vegetable stir-fry","a small turkey sandwich","a fruit smoothie"]
    elif workout_name == "Weight Lifting":
        if duration <= 15:
            food_taken = ["Greek yogurt with a tablespoon of honey","a handful of almonds","a protein bar"]
        elif duration <= 30:
            food_taken = ["Grilled chicken breast with sweet potatoes", "a protein shake with a banana"," a quinoa and vegetable bowl"]
        else:
            food_taken = ["Grilled lean meat or plant-based protein with whole grain pasta and marinara sauce", "a protein smoothie with banana and peanut butter","a turkey and vegetable wrap"]
    elif workout_name == "Cycling":
        if duration <= 15:
            food_taken = ["Whole grain toast with avocado","a small bowl of muesli with fruits","a boiled egg with whole grain crackers"]
        elif duration <= 30:
            food_taken = ["Grilled salmon with quinoa and vegetables","a protein smoothie with spinach","a chicken wrap with salad"]
        else:
            food_taken = ["Baked salmon with quinoa and roasted vegetables","a protein bar","a chicken stir-fry with brown rice and mixed vegetables"]
    elif workout_name == "HIIT":
        if duration <= 15:
            food_taken = ["Whole grain toast with avocado","a small handful of nuts","a fruit smoothie with protein powder"]
        elif duration <= 30:
            food_taken = ["Grilled chicken breast with quinoa and roasted vegetables","a protein shake with berries","a spinach salad with tofu"]
        else:
            food_taken = ["Grilled lean steak with roasted sweet potatoes and vegetables","a protein shake with almond milk","a quinoa and black bean bowl"]
    elif workout_name == "Yoga":
        if duration <= 15:
            food_taken = ["Greek yogurt with mixed berries","a small portion of trail mix","a whole grain wrap with hummus and vegetables"]
        elif duration <= 30:
            food_taken = [" Vegetable stir-fry with tofu or lean meat","a green smoothie with spinach and protein powder","a quinoa salad with avocado and chickpeas"]
        else:
            food_taken = ["Grilled fish with brown rice and steamed vegetables","a protein smoothie with chia seeds","a mixed greens salad with grilled chicken"]
    elif workout_name == "Cross Fit":
        if duration <= 15:
            food_taken = ["Whole grain crackers with almond butter","a small chicken or turkey wrap","a fruit and yogurt parfait"]
        elif duration <= 30:
            food_taken = ["Grilled lean steak with roasted sweet potatoes and vegetables","a protein shake with almond milk","a quinoa and black bean bowl"]
        else:
            food_taken = ["Grilled shrimp or tofu with whole wheat noodles and stir-fried vegetables","a quinoa and black bean salad"]
    elif workout_name == "Pilates":
        if duration <= 15:
            food_taken = ["Apple slices with almond butter","a small portion of cottage cheese with fruit"," a veggie omelet"]
        elif duration <= 30:
            food_taken = ["Grilled fish with brown rice and steamed vegetables", "a protein smoothie with chia seeds"]
        else:
            food_taken = ["a mixed greens salad with grilled chicken"]
    elif workout_name == "Circuit Training":
        if duration <= 15:
            food_taken = ["Whole grain cereal with low-fat milk","a small turkey or chicken sandwich","a fruit and yogurt smoothie"]
        elif duration <= 30:
            food_taken = ["Baked salmon with quinoa and roasted vegetables","a protein bar"]
        else:
            food_taken = [ "chicken stir-fry with brown rice and mixed vegetables"]
    elif workout_name == "Kick boxing":
        if duration <= 15:
            food_taken = ["Whole grain toast with almond butter and sliced banana","a small portion of brown rice with grilled chicken"]
        elif duration <= 30:
            food_taken = [" Grilled shrimp or tofu with whole wheat noodles and stir-fried vegetables","a protein shake with almond milk"]
        else:
            food_taken = ["a fruit smoothie with added protein","a quinoa and black bean salad"]
    elif workout_name == "Zumba":
        if duration <= 15:
            food_taken = ["Mixed fruit salad with Greek yogurt","a small portion of whole grain pasta with marinara sauce"]
        elif duration <= 30:
            food_taken = ["Grilled salmon with quinoa and steamed vegetables","a protein smoothie with almond milk and spinach"]
        else:
            food_taken = ["a vegetable and tofu stir-fry","a chicken and vegetable wrap"]
    elif workout_name == "Basketball":
        if duration <= 15:
            food_taken = ["Whole grain bagel with low-fat cream cheese", "a small portion of brown rice with grilled chicken or fish"]
        elif duration <= 30:
            food_taken = [" Grilled lean meat or plant-based protein with whole grain pasta and marinara sauce"]
        else:
            food_taken = ["a vegetable and bean burrito","a protein smoothie with banana and peanut butter","a turkey and vegetable wrap"]
    else:
        food_taken = []
    
    return food_taken

# Function to get water intake for a workout
def get_water_intake_for_workout(workout_name):
    # Replace with your logic to retrieve water intake for the workout
    # Example: querying a database or fetching from an API
    if workout_name == "Running":
        water_intake = 800
    elif workout_name == "Walking":
        water_intake = 1000
    elif workout_name =="Swimming":
        water_intake = 1000
    elif workout_name == "Weight Lifting":
        water_intake = 1300
    elif workout_name == "Cycling":
        water_intake = 2000
    elif workout_name == "HIIT":
        water_intake = 1800
    elif workout_name == "Yoga":
        water_intake = 500
    elif workout_name == "Cross Fit":
        water_intake = 2000
    elif workout_name == "Pilates":
        water_intake = 1000
    elif workout_name == "Circuit Training":
        water_intake = 500
    elif workout_name == "Kick boxing":
        water_intake = 800
    elif workout_name == "Zumba":
        water_intake = 250
    elif workout_name == "Basketball":
        water_intake = 600
    else:
        water_intake = 0
    return water_intake

# Create the login window
login_window = tk.Tk()
login_window.title("FITBIT - Login")
login_window.configure(bg="white")

# Create UI elements for login
login_label = tk.Label(login_window, text="FITBIT", font=("Arial", 40, "bold"), bg="black", fg="white")
username_label = tk.Label(login_window, text="Username:", bg="white")
username_entry = tk.Entry(login_window)
password_label = tk.Label(login_window, text="Password:", bg="white")
password_entry = tk.Entry(login_window, show="*")
login_button = tk.Button(login_window, text="Login", command=validate_credentials, bg="orange", fg="white")
login_error_label = tk.Label(login_window, text="", fg="red", bg="white")

# Arrange UI elements in login window
login_label.pack(pady=40)
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack(pady=20)
login_error_label.pack(pady=5)

# Create the main application window
window = tk.Tk()
window.title("FITBIT")
window.configure(bg="grey")

# Create UI elements for workouts
workout_name_label = tk.Label(window, text="Workout Name:", bg="white", fg="black")
name_entry = tk.Entry(window, bg="white", fg="black")
duration_label = tk.Label(window, text="Duration (minutes):", bg="white", fg="black")
duration_entry = tk.Entry(window, bg="white", fg="black")
log_workout_button = tk.Button(window, text="Log Workout", command=log_workout, bg="white", fg="black")
workout_text = tk.Text(window, height=20, width=60, bg="white", fg="black",font="Arials")

# Arrange UI elements using grid layout
workout_name_label.grid(row=0, column=0, pady=20)
name_entry.grid(row=0, column=1, pady=20)
duration_label.grid(row=1, column=0, pady=10)
duration_entry.grid(row=1, column=1, pady=10)
log_workout_button.grid(row=2, column=0, columnspan=2, pady=20)
workout_text.grid(row=3, column=0, columnspan=2, padx=20)

# Hide the main application window initially
window.withdraw()

# Start the login window
login_window.mainloop()
