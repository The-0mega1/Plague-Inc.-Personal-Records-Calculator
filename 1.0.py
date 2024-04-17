# Step 1: Show Information about the script
print(" ")
print("Plague Inc. Personal Records Calculator")
print("Version 1.0")
print("Made by Jake Huff AKA The_0mega1")
print(" ")

# Step 2: Assign each difficulty to a number between 1 and 4
difficultyMultipliers = {
    "Casual": 1,
    "1": 1,
    "Normal": 2,
    "2": 2,
    "Brutal": 3,
    "3": 3,
    "Mega Brutal": 4,
    "4": 4
}

# Step 3: Prompt for user input
score = int(input("Enter your score: "))
biohazards = int(input("Enter the number of biohazards you got: "))
time = int(input("Enter the time it took to complete the game in ingame days: "))
cureProgress = int(input("Enter the cure progress at the end of the game (as an integer): "))
difficulty = (input("Enter the the name of the difficulty you were playing on (Casual, Normal, Brutal, or Mega Brutal), or a number corresponding to the difficulty you were playing on (1, 2, 3, or 4): "))

# Step 4: Check if difficulty is valid
if difficulty in difficultyMultipliers: 
    difficultyMultiplier = difficultyMultipliers[difficulty]
else:
    print("Provided difficulty invalid. Please enter Casual, Normal, Brutal, Mega Brutal, or an integer between 1 and 4.")

# Step 5: Calculate Final Score
# MATH TIME!

finalScore = (((score * biohazards) - (time + cureProgress)) * difficultyMultiplier)

print(f"Final Score: {finalScore}")