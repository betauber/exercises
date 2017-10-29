def days_till_chrismas(day, month):
    # TODO: For now we assume every month has 30 days
    months = [30 for x in range(12)]
    day_count = 0

    # Add remaining days of the current month
    day_count += months[month] - day

    # Add days from the next month till november (included)
    for i in range(month+1, 11):
        day_count += months[i]

    # Add days in december
    day_count += 24

    return day_count


d = days_till_chrismas(14, 2)

print(d)