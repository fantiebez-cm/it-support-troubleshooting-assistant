
def troubleshoot():
    print("=== IT Support Troubleshooting Assistant ===")
    print("1. No internet connection")
    print("2. Computer running slowly")
    print("3. Printer not working")

    choice = input("Choose a problem (1-3): ")

    if choice == "1":
        print("Check your network cable or Wi-Fi.")
        print("Restart your network adapter if appropriate.")
    elif choice == "2":
        print("Close unnecessary applications.")
        print("Check available disk space.")
    elif choice == "3":
        print("Check printer power and cables.")
        print("Check the paper and print queue.")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    troubleshoot()
