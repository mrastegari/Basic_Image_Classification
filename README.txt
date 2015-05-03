


===============================================================================
=                              Coding Challenge                               =
===============================================================================

Your challenge is to implement a miniature shape classifier that can be trained and tested on the provided datasets. You may not finish everything in the time allotted, but you should try to get as far as you can. If you have questions about any part of the challenge, feel free to call me (Ken) at 706-318-1019 anytime between 9 AM PST and 11:30 PM PST.



===============================================================================
=                               Initial Setup                                 =
===============================================================================

You're going to be coding in Python. If you don't already know python, it's easy enough to pick up that it shouldn't be a significant friction point. To make things easy, download the ready-made enthought python distribution: https://www.enthought.com/downloads/

Helpful debugging tip: run your program from the command line using:


ipython --pdb --pprint --automagic --no-confirm-exit --colors=Linux


Once at the prompt, type "run main.py". After your program executes, you will have access to all variables you set at the outermost scope of the program. If there are exceptions, it will automatically drop into debugger so that you can examine variable contents. If you want to set a breakpoint, add this line to your code:


from IPython.core.debugger import Pdb; Pdb(color_scheme='Linux').set_trace()


You're going to be doing a lot of array and image manipulation work. Numpy is the library of choice for manipulating arrays. Here's some example code you might find helpful:


import numpy foo = numpy.zeros((5,5), dtype='float')


# returns 5x5 array of floats

array([[ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.]])


foo.max()

foo.sum() do what you expect


Selecting a subsection of an array looks like this:


bar = foo[0:2,0:2]
# bar now contains top left 2x2 of foo


# You can do assignment this way too:


foo[0:2,0:2] = 1.
# sets top left elements to 1

array([[ 1.,  1.,  0.,  0.,  0.],

       [ 1.,  1.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.]])


# You can also do element-wise math:

foo[0:2,0:2] *= 2

array([[ 2.,  2.,  0.,  0.,  0.],

       [ 2.,  2.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.],

       [ 0.,  0.,  0.,  0.,  0.]])


To quickly visualize the contents of an array, you can run:


from scipy.misc.pilutil import toimage

toimage(foo).show()

# or to save the image to disk

toimage(foo).save('foo.png')


That should be enough to get you rolling in python.



===============================================================================
=                            Training and Testing                             =
===============================================================================

Attached is an image data set of 5 categories of shapes. You will extract features from the training images, train a classifier, and test your classifier on each of the five test datasets. We have provided you with some starter code to help with loading images and reporting test results. Please take a minute to read through each of the provided files and understand what's going on. Your primary task is to implement the methods in classifier.py, but you are free to modify any of the files. 

To train your classifier, store features with pixel sizes between 3x3 and 8x8. We recommend using a 2d correlation function to perform a sliding window match of your saved features. Scipy has already implemented this for you:

http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html

By being clever with how you pick and manipulate features and what you do with the correlation output, store a higher level representation of each of the 5 categories that you can use to classify the test images. We ask that you do not resort to counting the number of white pixels or the number of edges in your classifier. We prefer to see you write something that could work reasonably well when the test images are placed in a real-world environment, and counting is not robust to occlusion or clutter.

The five test datasets are designed to test the strengths and weaknesses of your classifier. Our goal is to see how you approach the problem of generalization and recognition under different conditions. It might seem difficult to try and recognize a square in many different positions when you have only trained on one position, but you have a good bit of flexibility in pre-training your classifier. For example, you may choose to train on translations of lines and then reuse the line features to achieve translation invariance in other shapes. 



===============================================================================
=                           What we're looking for                            =
===============================================================================

In your final submission we must be able to run "main.py" and observe the classification accuracy on each of the test datasets. We do not expect you to get 100% accuracy on all of them, and it is fine if you specialize and try to get high accuracy on just a couple. We do expect that your classifier can correctly recognize the training images and that it performs better than random at recognizing the test images. 

If you really want to impress us, here's what you can do:


- Demonstrate your thought process. Document what you tried and what you would like to try if given more time.

- Demonstrate your understanding of the problem. What are the tradeoffs you encountered? Did you make reasonable assumptions? Can you think of interesting test images that exploit the weaknesses of your classifier?

- Write clean, well organized, commented code. It doesn't need to be perfect, but it should demonstrate that you appreciate the quality of code required by a team environment.




Let me know if you have questions, and good luck!

~Ken










