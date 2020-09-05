#My calculator calculates how far one can run using three inputs 
print("Filler")
SPEED = int(input("What is your average speed (MPH) during (excluding break time) the run? "))
RUNTIME = int(input("How long (in MINTUES) will your ENTIRE run (including break time) be? "))
BREAKTIME = int(input("How long will your break be? "))
Final_Distance = ((RUNTIME - BREAKTIME)/60)*SPEED
print (F"Your computed running distance is {Final_Distance} miles!")

