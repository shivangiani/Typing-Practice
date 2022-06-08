
import matplotlib.pyplot as plt 

import time as t

# an empty list to store the time and accuracy of each attempts 
times = []
attempt = []
mistakes = 0 # to calculate number of wrong attempts
wrong_words = 0 # to calculate number of wrong words


print("\n\n\n  *******  INSTRUCTIONS  *******  \n")
print("  1. You will have to type faster.")
print("  2. You will have to type a word of your choice or a sentence.")
print("  3. Type as fast as you can for five times")
print("  4. Take care of the the captial and small letters.\n")
input("  Press enter to continue\n")
practice_line = input("  Enter your word or sentence \n\n  ") # input the word or sentence
print("______________________________________")
print("\n\n")

line = practice_line
l = line.split() 
length = len(l)
total_words = 5 * length


while len(times) < 5:
     num = 0
     start = t.time() # to get the start time from timestamp
     word = input("Type here :  ")
     end = t.time()  # to get the end time 
     time_elapsed = end - start
     
     times.append(time_elapsed) 
      
     # to calculate the number of mistakes 
     
     if(word != practice_line):
          mistakes += 1
     
     wd = word
     w= wd.split()

     # to calculate number of wrong words
     for i  in range(0,len(w)) :
          if( w[i] != l[i]):
               wrong_words +=1
               num += 1
     
     attempt.append(((length - num) * 100 )/ length) # calculating accuracy of each attempt

accuracy = ((total_words - wrong_words) * 100 )/ total_words # calculating overall accuracy

print("______________________________________")
print("\n\n\n  ******* RESULT *******\n\n")
print("  1. There are 5 attempts. Any type of mistake is included in wrong attempt.")
print("  2. The time evolution is in seconds")
print("  3. Accuracy is in percentage \n")

print("  Number of words wrong : " + str(wrong_words) + " out of words " + str(total_words) )
print("  Accuracy : " + str(accuracy))
print("______________________________________\n\n")
print("\n  NOW LET'S SEE YOUR EVOLUTION GRAPHICALLY ")

# instead of showing chart immediately
# lets wait 3 seconds so user can read these sentences
t.sleep(3) 

# graphical report of time evolution 
# We take two axis x and y
x = [1,2,3,4,5]
y = times

legend = ["1" , "2" , "3" , "4" , "5" ]

#function is used to get or set the current tick locations and labels of the x-axis.
plt.xticks(x , legend)
plt.ylabel('Time in seconds')
plt.xlabel("No of Attempts")
plt.title('Your Typing Evolution')
plt.plot(x,y) # to plot the the graph 
plt.show() # to display the graph


# graphical report of attempt vise accuracy 
x = [1,2,3,4,5]
y = attempt

legend1 = ["attempt 1" , "attempt 2" , "attempt 3" , "attempt 4" , "attempt 5"]

plt.xticks(x,legend1)
plt.xlabel(" No of attempts ")
plt.ylabel("Percentage")
plt.title(" Your Attempt Accuracy Evoultion ")
plt.ylim(0, 100)
plt.bar(x,y) # plot the bar graph
plt.show()

# graphical report of overall accuracy
x = [1 , 2 , 3 ]
y = [0 ,accuracy, 0]

ledgend2 = [" " , "accuracy bar" , " "]

plt.xticks(x,ledgend2)
plt.ylabel("Percentage")
plt.title(" Your Overall Accuracy Evolution")
plt.ylim(0, 100) # set the limits of y axis 
plt.bar(x,y)
plt.show()