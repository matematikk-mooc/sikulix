# sikulix
Automated sikulix test scripts. 

Since Canvas updates their code every three weeks, the MatematikkMOOC-design risk breaking up at the same intervalls. 
To be able to detect a breakage, we have made automated test scripts with Sikulix. They work by comparing images from a previous 
GUI with images from the current GUI. Since the comparison is done pixelwise, screen resolution and web browser will probably 
come into account. The first tests are made using Firefox. 

1. Install http://sikulix.com/ 
2. Start Firefox and log in to Canvas.
3. cd into the directory where the tc1.sikuli ...tcn.sikuli  test scripts are.
4. Run the command ../runsikulix tc1 tc2 ... tcn
5. Observe the magic and keep an eye on the text output from the scripts whether any tests fail.

