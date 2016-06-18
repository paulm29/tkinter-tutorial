'''
timetable2.txt is for a timetable program. It contains the following
on each line:
period,day,detail
e.g. 1,1,Information Technology
means I have Information Technology on Monday period 1
'''

timetable = []

def loadTimetable():
    with open("timetable2.txt") as file:
        for line in file:
            item = line.split(",") # separate on comma
            if len(item) == 1: # may be '\n' (new line)
                continue
            period = item[0]
            if period == "period": # skip the line in file starting with "period"
                continue
            day = item[1]
            detail = item[2]
            print(period + "," + day + "," + detail)
            timetable.append(period + "," + day + "," + detail)


def saveTimeTable():
    with open("timetable2.txt","w") as file: # don't forget the "w" for write

        file.write("period, day, detail\n") # write the header, \n is for new line

        # for each item in the timetable, write to file
        for item in timetable:
            print(item)
            item = item.split(",") # separate on commas
            file.write(item[0] + "," + item[1] + "," + item[2])


loadTimetable()
print("=================================================")
saveTimeTable()