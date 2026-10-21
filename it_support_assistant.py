
def troubleshoot(choice):
    print("=== IT Support Troubleshooting Assistant ===")

    if choice == "1":
        print("\nProblem: No internet connection")
        print("- Check your network cable or Wi-Fi.")
        print("- Check whether other devices can connect.")
        print("- Contact IT support if the issue continues.")

    elif choice == "2":
        print("\nProblem: Computer running slowly")
        print("- Close unnecessary applications.")
        print("- Check available disk space.")
        print("- Restart the computer if appropriate.")

    elif choice == "3":
        print("\nProblem: Printer not working")
        print("- Check printer power and cables.")
        print("- Check paper and toner levels.")
        print("- Check the printer queue.")

    else:
        print("Invalid choice.")

# Demonstrate each troubleshooting option
for option in ["1", "2", "3"]:
    troubleshoot(option)
    print("-" * 40)
