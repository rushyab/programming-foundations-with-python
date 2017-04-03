import webbrowser, time

link = "https://www.youtube.com/watch?v=A8OSsiMUdac" # cristiano ronaldo unstoppable

wait_time = 10   # break time in seconds
total_breaks = 3 # number of breaks
break_count = 0  # initial count

print("This program started on {}".format(time.ctime()))
while break_count < total_breaks:
    time.sleep(wait_time)
    webbrowser.open(link)
    break_count += 1
