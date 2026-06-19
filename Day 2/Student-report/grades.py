def calculate_total(marks):
    total = 0
    for key, value in marks.items():
        total = total + value
    return total

def calculate_average(marks):
    avg = calculate_total(marks)/len(marks)
    return avg

def calculate_grade(marks):
    percentage = calculate_average(marks)
    if percentage > 89:
        return "A"
    elif percentage > 74:
        return "B"
    elif percentage > 59:
        return "C"
    elif percentage > 39:
        return "D"
    else:
        return "F"
