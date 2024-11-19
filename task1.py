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