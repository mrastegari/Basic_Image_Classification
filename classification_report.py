
from string import ljust



class ClassificationReport(object):
  
  def __init__(self, title):
    self.title = title
    self.category_counts = {}
    self.errors = {}
  
  def append_result(self, recognized_category, target_category, filename):
    """ Saves the given classification result. """
    if target_category not in self.category_counts:
      self.category_counts[target_category] = 0
      self.errors[target_category] = []
      
    self.category_counts[target_category] += 1
    if target_category != recognized_category:
      self.errors[target_category].append((recognized_category, filename))
      
  def extend(self, other_report):
    """ Appends all of the results in the other_report to this report. """
    for category in other_report.category_counts:
      if category not in self.category_counts:
        self.category_counts[category] = 0
        self.errors[category] = []
        
      self.category_counts[category] += other_report.category_counts[category]
      self.errors[category] += other_report.errors[category]
      
  def print_summary(self):
    """ Prints the recognition accuracy of each category and the total. """
    
    print '<>' * 40
    print
    print self.title
    print
    
    total_num_imgs = 0
    total_num_correct = 0
    for category in self.category_counts:
      num_imgs = self.category_counts[category]
      num_correct = num_imgs - len(self.errors[category])
      pct_correct = round(100 * float(num_correct) / num_imgs)
      print "%s (%s / %s) = %s%% correct" % \
            (ljust(category, 10), num_correct, num_imgs, pct_correct)
      
      total_num_imgs += num_imgs
      total_num_correct += num_correct
      
    total_pct_correct = round(100 * float(total_num_correct) / total_num_imgs)
    print "\nTotal      (%s / %s) = %s%% correct" % \
          (total_num_correct, total_num_imgs, total_pct_correct)
    
    print
    print '<>' * 40
    
  def print_errors(self):
    """ Prints the errors in each category. """
    
    print '<>' * 40
    print
    print self.title
    
    for category, errors in self.errors.items():
      print
      print '"%s" was recognized as:' % category
      print
      
      for error in errors:
        print "%s (%s)" % error
        
      print
      print '-' * 80
      
    print '<>' * 40



