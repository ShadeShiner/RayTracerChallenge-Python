# RayTracerChallenge-Python
An implementation of a basic Ray Tracer from the book "The Ray Tracer Challenge" using the Python language.

https://en.wikipedia.org/wiki/Ray_tracing_(graphics)

The book explains what is Ray Tracing, the different aspects of how it is done, and test cases that must be passed for it to successfully work.
There is psuedocode that is presented so that the reader can use any language and I've decided to use the Python language. I am mostly using this
opportunity to learn a little bit of 3D Graphics even if it is not math heavy.

I have chose Python for the following reasons:
  * I am most proficient with Python.
  * I can implement most of psuedocode quickly.
  * It is cross platform and easy to run
  * Taking the opportunity to learn Cucumber and the Gherkin testing methodology.

To run the tests and validate the code:
  * Install Python 3
  * Using PIP, install the required packages with the following command line statement: "pip install -r requirements.txt"
  * Enter "behave" as the next command line statement and it will run all the tests that have been created at this point.

There is also a C language equivalent version of this repository that was used to investigate and learn C.
https://github.com/ShadeShiner/RayTracerChallenge-C

Generated images from this project can be seen within the /src/generated_images/ directory path. The images are in the .ppm format, so a program like GIMP can open this file successfully. There is converters that can be found online as well.
