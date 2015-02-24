import pylab as plt
import numpy as np
from processE3Data import E3Data

class E3DataPlotter:
	def __init__(self,title,e3data):
		self.e3data = e3data
		self.title = title

	def plot(self,outputFigure):
		#init the plot
		fig, ax = plt.subplots()
		index = np.arange(len (self.e3data.data))
		bar_width = 1
		ax.plot(index,self.e3data.data,color='red')
		ax.set_ylabel("%s value" %(self.e3data.dataType))
		if(self.e3data.dataType =="HR"):
			ax.set_xlabel("Time (seconds) ")
		else:
			ax.set_xlabel("Values ( HZ: %s )" % ( str(self.e3data.samplingRate)))
		ax.set_title(self.title)
		plt.grid(True)
		plt.savefig(outputFigure)

if __name__ == "__main__":
	e3data = E3Data.newE3DataFromFilePath(E3Data,"HR.csv","HR") 
	e3plot = E3DataPlotter("HR values for subject S7, all",e3data)
	e3plot.plot("s7_e3_hr_all")
