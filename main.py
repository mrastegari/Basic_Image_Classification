
from classifier import Classifier
from experiment import Experiment
from classification_report import ClassificationReport
from IPython.core.debugger import Pdb;


def main():
  """ This is the main entry point for training and testing your classifier. """
  classifier = Classifier()
  experiment = Experiment(classifier)
  experiment.train('training')
  
  # Sanity check. Should get 100% on the training images. 
  report = experiment.test('training')
  report.print_summary()
  
  Pdb.set_trace()

  test_datasets = 'translations rotations scales noise occlusion distortion blurry_checkers'
  final_report = ClassificationReport("All Datasets")
  
  # Print the classification results of each test
  for dataset in test_datasets.split():
    report = experiment.test('testing/' + dataset)
    report.print_summary()
    #report.print_errors() # Uncomment this to print the error images for debugging. 
    final_report.extend(report)
  
  final_report.print_summary()


  
if __name__ == '__main__':
  main()
  
  
