
#  Student Projects 2013

## Project goals

small experiments of **geometric model extraction** from 2D and *3D medical images*

including:

+	image enhancement (webimaging)
+	image segmentation (webimagesegmenting)
+	block decomposition (webimagepartitioning)
+	linear algebraic representation (weblarmodeling)
+	boundary extraction (webmodelboundary)
+	model smoothing (webmodelsmoothing)
+	internal/external hierarchical decomposition (webprogressive)
+	model rendering (webrendering)


## Project framework

-	on-going development of the new standard [**IEEE-SA P3333.2**](http://standards.ieee.org/develop/project/3333.2.html) for “Three-Dimensional Model Creation Using Unprocessed 3D Medical Data”

## IEEE-SA P3333.2 

This standard establishes the minimum requirements for enabling portability and consistent display of 3-D medical images across dedicated 3D display equipment, computers, mobile smart pads and smart phones. 

This includes standardization of volume image rendering (texture), collaboration of fragmented images and 3D models, data storage, data compression, data transport, motion simulation, 3D platforms, and 3D model management systems.

## IEEE-SA P3333.2 Working Group
### Advanced Corporate members

- Chosun University Hospital 
- Electronics & Telecommunications Research Institute 
- Gwangju Technopark 
- Korea Electronics Association 
- Korean Agency for Technology & Standards 
- LG Electronics 
- Osaka University 
- Roma Tre University 
- Siliconfile Technologies Inc. 


## DICOM: the current standard (From Wikipedia)
### Digital Imaging and Communications in Medicine

+	It is a standard for handling, storing, printing, and transmitting information in medical imaging. 

+	It includes a file format definition and a network communications protocol. 

+	The communication protocol is an application protocol that uses TCP/IP to communicate between systems. 

+	DICOM files can be exchanged between two entities that are capable of receiving image and patient data in DICOM format.

+	DICOM enables the integration of scanners, servers, workstations, printers, and network hardware from multiple manufacturers into a *picture archiving and communication system* ([**PACS**](http://en.wikipedia.org/wiki/Picture_Archiving_and_Communication_System)).



# Software infrastructure

## languages

+ 	Python 2.7
	
	*	for first prototyping (testing and debugging)
	*	first and second project milestone (end of March, end of April)
	

+ 	Javascript + several libraries + plasm.js

	*	for porting (line by line, when possible) to the web platform 
	*	third project milestone (end of May)

## Integrated Development environment (IDE)

+	[*ipython*](http://ipython.org/)

	provides a rich architecture for interactive computing
	
+	platform specific IDE

	+	[*Eclipse*](http://www.eclipse.org/) : to provide a universal toolset for development.
	+	[*Visual Studio*](www.microsoft.com/visualstudio/eng) :  integrated development environment (IDE) from Microsoft
	+	[*Xcode*](developer.apple.com/technologies/tools/whats-new.html) : toolset for building OS X and iOS applications
	

+	web development

	+	[*Sublime Text 2*](http://www.sublimetext.com/)
	

## Revision Control System

+	[*Git*](http://git-scm.com/)

	developed by Linus Torvald to manage the development of the Linux kernel

+	[*GitHub*](https://github.com/)

	web-based hosting service for software development projects that use the Git revision control system

##	Python Libraries

+ 	[*pyplasm*](http://www.plasm.net/) : functional language for computing with geometry
+ 	[*larpy*](https://github.com/cvdlab/larpy) : linear algebraic representation of geometry -- in development
+ 	[*scipy*](http://www.scipy.org/) : scientific computing with Python 
+ 	[*matplotlib*](http://matplotlib.org/) : python 2D plotting library for publication quality figures 
+ 	[*PIL*](http://www.pythonware.com/products/pil/) : adds image processing capabilities to Python interpreter
+ 	[*biopython*](http://biopython.org/wiki/Main_Page) : set of freely available tools for biological computation written in Python 
+	[*pydicom*](https://code.google.com/p/pydicom/) : python package for working with DICOM files

##	Software tools (hopefully :o)


+	[*materialise*](http://biomedical.materialise.com/)

	Biomedical software and solutions for engineering on anatomy

	+	[*Mimics*](http://biomedical.materialise.com/mimics)

		Medical Image Segmentation for Engineering on Anatomy
		
	+	[*Mimics Student Edition*](http://biomedical.materialise.com/MimicsSE)
	
		An Interactive Way to Learn about 3D Medical Image Processing
		
