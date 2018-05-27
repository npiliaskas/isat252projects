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

def mpg(kpl):
  return kpl / 1.6093 / 0.264172

def kpl(mpg):
  return mpg * 1.6093 * 0.264172

#from Morgan Benton code example (email)
#create car class
class car: 

  def __init__(self, mpg = "", kpl = ""):
    self.miles_per_gallon = mpg
    self.kilometers_per_litter = kpl

    if mpg is None and kpl is None:
      print("input a mileage value")
    elif mpg is None:
      def mpg(kpl):
        return kpl / 1.6093 / 0.264172
    elif kpl is None:
      def kpl(mpg):
        return mpg * 1.6093 * 0.264172


