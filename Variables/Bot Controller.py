#A script that simulates an always-on robot
print("🤖 Robot System Online. ")
print("Type 'quit' to exit the program.")

while True:
    command = input("\nCommand > ").lower()
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
    else:
        print("Error: Unknown command.")
# The robot will respond to commands until 'quit' is entered
