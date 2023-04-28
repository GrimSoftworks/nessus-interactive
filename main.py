import nessus
import file1
import file2
import file3

access_key = 'your_access_key'
secret_key = 'your_secret_key'

# Create a Nessus API client instance
client = nessus.NessusClient(access_key, secret_key)

# Authenticate with the Nessus API
client.login()

def menu():
    print("Select an option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        file1.function1()
    elif choice == "2":
        file2.function2()
    elif choice == "3":
        file3.function3()
    elif choice == "4":
        print("Exiting menu...")
    else:
        print("Invalid choice. Try again.")
        menu()

menu()
