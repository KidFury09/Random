from datetime import date
import inflect


def main():

    p = inflect.engine()

    today = date.today()
    new_years = date(today.year + 1, 1, 1)

    time = new_years - today
    day = time.days
    minutes = day * 1440
    seconds = minutes * 86400

    print()
    print("There is exactly:")
    
    print("Days: ", p.number_to_words(day, andword="").capitalize() + " days")
    print("Minutes: ", p.number_to_words(minutes, andword="").capitalize() + " minutes")
    print("Seconds: ", p.number_to_words(seconds, andword="").capitalize() + " seconds")

    print(f"To {today.year + 1}")
    print()


if __name__ == "__main__":
    main()