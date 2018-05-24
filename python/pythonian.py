#basic code structure of project from...
#https://github.com/morphatic/isat252u18examples/blob/master/python/converter/converter.py
#and 
#https://github.com/morphatic/isat252u18examples/blob/master/python/lms/student.py

#convert kilometers to miles
def kpm(m):
  return m * 1.6093

#convert miles to kilometers
def mpk(k):
  return k / 1.6093  

#convert gallons to liters 
def gpl(g):
  return g / 0.264172

#convert liters to gallons 
def lpg(l):
  return l * 0.264172

#compute gas usage (gallons) per miles and kilometers 
def __init__(self, mpg = "", kpg = ""):
    self.miles_per_gallon = mpg
    self.kilometers_per_gallon = kpg

#compute gas usage (litters) per miles and kilometers
def __init__(self, mpl = "", kpl = ""):
    self.miles_per_litter = mpl
    self.kilometers_per_litter = kpl

#compute gallons per litters and visa versa
def __init__(self, gpl = "", lpg = ""):
    self.gallons_per_litters = gpl
    self.litters_per_gallon = lpg

#^^^EVERYTHING HERE UP IS GOOD!^^^   