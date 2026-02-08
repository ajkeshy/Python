#A script that simulates an always-on robot
print("🤖 Robot System V3.0 Online. ")
print("Type 'quit' to exit the program.")
#We are now using the concept of a dictionary to map commands to their respective values
commands = { 
    "start": "Robotic arm is moving...",
    "forward": "Robot is moving forward..",
    "backward": "Robot is moving backward.",
    "left": "Robot is turning left.",
    "right": "Robot is turning right.",
    "stop": "Robotic arm has halted.",
    "wait": "Robot is in standby mode.",
    "jump": "Robot is jumping!",
    "dance": "Robot is dancing! 💃",
    "sing": "Robot is singing! 🎤",
    "charge": "Robot is charging its batteries.",
} 

while True:
    command = input("\nCommand > ").lower()

#Handling the quit command first to allow for a clean exit before processing other commands
    if command == "quit":
        print("Shutting down the robot system. Goodbye!")
        break #Exit the loop and end the program

    if command in commands:
        print(commands[command]) #Print the response associated with the command
    else:        
        print("Unknown command. Please try again.") #Handle unrecognized commands

    #Adding logs to ensure logs are kept as best practice
    with open("robot_log.txt", "a") as log_file:
        log_file.write(command + "\n")

# The robot will respond to commands until 'quit' is entered
#The while lop has now become shorter and more efficient due to the use of a dictionary, which allows for easy addition of new commands in the future.
