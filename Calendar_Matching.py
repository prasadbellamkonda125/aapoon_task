"""Calendar Matching"""

from datetime import datetime, timedelta

def calendar_matching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):

    calendar1 = [[datetime.strptime(start, '%H:%M'), datetime.strptime(end, '%H:%M')] for start, end in calendar1]
    calendar2 = [[datetime.strptime(start, '%H:%M'), datetime.strptime(end, '%H:%M')] for start, end in calendar2]
    dailyBounds1 = [datetime.strptime(time, '%H:%M') for time in dailyBounds1]
    dailyBounds2 = [datetime.strptime(time, '%H:%M') for time in dailyBounds2]
    meetingDuration = timedelta(minutes=meetingDuration)

    # Merge both calendars into a single list of time slots
    calendar = calendar1 + calendar2
    calendar.sort()

    # available time slots
    available_slots = []
    start = min(dailyBounds1[0], dailyBounds2[0])
    end = max(dailyBounds1[1], dailyBounds2[1])
    current = start
    for i in range(len(calendar)):
        if current + meetingDuration <= calendar[i][0]:
            available_slots.append([current.strftime('%H:%M'), (current + meetingDuration).strftime('%H:%M')])
        current = calendar[i][1]
    if current + meetingDuration <= end:
        available_slots.append([current.strftime('%H:%M'), (current + meetingDuration).strftime('%H:%M')])

    return available_slots


calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

available_slots = calendar_matching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)

print(available_slots)

