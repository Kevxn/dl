#download calc
import datetime
import time 
import sys

def main(choice):
	my_speed = 38
	if choice[1] == '-d':
		filesize_in_gb = float(choice[2])
		filesize_in_mb = filesize_in_gb * 1024
		filesize_in_megabits = filesize_in_mb * 8
		time_to_download = filesize_in_megabits / my_speed # in seconds
		_time = datetime.timedelta(seconds = time_to_download)
		seconds = _time.total_seconds()
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60
		print("{} hours\n{} mins\n{} seconds".format(int(hours), int(minutes), int(seconds)))

main(sys.argv)
