import time
import numpy as np

def process_stars(star_id):
    """
    Simulate waiting 5 seconds per star to process
    """
    print('Processing: ' + star_id + '\n')
    time.sleep(5)
    print('Star processed\n')

def process_stars_unique(star_id, image_size):
    """
    Simulate waiting longer for bigger images.
    """
    print('Processing: ' + star_id + '\n')
    time.sleep(image_size)
    print(f'Star processed in {image_size} seconds\n')
    return (star_id, image_size)

def fast_task(x):
    return x ** 2

def slow_task(x):
    time.sleep(1)

def get_Mv(mv, d):
  """
  mv: apparent magnitude
  d: distance (pc)
  name: name of star
  """
  Mv = mv - 5*np.log10(d) + 5
  time.sleep(1)
  return Mv