RaceHours = int(input("Enter the race hours: "))
RaceMin = int(input("Enter the race minutes: "))
RaceSec = int(input("Enter the race seconds: "))

RaceTime = RaceHours *60*60 + RaceMin*60 + RaceSec

print("The Total race time in seconds is: ")
print(RaceTime)

BestTime = int(input("Enter the best time: "))

if BestTime < RaceTime:
    BestTime = RaceTime
    print("New Best Time")
elif BestTime == RaceTime:
    print("Best time is equal to race time")
else:
    print("Race time is lower than best time")


