
from dataset_iterator import DatasetIterator, get_image_size
from classification_report import ClassificationReport
import os



class Experiment(object):
  """ Manages the training and testing of a classifier on different datasets. """
  
  def __init__(self, classifier):
    self.classifier = classifier
  
  def train(self, dataset_path):
    """ Loads the images from the dataset and trains the classifier on them. """
    
    self.classifier.prepare_for_training(get_image_size(dataset_path))
    
    img_iter = DatasetIterator(dataset_path)
    for image, category, filename in img_iter:
      self.classifier.learn_image(image, category)
    
    self.classifier.finish_training()
      
  def test(self, dataset_path):
    """ Loads the images from the dataset and tests the classifier on them. 
    Returns a report of the classification results. """
    
    img_iter = DatasetIterator(dataset_path)
    title = os.path.split(dataset_path)[1] + ' dataset'
    report = ClassificationReport(title)
    
    for image, category, filename in img_iter:
      recognized_category = self.classifier.classify(image)
      report.append_result(recognized_category, category, filename)
    
    return report


