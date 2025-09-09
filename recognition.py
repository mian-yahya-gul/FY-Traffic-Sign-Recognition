import random   # Python's built-in library to generate random choices

# ------------------------------
# Function: dummy_recognition
# Purpose: Simulate traffic sign recognition (for prototype/demo)
# ------------------------------
def dummy_recognition():
    # List of possible traffic signs (dummy categories for testing)
    signs = ["Stop Sign", "Yield Sign", "Speed Limit Sign", "No Entry Sign"]

    # Randomly return one traffic sign from the list
    # This simulates the prediction result of a deep learning model
    return random.choice(signs)
