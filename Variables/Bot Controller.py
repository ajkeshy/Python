#A script that simulates an always-on robot
print("🤖 Robot System V2.0 Online. ")
print("Type 'quit' to exit the program.")
#Creating a list of valid commands
valid_commands = ["start", "forward", "backward", "left", "right", "stop", "wait", "jump", "quit"]
#Check if the command is valid and respond accordingly

while True:
    command = input("\nCommand > ").lower()
    if command not in valid_commands:
        print("⚠️ Error: Unknown command. Please try again.")
    if command == "quit":
        print("Shutting down robot system. Goodbye!")
        break
    elif command == "start":
        print("Robotic arm is moving...")
    elif command == "forward":
        print("Robot moving forward.")
    elif command == "backward":
        print("Robot moving backward.")
    elif command == "left":
        print("Robot turning left.")
    elif command == "right":
        print("Robot turning right.")
    elif command == "stop":
        print("Robotic arm has halted.")
    elif command == "wait":
        print("Robot is in standby mode.")
    elif command == "jump":
        print("Robot is jumping!")
# The robot will respond to commands until 'quit' is entered
