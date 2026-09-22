#functions

# def athlete_inf(name, sport):
#     print(f"{name} plays {sport}")

# athlete_inf("maya", "basketball")

# def training_info(time,days):
#     total=time*days
#     return total

# result=training_info(2,5)
# print(f"Total training time is {result} hours")

# def training_info(time,days):
#     total=time*days
#     if total>10:
#         print("high training load")
#     else:
#         print("moiderate training load")

# training_info(2,5)

#task

# def calculate_bmi (weight, height):
#     total=weight / (height ** 2)
#     return total

# bmi = calculate_bmi(60, 1.65)
# print(f"BMI: {bmi:.2f}")

# def calculate_training_hours(days, hours):
#     return days * hours


# def check_training_load(total_hours):
#     if total_hours >= 12:
#         return "High training load"
#     elif total_hours >= 7:
#         return "Moderate training load"
#     else:
#         return "Low training load"

# weekly_hours = calculate_training_hours(5, 2)

# status = check_training_load(weekly_hours)

# print(f"Weekly hours: {weekly_hours}")
# print(f"Training status: {status}")

#challenge
#inputs
total_sleep = float(input("Enter total sleep hours for the week: "))
days = float(input("Enter number of days in the week: "))
hours = float(input("Enter average training hours per day: "))  

def calculate_average_sleep(total_sleep):
    avg_sleep=total_sleep/7
    return avg_sleep

def calculate_training_hours(days, hours):
    total=days * hours
    return total

def check_recovery(avg_sleep,total):
    if avg_sleep<6:
        return "Poor recovery"
    elif avg_sleep>=8 and total<=10:
        return"excellent recovery"
    else:
        return "Moderate recovery"

avg_sleep = calculate_average_sleep(total_sleep)
total_training_hours = calculate_training_hours(days, hours)
recovery=check_recovery(avg_sleep, total_training_hours)

print("----- WEEKLY ATHLETE REPORT -----")
print(f"Average sleep:{avg_sleep:.2f} hours")
print(f"Weekly training:{total_training_hours:.2f} hours")
print(f"Recovery status: {recovery}")
