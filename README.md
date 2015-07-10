A simulation program for CRS pre-enlistment module. 
The program will try to predict what subjects you will get after the batch run. 
It will also show your chances of getting each subject on average. 
This is (hopefully) a better version of the first CRS Simulation. 
This is not a 100% accurate prediction. 
This is just to get an idea of your chances of getting units during the batch run.

----------------
HOW TO USE
----------------

Running the program
------------------------

To use the program, simply run the "run.py" (requires Python 2.7) along with some arguments:

python run.py [save file] [num runs, default = 1]

examples: (try running them yourself) [save.csv is already provided as an example]

python run.py save.csv			
(loads the subjects in save.csv and does a batch run once)

python run.py save.csv 1000
(does 1000 batch runs, high number of batch run is for a more accurate average)

python run.py save.csv 100 > results.txt
(output the results to results.txt instead of on the terminal)



Save file
----------

The save file is a file that contains the details of your desired classes.
You'll need a save file to run the program.
The save file is a .csv file(or really any file format like .txt, etc.)

See save.csv for an example (open using a text editor) 
(note: csv is usually opened by a spreadsheet program by default like Excel)
(that works too but if you edit using Excel or something, 
you have to export it as .csv since the program can't read .xls files an such)


Writing your own save file
-------------------------------

This is very easy, you just have to know the format.

Open a text editor and save the file as a .csv  (.txt also works)

Each line describes a class that you want to enlist on, listed by ranking.

line 1 describes your chosen class at rank 1, line 2 = rank 2, etc.

Each line is composed of several arguments separated by commas.

The format is as follows

[Subject/Class Name], [Section], [Available Slots], [Demand], [Units], [optional: Conflicting Sections]

examples:

CS 21,  THQR,   15, 7,  4.0,    THQ,    THR
Math 54, WFQ2THR12, 20, 42, 5.0, WFQ, THR, THQR, WFQR
CS 32, THU-1, 15, 96, 3.0, THU

Explanation:

Class Name - the name of the subject. ex. CS 21, make sure that your subject names are consistent.
if you use "CS 21" then don't use "CS21" (no space) or "cs 21" (lowercase), etc. to refer to the same subject.

The class name is important because if you are granted a slot in a higher ranked class,  your slots in a lower ranked class of the same name will be cancelled.
This is how CRS works. The program checks this by string comparison (e.g. name1 == name2)
If your naming of subjects is not consistent, you might get multiple classes of the same subject during the simulation.


Section - this is the section code for that class. ex. THQR
Again, be consistent in this because this is also used for ranking.
(same section == same timeslot, even if they're different subjects)


Available slots - these are the available slots. Make sure to put the Available slots and not the Total slots.
For example, if the AvailableSlots/TotalSlots/Demand is 18/20/30, write 18 instead of 20.
This is the value that will be used to calculate probabilities


Demand - the demand on a subject


Credits - how many units a subject is. Write 0.0 for NTSP or PE. CRS will not grant you more than 20 units (overload). That is also taken into account in this program


Conflicting sections (optional) - these are the other sections that share timeslot with the subject.
For example:

THQR conflicts with THQ and THR so you should also add it at the end of the line.
THU-1 would conflict with THU, so you should also write THU
WFQ2THR12 conflicts with other WFQ#THR##, so you should add WFQ and THR
(you don't have to add each WFQ#THR##, just the common substrings WFQ and THR would work)

Don't forget to put commas in between as a separator.



Interpretting the results
----------------------------

The batch run shows 2 results.

1. The results of n-batchruns
2. Summary of n-batchruns

1 shows the subjects granted to you during the simulation and the number of units you got.
The format printed is [Subject] [Section] [Slots/Demand] [Units]

Example result:

Run #1
Granted classes:

CS 32	THV-1	(3.0)
CS 21	THQR	(4.0)
ROTC 1	RANGER	(0.0)
FA 28	U	(3.0)
Total units: 10.0


2 shows some statistics regarding the n-batch run.

Example result:

Runs Summary (100 runs)
Average units:	11.13
Subject	Section	[Times Granted/Num runs]
CS 32	THV	(18/100)	18%
CS 32	THU-1	(11/100)	11%
CS 32	THU	(27/100)	27%
CS 32	THV-1	(44/100)	44%
CS 21	WFWX	(23/100)	23%
CS 21	WFUV-1	(14/100)	14%
CS 21	WFUV	(7/100)	7%
CS 21	THQR	(56/100)	56%
CS 21	WFQR	(0/100)	0%
ROTC 1	RANGER	(100/100)	100%
Anthro 10	THQ	(25/100)	25%
Math 54	WFQ2THR12	(18/100)	18%
Math 54	WFQ2THR11	(13/100)	13%
Math 54	WFQ2THR10	(6/100)	6%
FA 28	U	(51/100)	51%
Art Stud 1	WFR-2	(0/100)	0%

It shows how many times each unit was granted over the multiple batch run, as well as the average units.
As you can see, in the above example, the CS 21 classes have different probabilities.
The most likely class you will get is the THQR with 56%.
If you add the probabilities of the CS 21 classes, they add up to 100%, which means you're sure to get one of the CS 21 classes during the batch run.
Also, CS 21 WFQR has a 0% possibility. This is because CS 21 THQR has more slots than demand so the chance of getting it is 100%. 
Since THQR has a higher rank than WFQR, the WFQR class will never be granted. So you might as well cancel it.



Final words
-------------
Again, this is not 100% accurate. For one, I am not sure of the exact mechanics of the CRS.
And there are other factors not taken into account (like priorities to Graduating students)
This is meant only to serve as a guide. 
Also, follow at your own risk.
Do not blame me if you get few units even though the simulations say you have a high chance of getting units.
Since this is not yet tested, feedback would be helpful. (tell me if the program was accurate or if it wasn't after the assignment of slots)