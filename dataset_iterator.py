
import os
from PIL import Image



def DatasetIterator(dataset_path):
  """ A simple iterator for retrieving the images of a dataset. """
  
  for category in os.listdir(dataset_path):
    category_path = os.path.join(dataset_path, category)
    if not os.path.isdir(category_path): continue
    
    for img_filename in os.listdir(category_path):
      img_path = os.path.join(category_path, img_filename)
      if os.path.isdir(img_path): continue
      
      if img_filename.split('.')[-1] =='png':
        yield Image.open(img_path), category, img_path


def get_image_size(dataset_path):
  """ Returns the image size of the given dataset as a (width, height) tuple. """
  # Find the first image and return its size.
  iter = DatasetIterator(dataset_path)
  image, category, filename = iter.next()
  return image.size
