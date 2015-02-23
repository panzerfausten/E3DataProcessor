from processE3Data import E3Data
import datetime
#slide sample data

e3data = E3Data.newE3DataFromFilePath(E3Data,"ACC.csv","ACC")
slide   = e3data.getSlide(3254,3428)
slide.saveToFile("data/s7_e3_acc_3.csv")
print slide.toString(False)

e3data = E3Data.newE3DataFromFilePath(E3Data,"BVP.csv","BVP")
slide   = e3data.getSlide(3254,3428)
slide.saveToFile("data/s7_e3_bvp_3.csv")
print slide.toString(False)

e3data = E3Data.newE3DataFromFilePath(E3Data,"EDA.csv","EDA")
slide   = e3data.getSlide(3254,3428)
slide.saveToFile("data/s7_e3_eda_3.csv")
print slide.toString(False)

e3data = E3Data.newE3DataFromFilePath(E3Data,"TEMP.csv","TEMP")
slide   = e3data.getSlide(3254,3428)
slide.saveToFile("data/s7_e3_temp_3.csv")
print slide.toString(False)

