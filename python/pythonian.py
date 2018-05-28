#basic code structure of project from...
#https://github.com/morphatic/isat252u18examples/blob/master/python/converter/converter.py
#and 
#https://github.com/morphatic/isat252u18examples/blob/master/python/lms/student.py

#convert kilometers to miles
def kpm(m):
  return m * 1.6093

#convert miles to kilometers 
mpk = lambda k : k / 1.6093

#convert gallons to litters 
def gpl(g):
  return g / 0.264172

#convert litters to gallons 
def lpg(l):
  return l * 0.264172


#from Morgan Benton code example (email)
#create car class
class car: 

  def __init__(self, mpg = None, kpl = None):
    if mpg is None and kpl is None:
      self.mpg = 0
      self.kpl = 0
    elif mpg is None:
      self.mpg = mpk(gpl(kpl))
      self.kpl = kpl
    elif kpl is None:
      self.mpg = mpg
      self.kpl = kpm(lpg(mpg))