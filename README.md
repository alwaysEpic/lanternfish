# lanternfish

All answers have been answered in the word document.

PART1

I have included the arrays noted in the word document as files to run.
testfile.txt is the small list used for the examples in the text.
providedData.txt is the noted test data

fishSchool.py [Number of Days to Simulate] [Fish School Data File]

e.g.

python3 fishSchool_recursive.py 80 testFile.txt

python3 fishSchool_alltheloops.py 80 providedData.txt

There are a number of comments in the file to explain my thought process

fishSchool_recursive was my first build

fishSchool_alltheloops was the second

fishSchool_optimized was where I tried to optimize enough for the massive exponential issue, and it didn't work

Each python script works for Part 1, they do not work for Part 2

PART2

After no luck in optimizing the python algorithm, I slept on it and decided to try C the next day. I realized halfway through the process that I should be using a rotation of bins. This could also be written in Python

I have built test programs for linux, mac and windows.  

Mac: ./fishApp_mac [number of days to simulate] [Fish School Data File]

Linux: ./fishApp_linux [number of days to simulate] [Fish School Data File]

Windows: fishSchool [number of days to simulate] [Fish School Data File]

e.g.

./fishApp_linux 80 testFile.txt

./fishApp_mac 256 providedData.txt

The file is simple as well and can be rebuilt using:

 g++ fishSchool.cpp -o [name of app]
