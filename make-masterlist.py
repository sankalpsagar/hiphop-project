import billboard
import time
def driver():
	iniyear = '2005'
	endyear = '2005'
	filepath = '/home/ed3n/projects/HipHop/test'
	makefile(iniyear, endyear, filepath)

def makefile (iniyear, endyear, filepath):
	f = open(filepath, 'w')
	chart = billboard.ChartData('r-b-hip-hop-songs', '{}-01-01'.format(iniyear))

	while chart.nextDate.split("-")[0] != endyear:
		f.write("Date: {}\n\n".format(chart.date))
		for songs in chart:
			f.write("{} | {} | {} \n".format(songs.title, songs.artist, songs.weeks))
		time.sleep(5)
		f.write("\n\n")
		chart = billboard.ChartData('r-b-hip-hop-songs', chart.nextDate)

	f.close()

print("Hang on tight!")
driver()
print("Woohoo, done.")