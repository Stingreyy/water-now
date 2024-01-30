import plyer
from datetime import datetime, timedelta
import time  # Add this import statement

# Get user input for weight and height
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in cm): "))

# Calculate recommended water intake
water_intake = (weight + height) * 0.035  # Adjust formula based on personal requirements

# Set reminder interval (e.g., every 30 minutes)
reminder_interval = timedelta(minutes=30)

# Main loop for reminders
while True:
    current_time = datetime.now()
    print("Drink water now!")

    # Display additional information, like current intake status or goal

    # Use plyer to show a notification
    plyer.notification.notify(
        title='Water Reminder',
        message='Remember to drink water!',
        timeout=10  # Display notification for 10 seconds
    )

    # Wait for the next reminder interval
    next_reminder_time = current_time + reminder_interval
    time_to_wait = (next_reminder_time - datetime.now()).total_seconds()
    time.sleep(time_to_wait)
