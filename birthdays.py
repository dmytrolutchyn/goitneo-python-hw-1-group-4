from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    bd_weekdays = {day: [] for day in weekdays}
    
    today = datetime.now().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today: # check if birthday already happened
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days # how many days left to birthday

        birthday_weekday = birthday_this_year.strftime("%A")

        time_to_next_Saturday = timedelta((12 - today.weekday()) % 7).days # days left to this Saturday, so we can congratulate them on next Monday

        if time_to_next_Saturday <= delta_days < time_to_next_Saturday + 7: # is within next week (this Saturday - next Saturday)
            day_of_week = birthday_this_year.weekday()
            if day_of_week > 4: # check for weekends
                bd_weekdays["Monday"].append(name)
            else:
                bd_weekdays[birthday_weekday].append(name)

    for day, names in bd_weekdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")


if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(2024, 3, 28)}, # Next Thursday
        {"name": "Jan Koum", "birthday": datetime(2024, 3, 24)}, # This Sunday -> congratulate on Monday
        {"name": "Jill Valentine", "birthday": datetime(2024, 3, 19)}, # This Tuesday -> do not congratulate next week
        {"name": "Kim Kardashian", "birthday": datetime(2024, 3, 23)}, # This Saturday -> congratulate on Monday
        {"name": "Elon Musk", "birthday": datetime(2024, 3, 20)}, # This Wednesday -> do not congratulate next week
        {"name": "Joe Rogan", "birthday": datetime(2024, 3, 26)} # Next Tuesday
    ]

    get_birthdays_per_week(users)
