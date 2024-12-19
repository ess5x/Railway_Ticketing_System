def display_summary(name, destination, ticket_count, total_price):
    print("\n--- Transaction Summary ---")
    print(f"Customer Name: {name}")
    print(f"Destination: {destination}")
    print(f"Number of Tickets: {ticket_count}")
    print(f"Total Price: £{total_price:.2f}")


def generate_receipt(name, destination, ticket_count, total_price):
    filename = f"{name.replace(' ', '_').lower()}_receipt.txt"
    with open(filename, "w") as file:
        file.write("--- Receipt ---\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"Destination: {destination}\n")
        file.write(f"Number of Tickets: {ticket_count}\n")
        file.write(f"Total Price: £{total_price:.2f}\n")
    print(f"\nReceipt has been generated: {filename}")


def main():
    print("Welcome to the Railway Ticketing System!")

    # Prices for destinations
    prices = {
        "London": 10.15,
        "Manchester": 22.50,
        "Birmingham": 21.40
    }

    #Get the user's name
    name = input("Please enter your name: ").strip()

    #Ask for the destination
    print("\nDestinations and Prices:")
    for destination, price in prices.items():
        print(f"{destination}: £{price:.2f}")
    
    destination = input("\nEnter your destination: ").strip()
    if destination not in prices:
        print("Invalid destination. Please restart the system.")
        return

    # Ask for the number of tickets
    try:
        ticket_count = int(input("Enter the number of tickets you want to purchase: "))
        if ticket_count <= 0:
            print("Number of tickets must be greater than 0.")
            return
    except ValueError:
        print("Invalid input for the number of tickets. Please enter an integer.")
        return

    # Calculate the total price
    total_price = prices[destination] * ticket_count

    # Display transaction summary
    display_summary(name, destination, ticket_count, total_price)

    # Ask if they want a receipt
    receipt_choice = input("\nDo you want to print a receipt? (yes/no): ").strip().lower()
    if receipt_choice == "yes":
        generate_receipt(name, destination, ticket_count, total_price)
    else:
        print("Thank you for your purchase! Have a great day!")


if __name__ == "__main__":
    main()
