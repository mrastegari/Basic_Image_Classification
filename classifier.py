
import random



class Classifier(object):
  """ You need to implement this class. """
  
  def prepare_for_training(self, image_size):
    """ Called immediately before training begins. You can use this method
    to initialize any needed structures or objects. """
    self.image_size = image_size
    self.categories = []

  def learn_image(self, image, category):
    """ This method is called exactly once for each image in the training
    dataset. This is where you should process the image and store it so that 
    it can be recognized again later. """
    self.categories.append(category)
    
  def finish_training(self):
    """ Called immediately after training completes. You can use this method
    to prepare for testing. """
    
  def classify(self, image):
    """ Called on each image in the test dataset after training is complete.
    Returns the category of the given image. """
    
    # For now return a random winner. 
    return random.choice(self.categories)


