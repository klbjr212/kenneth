"""
Outage Notification Template Application
Beginner-friendly CLI app to generate outage notification messages.

What this app teaches:
- Variables & dictionaries
- Functions
- if / elif / else blocks
- String formatting
- User input
"""

# -----------------------------
# Templates
# -----------------------------

templates = {
    "investigating": (
        "NOC has received reports of customers experiencing service interruptions in {location}. "
        "The issue is currently under investigation by NOC and Tier 2. "
        "There is no ETR at this time."
    ),
    "identified": (
        "NOC has identified the cause of the outage affecting customers in {location}. "
        "Field Operations have been notified and are engaged. "
        "Estimated restoration time will be provided once available."
    ),
    "restoring": (
        "Technicians are actively working to restore services for customers in {location}. "
        "Repairs are in progress. Additional updates will be shared as work continues."
    ),
    "restored": (
        "NOC has confirmed that services have been fully restored for all affected customers in {location}. "
        "We will continue to monitor to ensure stability."
    ),
}


# -----------------------------
# Functions
# -----------------------------

def show_menu():
    print("\nOutage Notification Generator")
    print("------------------------------")
    print("1. Investigating")
    print("2. Identified")
    print("3. Restoring")
    print("4. Restored")
    print("5. Quit")


def get_template_choice():
    choice = input("Choose a template (1-5): ").strip()

    if choice == "1":
        return "investigating"
    elif choice == "2":
        return "identified"
    elif choice == "3":
        return "restoring"
    elif choice == "4":
        return "restored"
    elif choice == "5":
        return None
    else:
        print("Invalid choice. Try again.")
        return "invalid"


def generate_message(template_key, location):
    template = templates[template_key]
    return template.format(location=location)


# -----------------------------
# Main App Loop
# -----------------------------

def main():
    while True:
        show_menu()
        template_key = get_template_choice()

        if template_key is None:
            print("Goodbye.")
            break
        elif template_key == "invalid":
            continue

        location = input("Enter affected location (city/state or site ID): ").strip()

        if not location:
            print("Location cannot be empty.")
            continue

        message = generate_message(template_key, location)

        print("\n--- Generated Notification ---")
        print(message)
        print("-------------------------------")


# Run the app
if __name__ == "__main__":
    main()
