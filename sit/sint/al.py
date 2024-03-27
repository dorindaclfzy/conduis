import datetime

# Function to add a log entry with the current timestamp
def add_log_entry(log, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log[timestamp] = message

# Initialize the log dictionary
log = {}

# Example usage
add_log_entry(log, "Server started")
add_log_entry(log, "User logged in")

# This will print the log with timestamps
print(log)
