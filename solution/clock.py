# Define a function that checks  whether the period is "am" or "pm" and adjusts the hour accordingly
def convert_to_24_hour_format(hour, minute, period):
    if period.lower() == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return "{:02d}:{:02d}".format(hour, minute)

# Example usage:
hour = 6
minute = 40
period = "pm"
result = convert_to_24_hour_format(hour, minute, period)
print(result)