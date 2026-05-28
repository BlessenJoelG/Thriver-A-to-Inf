class Solution:
    def whichWeekDay(self, day):
        match day:
            case day if day == 1:
                print("Monday")
            case day if day == 2:
                print("Tuesday")
            case day if day == 3:
                print("Wednesday")
            case day if day == 4:
                print("Thursday")
            case day if day == 5:
                print("Friday")
            case day if day == 6:
                print("Satday")
            case day if day == 7:
                print("Sunday")
            case day:
                print("Invalid")