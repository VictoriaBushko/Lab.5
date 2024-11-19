class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __del__(self):
        print(f"Об'єкт TimeConverter {self.hours:02}:{self.minutes:02}:{self.seconds:02} видалено")

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def display_time(self):
        print(f"Поточний час: {self.hours:02}:{self.minutes:02}:{self.seconds:02}")

    def outputConvertedTime(self, input_time=None):
        if input_time is None:
            self.display_time()
        elif isinstance(input_time, int):
            self.from_seconds(input_time)
            print(f"Час із секунд: {self.hours:02}:{self.minutes:02}:{self.seconds:02}")
        elif isinstance(input_time, str):
            try:
                h, m, s = map(int, input_time.split(":"))
                self.hours, self.minutes, self.seconds = h, m, s
                seconds = self.to_seconds()
                print(f"Час у секундах: {seconds}")
            except ValueError:
                print("Помилка: Невірний формат часу. Використовуйте формат hh:mm:ss.")

def main():
    time_converter = TimeConverter(4, 26, 11)
    time_converter.display_time()

    seconds = time_converter.to_seconds()
    print(f"Час у секундах: {seconds}")

    time_converter.from_seconds(5400)
    time_converter.display_time()

    print("\nПриклад з outputConvertedTime:")
    time_converter.outputConvertedTime("8:11:43")
    time_converter.outputConvertedTime(3661)
    time_converter.outputConvertedTime(5400)
    time_converter.outputConvertedTime()

if __name__ == "__main__":
    main()


class TimeConverter:
    def __init__(self, year=0, month=1, day=1, hour=0, minute=0, second=0):
        self.is_bce = year < 0
        self.year = abs(year)
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def calculate_seconds_from_start(self):
        try:
            days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            days_in_years = 0
            for y in range(1, self.year):
                if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                    days_in_years += 366
                else:
                    days_in_years += 365

            days_in_month = 0
            for m in range(self.month - 1):
                days_in_month += days_in_months[m]
            if self.month > 2 and ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
                days_in_month += 1

            total_days = days_in_years + days_in_month + (self.day - 1)

            total_seconds = total_days * 86400 + self.hour * 3600 + self.minute * 60 + self.second

            return -total_seconds if self.is_bce else total_seconds

        except Exception as e:
            print(f"Помилка: {e}")
            return None

    def display_seconds(self):
        seconds = self.calculate_seconds_from_start()
        if seconds is not None:
            era = "до н.е." if self.is_bce else "н.е."
            date_str = f"{'-' if self.is_bce else ''}{self.year:04}-{self.month:02}-{self.day:02} {self.hour:02}:{self.minute:02}:{self.second:02}"
            print(f"Кількість секунд від 0 року до {date_str} ({era}): {int(seconds)} секунд")


def main():
    date_input = input(
        "Введіть дату і час у форматі рік:місяць:день:година:хвилина:секунда (наприклад, -2024:03:15:12:30:45 або -2024/03/15/12/30/45 для до н.е.): ")

    try:
        date_input = date_input.replace('/', ':')

        if not all(c.isdigit() or c in ":-" for c in date_input):
            raise ValueError("Неправильний формат дати. Використовуйте тільки цифри та роздільники ':' і '-'.")

        date_parts = date_input.split(':')
        if len(date_parts) < 3:
            raise ValueError("Неправильний формат дати. Введіть принаймні рік, місяць і день.")

        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])
        hour = int(date_parts[3]) if len(date_parts) > 3 else 0
        minute = int(date_parts[4]) if len(date_parts) > 4 else 0
        second = int(date_parts[5]) if len(date_parts) > 5 else 0

        if not (1 <= month <= 12):
            raise ValueError("Місяць має бути в діапазоні від 1 до 12.")
        if not (1 <= day <= 31):
            raise ValueError("День має бути в діапазоні від 1 до 31.")
        if not (0 <= hour < 24):
            raise ValueError("Година має бути в діапазоні від 0 до 23.")
        if not (0 <= minute < 60):
            raise ValueError("Хвилина має бути в діапазоні від 0 до 59.")
        if not (0 <= second < 60):
            raise ValueError("Секунда має бути в діапазоні від 0 до 59.")

        time_converter = TimeConverter(year, month, day, hour, minute, second)
        time_converter.display_seconds()

    except ValueError as ve:
        print(f"Помилка: {ve}")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()