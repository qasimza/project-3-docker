Project#3: DOCKER
(Total Points: 10)
Do the following (Python is mentioned but you can use any language of your choice to complete the task):
1.	Start docker container from any image of your choice
2.	Install python so that the code written in python can be executed.
3.	Write a python script to read 2 text files (IF.txt &  Limerick-1.txt) from location: /home/data (inside your container)
4.	Python script should be able to do following:
a.	List name of all the text file at location: /home/data
b.	Read the two text files and count total number of words in each text files
c.	Add all the number of words to find the grand total (total number of words in both files)
d.	List the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
e.	Find the IP address of your machine
f.	Write all the output to a text file at location: /home/output/result.txt (inside your container).
g.	Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit.
5.	Make your container image as small as possible.
6.	Submit your image for evaluation in Canvas. 

How to submit your work:
1.	Create your final image (e.g. proj2docker_rk.tar)
2.	Upload it to Canvas.
3.	You can also copy the file to Sharepoint, Google Drive or OneDrive and provide your download link in the submission section in Canvas.
4.	Share the code in GitHub or as an attachment.  (2 points will be deducted for not sharing the code) (Example https://github.com/RashmiKasakar.)

Note: following steps will be followed while evaluating your work.
a.	I will be mapping a directory on my machine to location inside your container (/home/data) and run it.
b.	Step (a) will allow me to provide input to your code
c.	Upon running your container, I will get all the information about my input files through your code.

Hints:
1.	Watch the tutorial video on docker posted and follow the example used to get the size of google page size.   See W6C1 LinkedIn Learning Docker.pdf.  Please use UC email address to access: https://www.linkedin.com/learning/learning-docker-2/what-is-docker?u=2133849

1.	You can map a local directory on your laptop with all the input text file to your container at location /home/data using following command (see docker documentation for more detail about the command below because it is not complete example):
a.	docker run -v /mylaptop/dir:/home/data
2.	Once you have completed your container, you can use alpine image to make the size of your image smaller (as shown in the tutorial video)
