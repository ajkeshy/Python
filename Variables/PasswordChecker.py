# 1. Ask for input
password = input("Please enter the admin password: ")

# 2. Check if the input matches our secret
# Notice the double equals (==)
if password == "PythonPro":
    print("✅ Access Granted!")
    print("Welcome to the secret server.")

# 3. Handle the wrong password
else:
    print("❌ Access Denied!")
    print("Please try again.")

print("--- System Check Complete ---")
