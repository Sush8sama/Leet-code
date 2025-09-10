
"""
An interview question I heard some time ago.

Question: Given a time in hh:mm format, calculate the angle of the hour and minute hands on a clock.
"""

class ClockAngle:
    
    def __init__(self):


     """
     Returns how many degrees the hour hand is in front of the minute hand. 
     """    
    def calculate_angle_human(self, time: str) -> float:
        hours, minute = time.split(":")
        hours, minute = int(hours), int(minute)

        hours = hours % 12
        total_minutes = hours * 60 + minute
        hour_angle =  360/(12*60) * total_minutes
        minute_angle = 360/60 * minute

        angle = hour_angle - minute_angle 

        # Some parsing
        if angle > 180:
            angle = 360 - angle
        elif angle < -180:
            angle = 360 + angle
        return angle


if __name__ == "__main__":
    clock_angle = ClockAngle()
    print(clock_angle.calculate_angle_human("03:00"))  # 90.0
    print(clock_angle.calculate_angle_human("06:00"))  # 180.0
    print(clock_angle.calculate_angle_human("09:00"))  # 90.0
    print(clock_angle.calculate_angle_human("12:00"))  # 0.0
    print(clock_angle.calculate_angle_human("03:15"))  # 7.5
    print(clock_angle.calculate_angle_human("04:45"))  # 127.5
    print(clock_angle.calculate_angle_human("01:50"))  # 155.0
    print(clock_angle.calculate_angle_human("12:30"))  # 165.0