from collections import defaultdict
from datetime import datetime

def analyze_chat(file_path):
    # Dictionary to store message counts per user
    user_messages = defaultdict(int)
    # Dictionary to store message counts per hour of the day
    messages_per_hour = defaultdict(int)

    # Read and process each line in the file
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) != 3:
                continue  # Skip lines with incorrect format

            timestamp_str, user, message = parts
            try:
                timestamp = datetime.fromisoformat(timestamp_str)
                user_messages[user] += 1
                messages_per_hour[timestamp.hour] += 1
            except ValueError:
                continue  # Skip lines with invalid timestamps

    # Check if there are entries in user_messages dictionary
    if not user_messages:
        return 0, None, None

    # Calculate total messages per user
    total_messages = sum(user_messages.values())

    # Find the most active user
    most_active_user = max(user_messages, key=user_messages.get)

    # Find the hour with the most messages
    most_active_hour = max(messages_per_hour, key=messages_per_hour.get)

    return total_messages, most_active_user, most_active_hour

# Example usage:
file_path = '/Users/shashikumarezhil/Documents/chat_log.txt' #edit according to your file location
total_messages, most_active_user, most_active_hour = analyze_chat(file_path)

print(f'Total messages: {total_messages}')
print(f'Most active user: {most_active_user}')
if most_active_hour is not None:
    print(f'Most active hour: {most_active_hour}:00 - {most_active_hour + 1}:00')
else:
    print('No messages found in the chat log.')
