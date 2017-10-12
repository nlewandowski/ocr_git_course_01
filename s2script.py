import csv
import s2sphere as s2

def getParentLvl13(s2c):
  return s2c.id().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent().parent()


driverPos = list()
dropOffPos = list()
pickUpPos = list()

inputfile = '/home/administrateur/Workspace/results-20170726-154612.csv'
with open(inputfile, 'r') as csvfile:
   posreader=csv.reader(csvfile, delimiter=',')
   for row in posreader:
     #print(row)
     mDriverPos = s2.LatLng.from_degrees(float(row[0]), float(row[1]))
     mDropOffPos = s2.LatLng.from_degrees(float(row[2]), float(row[3]))
     mPickUpPos = s2.LatLng.from_degrees(float(row[4]), float(row[5]))
     driverPos.append([str(row[0]), str(row[1]), str(getParentLvl13(s2.Cell.from_lat_lng(mDriverPos))).split(' ')[1][:8]])
     dropOffPos.append([str(row[2]), str(row[3]), str(getParentLvl13(s2.Cell.from_lat_lng(mDropOffPos))).split(' ')[1][:8]])
     pickUpPos.append([str(row[4]), str(row[5]), str(getParentLvl13(s2.Cell.from_lat_lng(mPickUpPos))).split(' ')[1][:8]])

with open('/home/administrateur/Workspace/drivers.csv', 'w') as driverFile:
  driverWriter=csv.writer(driverFile, delimiter=',')
  driverWriter.writerows(driverPos)

with open('/home/administrateur/Workspace/dropoff.csv', 'w') as dropoffFile:
  dropoffWriter=csv.writer(dropoffFile, delimiter=',')
  dropoffWriter.writerows(dropOffPos)

with open('/home/administrateur/Workspace/pickup.csv', 'w') as pickupFile:
  pickupWriter=csv.writer(pickupFile, delimiter=',')
  pickupWriter.writerows(pickUpPos)

