# sikulix
Automated sikulix test scripts. 

Since Canvas updates their code every three weeks, the MatematikkMOOC-design risk breaking up at the same intervalls. 
To be able to detect a breakage, we have made automated test scripts with Sikulix. They work by comparing images from a previous 
GUI with images from the current GUI. Since the comparison is done pixelwise, screen resolution, web browser, computer type and os version can come into account. I have used

- Screen resolution 2560x1440
- Firefox 54.0 (64-bits)
- MacBook Pro (Retina, 13-tommers, late 2013), Graphics Intel Iris 1536 MB
- OSX El Capitan 10.11.6 (15G1510)

To run the tests: 

1. Import the test course (found in this directory) into Canvas and publish it.
2. Add a student to the course and go to the course page as that student, using Firefox as web browser.
3. Install http://sikulix.com/ 
4. Add the path to where you installed sikulix to your .bash_profile by adding a line like this:

   export PATH=~/sikulix:$PATH

5. cd into the directory where the tc1.sikuli ...tcn.sikuli  test scripts are.
6. Run the command ../runsikulix tc1 tc2 ... tcn
7. Observe the magic and keep an eye on the text output from the scripts whether any tests fail.

=Troubleshooting=
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
