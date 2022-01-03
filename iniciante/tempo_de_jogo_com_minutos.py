class Time:
    total_minutes: int
    minute: int
    hour: int
    def __init__(self, hour: int, minute: int) -> None:
        self.hour = hour
        self.minute = minute
        self.total_minutes = hour * 60 + minute

    @classmethod
    def from_minutes(cls, minutes: int) -> "Time":
        return cls(minutes // 60, minutes % 60)

    def __eq__(self, other: "Time"):
        return self.total_minutes == other.total_minutes

    def __gt__(self, other: "Time"):
        return self.total_minutes > other.total_minutes

    def __lt__(self, other: "Time"):
        return self.total_minutes < other.total_minutes

    def __ge__(self, other: "Time"):
        return self.total_minutes >= other.total_minutes

    def __le__(self, other: "Time"):
        return self.total_minutes <= other.total_minutes

    def __sub__(self, other: "Time"):
        if self == other:
            return Time(24, 0)
        elif self > other:
            return Time.from_minutes(24*60 + other.total_minutes - self.total_minutes)
        elif self < other:
            return Time.from_minutes(other.total_minutes - self.total_minutes)
    
    def __str__(self) -> str:
        return f"{self.hour}:{self.minute:02d}"

def main():
    hour1, minute1, hour2, minute2 = list(map(int, input().split()))
    time1 = Time(hour1, minute1)
    time2 = Time(hour2, minute2)
    duration = time1 - time2
    print(f"O JOGO DUROU {duration.hour} HORA(S) E {duration.minute} MINUTO(S)")

if __name__ == "__main__":
    main()