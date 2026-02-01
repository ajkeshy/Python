#A script that simulates a simple robot

#Ask for user input
command = input("Enter a command for the robot (forward, backward, left, right, start, stop): ")

#Process the commands
if command == "start":
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
