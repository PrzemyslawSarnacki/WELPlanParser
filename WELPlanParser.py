import pandas as pd
import csv


def map_shortcuts():
    shortcuts = []
    full_name = []
    # If there's more or less classes replace 26 with different number
    # or try to limit parsing on non-breaking space (&nbsp)
    for j in range(1, 26, 2):
        shortcuts.append(df[25][j])
        full_name.append(df[26][j] + ' ')
    return(dict(zip(shortcuts, full_name)))

def save_to_csv():
    filewriter = csv.writer(open("plan.csv", "w", newline=''), delimiter=',')
    filewriter.writerow(['Subject', 'Start Date', 'Start Time', 'End Time'])
    for column in range(3,25):
        date = []
        for x in range(1, 50, 8):
            date.append(df[column][x])
        for i in range(0, 7):
            hours = ((df[1])[(i*8)+1:(i+1)*8]).values.tolist()
            endHours = ((df[1])[(i*8)+1:(i+1)*8])
            endHours = endHours.replace({'8:00 AM': '9:35 AM', '9:50 AM': '11:25 AM', '11:40 AM':'1:15 PM', '1:30 PM':'3:05 PM', '3:45 PM' :'5:20 PM', '5:35 PM':'7:25 PM', '7:25 PM': '9:00 PM'})
            endHours = endHours.values.tolist()
            classes = (df[column])[(i*8)+1:(i+1)*8].values.tolist()
            for hour, classs, endHour in list(zip(hours, classes, endHours)):
                if classs != "&nbsp" and classs != "I":
                    filewriter.writerow([classs, date[i], hour, endHour])

dfs = pd.read_html("https://plany.wel.wat.edu.pl/lato/WEL19ET1S4.htm", flavor='lxml')
df = dfs[0]
df = df.iloc[1:]
df[1] = df[1].replace({'1-2':'8:00 AM', '3-4':'9:50 AM', '5-6':'11:40 AM', '7-8':'1:30 PM', '9-10':'3:45 PM', '11-12':'5:35 PM', '13-14':'7:25 PM'})
df = df.replace({'.III':'/03/2020', '.IV':'/04/2020','.VI':'/06/2020','.V':'/05/2020','.VII':'/07/2020',}, regex=True)
shortcuts_dict = map_shortcuts()
df = df.replace(shortcuts_dict, regex=True)
save_to_csv()