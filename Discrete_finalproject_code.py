# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import matplotlib.pyplot as plt
from matplotlib import image



import random #import random library 

"""
Function: And(); 
Does runs the and gate 
Truth table for an And Gate
----------------------------
 A B | A.B
 0 0 | 0
 0 1 | 0 
 1 0 | 0
 1 1 | 1
"""
def And(List_1, List_2 ):
    new_List=[ 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ]
  
    for i in range(0, len(List_1)):
      
        if  (List_1[i] == List_2[i]):
            new_List[i]=List_1[i]
            
        elif (List_1[i]<List_2[i]):
            new_List[i]=List_1[i]
            
        elif (List_1[i]>List_2[i]):
            new_List[i]=List_2[i]
        
    return  new_List
"""
Function: Or(); 
Does runs the and gate 
Truth table for an And Gate
----------------------------
 A B | A + B
 0 0 | 0
 0 1 | 1 
 1 0 | 1
 1 1 | 1    
"""    
def Or(List_1, List_2):
     new_List=[ 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ]
     for i in range(0, len(List_1)):
        
         if  (List_1[i] == List_2[i]):
             new_List[i]=List_1[i]
         elif (List_1[i]<List_2[i]):
             new_List[i]=List_2[i]
         elif( List_1[i]>List_2[i]):
             new_List[i]=List_1[i]
     return  new_List
"""
Function: Xor(); 
Does runs the and gate 
Truth table for an And Gate
----------------------------
 A B | A xor B
 0 0 | 0
 0 1 | 1 
 1 0 | 1
 1 1 | 0   
 """
def Xor(List_1, List_2):   
    new_List=[ 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ]
    for i in range(0, len(List_1)):
        if  (List_1[i] == List_2[i]):
            new_List[i]=0
        else:
            new_List[i]=1 
    return  new_List

"""
Function: Nor(); 
Does runs the and gate 
Truth table for an And Gate
----------------------------
 A B | A.B
 0 0 | 1
 0 1 | 0
 1 0 | 0
 1 1 | 0   
 """
def Nor(List_1, List_2):
    List= Or(List_1, List_2);
    for i in range(0,len(List)):
         if List[i]==0:
             List [i]= 1
         else:
             List[i]=0 
    return List 

"""
Function:   Nnd(); 
Does runs the and gate 
Truth table for an And Gate
----------------------------
 A B | A.B
 0 0 | 1
 0 1 | 1
 1 0 | 1
 1 1 | 0
"""
def Nand(List_1, List_2):
    List= And(List_1, List_2);
    for i in range(0,len(List)):
         if List[i]==0:
             List [i]= 1
         else:
             List[i]=0 
    return List 

"""
Function: XNor(); 
Does runs the and gate 
Truth table for an And Gate
----------------------------
 A B | A xor B
 0 0 | 1
 0 1 | 0
 1 0 | 0
 1 1 | 1 
 """
def Xnor(List_1, List_2):
    List= Xor(List_1, List_2);
    for i in range(0,len(List)):
         if List[i]==0:
             List [i]= 1
         else:
             List[i]=0 
    return List 
 
"""
Funtion: converts decimal number to an 8 bit binary number 
takes in a decimal number 
"""   

def convert_decimal_to_binary(num):
    
    #creating a list with empty values 
    List=[ 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ]
    
    
    #converting to 8 bit decimal if i is a + number 
    if (num >= 0 and num<=127 ):
        
        #creating a list that loops backwards because the answer 
        # is written in reverse order 
        for i in range(7,0,(-1)):
            
                #finding the remainder and new number each time 
                num_remainder= num%2
                num=num//2
                
                #replacing the list value with the remainder each loop 
                List[i]= num_remainder
                
                #continues to loop until answer is equal to 0 
                #if answer equal to 0 it return the rest of the positions on the
                #loop as 0 
                if (num==0):
                    break
        #returns the list of binary number         
        return List 
            
    #converting to 8 bit binary if its a -number 
    if (num <0 and num>=(-128)):
        num= num*-1
        
        for i in range(7,-1,(-1)):
                
                num_remainder= num%2
                num=num//2
                List[i]= num_remainder
                if (num==0):
                    break
       
        #find the complement by changing 0 to ones 
        for i in range(0,8,1):
             if List[i]==0:
                 List [i]= 1
             else:
                 List[i]=0 
       
        #finding the two complement by adding one. 
        List[7]=List[7]+1 
        if List[7]==2:
            for i in range(7,0,(-1)):
                if List[i]>=2:
                    List[i]=List[i]-2
                    List[i-1]= List[i-1]+1
            return List 
               
        
        else:
            return List 
        
        
    else:
        print("The decimal number entered is out of range")
        
"""
 Function: plotting the image 
"""      
def Image(List):
    
    fig, ax = plt.subplots(4, 2)
  
    
    for i in range(1,9):
        if List[i-1]== 1:
            plt.subplot(4, 2, i)
            plt.imshow(image.imread("image"+str(i-1)+".jpeg"))
            plt.axis('off')
        else:
            plt.subplot(4, 2, i)
            plt.imshow(image.imread("imgblack.jpeg"))
            plt.axis('off')
       
    plt.subplots_adjust(wspace=-0.705, hspace=0)
    plt.show()
    
    '''***************    Part 2- Probalility calculation***********
    We survey 60 college individuals and  used the daa to create  a probablility 
    estimate. We attached a csv file of the data collected to for efficiency purposes 
    we decidedto clean the data outside of python. This will compute the probaility of you 
    guessin the picture. 
    
    '''
    
    
def guessing_the_picture(List, skill, probPicture ):
    """
    the amount of people who know the answer based off lookingat the picture. 
    if over 50% of the picture is displayed is 
    """
    
    count=0 
    if probPicture==0: 
        for i in range(len(List)):
            if List[i]==1:
                count+=1 
        percent_displayed= float(count/ len(List))
        reveal= float(3/8)
        
        if percent_displayed >= reveal:
            if skill=="a":
                #the amount of novice people who knew thw name after seeing the picture were 9
                #the total novice people were 50
                #therefor the probability of knowing it after seeing the picture is 9/50 
                probPicture= float(9/50)
                
            
            elif skill=="b":
                #the amount of novice people who knew thw name after seeing the picture were 6
                #the total novice people were 10
                #therefor the probability of knowing it after seeing the picture is 6/10 
                probPicture= float(6/10)
            
        elif percent_displayed < reveal:
            probPicture=0 

    else: 
      probPicture= probPicture

    
    
    return probPicture


"""
 Function: probability of guessing after 1 hints
 
"""
def guessing_one_hint(skill):   
    """
    the amount of people who guessed it based off the first hint 


    """
    if skill=="a":
                #the amount of novice people who knew thw name after seeing the picture were 9
                #the total novice people were 50
                #therefor the probability of knowing it after seeing the picture is 9/50 
                probHint1= float(2/50)
                
            
    elif skill=="b":
                #the amount of novice people who knew thw name after seeing the picture were 6
                #the total novice people were 10
                #therefor the probability of knowing it after seeing the picture is 6/10 
                probHint1= float(1/11)
    return probHint1
    

"""
Function: probability of guessing after 2 hints
"""
def guessing_two_hint(skill): 
    """
    the amount of people who guessed it based off the second hint 
    
    """
    if skill=="a":
                #the amount of novice people who knew thw name after seeing the picture were 9
                #the total novice people were 50
                #therefor the probability of knowing it after seeing the picture is 9/50 
                probHint2= float(14/50)
                
            
    elif skill=="b":
                #the amount of novice people who knew thw name after seeing the picture were 6
                #the total novice people were 10
                #therefor the probability of knowing it after seeing the picture is 6/10 
                probHint2= float(2/11)
    return probHint2

"""
 Function: probability of total 
"""   
def Probability_total(probPicture, probHint1, probHint2, i):
 
   if i ==0:
       probTotal= probPicture
   elif i==1:
        probTotal=probPicture  + probHint1
   elif i==2:
       probTotal= probPicture+ probHint1+probHint2
  
   
   return probTotal

"""
Function: Keeps track of the total peices revealed each time 
"""
def get_pic_list(List, pic_list):
    
    for i in range(len(List)):
        if List[i]==1:
            pic_list[i]=1 
    print("the updated pic list", pic_list)
    return pic_list

if __name__ == "__main__":
    
    
    print("Welcome to Art Heist. The game that allows you to\
 use numbers and clues to guess the name of the stolen art.\n")
    print("\nBefore we start: Select a skill level.")
    while True: 
        
        skill= input("You will be retriving a 17th century art peice\nHow\
 knowlegeable are you with 17th CE art \na. novice \nb. Intermediate\
 \n___type'a' or 'b' withouth the quotations \n\n")
        skill= skill.lower()
        if ((skill != 'a' )and (skill != 'b')):
            print("\n\nMake sure you typed 'a' or 'b' withouth the quotations. Ensure no spaces after\n")
        else: 
            break
         
    
    print("\nHow to Play: \nStep 1: you chose two numbers between -128\
 and 127 and the computer generates a logic gate which would\
 determine what picture is turned on.")

    i=0 
    probPicture=0 
    probHint1=0
    probHint2=0
    pic_list=[0, 0, 0, 0, 0, 0 ,0 ,0 ]
    while(i<3): 
        
        #User Input for the first 2 numbers 
        while True: 
            try:
                decimal_num= int(input("Enter the first number(decimal number ex 1,2,3) \n"))
            except ValueError :
                print("Make sure you enter a whole decimal number ex 1,2,3,4..")
            else: 
                break
        while True: 
            try: 
                decimal_num2= int(input("Enter the second number(decimal number ex 1,2,3)\n"))
            except ValueError :
                print("Make sure you enter a whole decimal number ex 1,2,3,4..")
            else:
                break 
            
            
            
        #logic gates lists 
        Logic_gates= ["And", "Or", "Nor", "Nand", "Xor", "Nor" ]
        
        #using random library to determine which logic gate is used 
        Logic_gate= random.choice(Logic_gates)
        
       
     
        #turning the two decimal number into an 8 bit binary number 
        binary_num_1= convert_decimal_to_binary(decimal_num)
        print("The first number in binary is ",binary_num_1 )
        binary_num_2= convert_decimal_to_binary(decimal_num2)
        print ("The second number in binary is ",binary_num_2)
        
        
        #Computing the truth table 
        ans= eval(Logic_gate)(binary_num_1,binary_num_2);#convert string into a function using eval()
        print("The logic gate chosen for you is", Logic_gate, "and your truth \
table outputs\n", ans)
        
        
        #printing the image 
        Image(ans);
        user_ans= input("Guess the name of the Hidden Art(Don't include space at the end)\n")
        user_ans=user_ans.lower()
       
        
        #user trying to guess answer 
        if user_ans == "girl with a pearl earring":
            if i== 0:
               pic_list = get_pic_list(ans, pic_list)
               output=guessing_the_picture(pic_list, skill, probPicture)
               if output!=0:
                   print("the probabiliy of getting it right is e",output)
               else: 
                   print("There is not enough information available for me to calculate the probability from our data e/n")
            else: 
                 pic_list = get_pic_list(ans, pic_list)
                 probPicture=guessing_the_picture(pic_list, skill, probPicture)
                 probHint1=guessing_one_hint(skill)
                 probHint2=guessing_two_hint(skill)
                 output= Probability_total(probPicture, probHint1, probHint2)
                 if output!=0:
                     print("the probabiliy of getting it right is a",output)
                 else: 
                     print("There is not enough information available for me to calculate the probability from our data a/n")
                     
                     
            print("Congrats you found the stolen art!")
            
            break
        
        elif(i==2):
        
           print("Sorry you ran out of tries. The art 'girl with a pearl earring' remains stolen")
           List=[1,1,1,1,1,1,1,1];
           Image(List);
           pic_list = get_pic_list(ans, pic_list)
           probPicture=guessing_the_picture(pic_list, skill, probPicture)
           probHint1=guessing_one_hint(skill)
           probHint2=guessing_two_hint(skill)
           output= Probability_total(probPicture, probHint1, probHint2,i)
           if output!=0:
               print("\nthe probabiliy of getting it right is",round(output,2))
           else: 
               print("\nThere is not enough information available for me to calculate the probability from our data")
               
           
           
        else:
            if i== 0:
              
                
               pic_list = get_pic_list(ans,pic_list)
               output=guessing_the_picture(pic_list, skill, probPicture)
               if output!=0:
                   print("the probabiliy of getting it right is ",round(output,2))
               else: 
                   print("There is not enough information available for me to calculate the probability from our data \n")
            else: 
                 pic_list = get_pic_list(ans, pic_list)
                 probPicture=guessing_the_picture(pic_list, skill, probPicture)
                 probHint1=guessing_one_hint(skill)
                 probHint2=guessing_two_hint(skill)
                 output= Probability_total(probPicture, probHint1, probHint2, i)
                 if output!=0:
                     print("\nThe probabiliy of getting it right is ",round(output,2))
                 else: 
                     print("\nThere is not enough information available for me to calculate the probability from our data\n")
                     
            print("\nWrong! Be careful you have ",( 3-(i+1)),"more try\n")

            

            if (i==0):
                print("\nhint! this artwork was has a  movie named after it. In\
 the movie, a young peasant maid working in the house of painter Johannes Vermee.")
            elif (i==1):
                print("\nhint! 'girl with a _____ ______' ")
        i=i+1
    
        