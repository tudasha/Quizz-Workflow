<!-- Imported from FS Quiz. Delete this line to keep your edits when the import runs again. -->
# Solution 864

Question has been removed from the quiz\n\n
50 Hz filter has a time constant of 20 milliseconds (tf: num=[1], den=[0,02, 1] which is considered as its delay, increasing the total loop delay to 30 + 20 = 50 ms or x 1,667.\n
So, to get same overshoot you need to dial down proportional gain x 1,667 which is 100/1,667 = 59,988.\n
Other stability evaluation methods can be used but should give similar result, thus tolerance in the answer.
