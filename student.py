#To calculate a students total marks, percentage, grade, and pass/fail status.
print("..........Marks Calculator...........")

#input basic details of student
name=str(input("\nEnter Your Name:")) 
roll=int(input("Enter Your Roll Number: ")) 
print("\n\nEnter the following details") 
sub1=int(input("English: ")) 
sub2=int(input("Social Science: ")) 
sub3=int(input("Hindi: ")) 
sub4=int(input("Mathematics: ")) 
sub5=int(input("Science: ")) 

#calculate total marks
total=sub1+sub2+sub3+sub4+sub5 
#calculate percentage
per=(total/500)*100 
print(f"\nYou get {total} out of 500") #print total marks
print("Percentage: ",per)   #print percentage

#give grades to each subjects
print("\nGrades in per subject")
if sub1>=90 and sub1<101:
    print("English: S") 
elif sub1>=80 and sub1<91:
    print("English: A") 
elif sub1>=70 and sub1<81:
    print("English: B") 
elif sub1>=60 and sub1<71:
    print("English: C") 
elif sub1>=50 and sub1<61:
    print("English: D") 
elif sub1>=40 and sub1<51:
    print("English: E") 
elif sub1<40:
    print("English: Fail")

if sub3>=90 and sub3<101:
    print("Hindi: S") 
elif sub3>=80 and sub3<91:
    print("Hindi: A") 
elif sub3>=70 and sub3<81:
    print("Hindi: B") 
elif sub3>=60 and sub3<71:
    print("Hindi: C") 
elif sub3>=50 and sub3<61:
    print("Hindi: D") 
elif sub3>=40 and sub3<51:
    print("Hindi: E") 
elif sub3<40:
    print("Hindi: Fail")

if sub4>=90 and sub4<101:
    print("Mathematics: S") 
elif sub4>=80 and sub4<91:
    print("Mathematics: A") 
elif sub4>=70 and sub4<81:
    print("Mathematics: B") 
elif sub4>=60 and sub4<71:
    print("Mathematics: C") 
elif sub4>=50 and sub4<61:
    print("Mathematics: D") 
elif sub4>=40 and sub4<51:
    print("Mathematics: E") 
elif sub4<40:
    print("Mathematics: Fail")


if sub5>=90 and sub5<101:
    print("Science: S") 
elif sub5>=80 and sub5<91:
    print("Science: A") 
elif sub5>=70 and sub5<81:
    print("Science: B") 
elif sub5>=60 and sub5<71:
    print("Science: C") 
elif sub5>=50 and sub5<61:
    print("Science: D") 
elif sub5>=40 and sub5<51:
    print("Science: E") 
elif sub5<40:
    print("Science: Fail")

if sub2>=90 and sub2<101:
    print("Social Science: S") 
elif sub2>=80 and sub2<91:
    print("Social Science: A") 
elif sub2>=70 and sub2<81:
    print("Social Science: B") 
elif sub2>=60 and sub2<71:
    print("Social Science: C") 
elif sub2>=50 and sub2<61:
    print("Social Science: D") 
elif sub2>=40 and sub2<51:
    print("Social Science: E") 
elif sub2<40:
    print("Social Science: Fail")

#give percentage grading
if per>=90 and per<101:
    print("Overall You Achive Grade S") 
elif per>=80 and per<91:
    print("Overall You Achive Grade A") 
elif per>=70 and per<81:
    print("Overall You Achive Grade B") 
elif per>=60 and per<71:
    print("Overall You Achive Grade C") 
elif per>=50 and per<61:
    print("Overall You Achive Grade D") 
elif per>=40 and per<51:
    print("Overall You Achive Grade E") 
elif per<40:
    print("---Overall You Achive Grade F---")


#each subject status
print("\nResult status: ")
if sub1>=40:
    print("PASS in English")
elif sub1<40:
    print("FAIL in English")

if sub2>=40:
    print("PASS in Social Science")
elif sub2<40:
    print("FAIL in Social Science")

if sub3>=40:
    print("PASS in Hindi")
elif sub3<40:
    print("FAIL in Hindi")

if sub4>=40:
    print("PASS in Mathematics")
elif sub4<40:
    print("FAIL in Mathematics")

if sub5>=40:
    print("PASS in Science")
elif sub5<40:
    print("FAIL in Science")


#overall status
print("\n\nOverall Status is: ")
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    print("PASS")
else:
    print("FAIL")

#about the result

print("\n\n\n\n\n\nStudent needs to score equal to 40 marks or more than in each subject for passing the course, if student percentage is less than 40% then student is \nfail or fail in any subject also fail")
print("So Student must to score more than 40% in each subject and overall total semester percentage")
print("\nAbbreviations:-")
print("S:- Superb, Student score more than 90%")
print("A:- Excellent, Student score more than 80%")
print("B:- Outstanding, Student score more than 70%")
print("C:- Best, Student score more than 60%")
print("D:- Average, Student score more than 50%")
print("E:- Fine,Student score more than 40%")
