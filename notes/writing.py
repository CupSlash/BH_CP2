#BH 2nd writing.py
#with open("BH_CP2\\notes\\new.txt", 'a') as file:
#    file.write("Joe\n")
#    file.write("Israel\n")
#    file.write("Zee\n")

#print("run finished")
#content = []
#with open("BH_CP2\\notes\sample.txt", 'r+') as file:
#    for line in file:
#        content.append(line.strip())

#    index = content.index('Tia')
#    content[index] = "Torii"
 
#    file.truncate(0)

#    for name in content:
#        file.write(name + "\n")

#print ("Code ends")

import csv
with open("BH_CP2\\notes\sample.csv", 'w', newline='') as csvfile:
    fieldnames = ['username', 'favorite color']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow(fieldnames)
    writer.writerow(["cosmic_voyager", "indigo"])
    writer.writerow(["tech_wizard", "turquoise"])

import os
os.remove