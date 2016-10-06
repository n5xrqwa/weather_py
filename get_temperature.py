#!/usr/bin/python3
from sense_hat import SenseHat
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--screen", help="print to screen", action="store_true")
parser.add_argument("-l", "--line" , help="print single line to screen", action="store_true")
parser.add_argument("-o", "--outfile", help="append to file")
args = parser.parse_args()

fmt = "%Y-%m-%d %H:%M:%S %Z"
now = time.localtime()


sense = SenseHat()
temp = sense.get_temperature()
Fahrenheit = 9.0/5.0 * temp + 32
humidity = sense.get_humidity()
pressure = sense.get_pressure()
orientation = sense.get_orientation_degrees()
north = sense.get_compass()

sensedatafmt = "%s %.2fC %.2fF %.2frH %.2fmB"
sensedata  = (time.strftime(fmt, now), temp, Fahrenheit, humidity, pressure)

def screenprint():
        print("Time: %s" % time.strftime(fmt, now))
        print("Temp: %.2f C" % temp)
        print("Temp: %.2f F" % Fahrenheit)
        print("Humidity: %.2f %%rH" % humidity)
        print("Pressure: %.2f Millibars" % pressure)
        print("Pitch: {pitch:.2f}, Roll: {roll:.2f}, Yaw: {yaw:.2f}".format(**orientation))
        print("North: %.2f" % north)

# main
if args.screen :
	screenprint()
elif args.line :
  print (sensedatafmt % sensedata)
elif args.outfile :
	print(sensedatafmt % sensedata, file=open(args.outfile, 'a'))
else :
  parser.print_help()

