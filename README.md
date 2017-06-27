# sikulix
Automated sikulix test scripts. 

Since Canvas updates their code every three weeks, the MatematikkMOOC-design risk breaking up at the same intervalls. 
To be able to detect a breakage, we have made automated test scripts with Sikulix. They work by comparing images from a previous 
GUI with images from the current GUI. Since the comparison is done pixelwise, screen resolution and web browser will probably 
come into account. The first tests are made using Firefox. 

1. Install http://sikulix.com/ 
2. Add the path to where you installed sikulix to your .bash_profile by adding a line like this:

   export PATH=~/sikulix:$PATH

3. Start Firefox and log in to Canvas.
4. cd into the directory where the tc1.sikuli ...tcn.sikuli  test scripts are.
5. Run the command ../runsikulix tc1 tc2 ... tcn
6. Observe the magic and keep an eye on the text output from the scripts whether any tests fail.

In the example below, sikulix reports a mismatch between the snapshot taken in Firefox and the image 1498213743797.png. 

```Bash
$ runsikulix -r tc1
running SikuliX: /Applications/SikuliX.app/Contents/Java/sikulix.jar -r tc1
.===
TC1
Test scroll event list.
Prerequisite: TC0
[log] App.open [0:Firefox]
[error] script [ /Users/erlendthune/github/sikulix/tc1.sikuli ] stopped with error in line 12
[error] FindFailed ( 1498213743797.png: (27x20) in R[1579,408 348x357]@S(0) E:Y, T:3,0 )
```

When a test fails like this, Firefox remains open where the test failed, and you can open the image sikulix used in the comparison in 
the tc1.sikuli directory:

```Bash
$ cd tc1.sikuli
$ ls
1498213743797.png	tc1.html
1498213773508.png	tc1.py
$ edit 1498213743797.png
```

Comparing the image with Firefox should reveal what is wrong. If the difference is subtle it might be an idea to use an image comparison program.
