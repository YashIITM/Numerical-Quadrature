import time


def TicTocGenerator():
  # Function that returns time differences
  ti = 0           # initial time
  tf = time.time() # final time
  while True:
    ti = tf
    tf = time.time()
    yield (tf-ti)   #Returns the time difference

TicToc = TicTocGenerator()  #create an instance of the TicTocGenerator

# Main function through which we define both tic() and toc()
def toc(tempBool = True):
  # Prints the time difference yielded by instance of TicTocGenerator()-TicToc
  tempTimeInterval = next(TicToc)
  if tempBool:
    print("Elapsed time: %f seconds.\n" %tempTimeInterval)

def tic():
  # Records a time in TicToc, marks the beginning of a time interval
  toc(False)
