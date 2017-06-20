# Debugging
# 6/13/17
# CTI-110 M3LAB - Debugging
# Syed

score = int(input("What is the test score? "))


if score >=  90:
    letterGrade = "A"
    
elif score >= 80:
    letterGrade = "B"
    
elif score >= 70:
     letterGrade = "C"
     
elif score >=  60:
    letterGrade = "D"
    
elif score >= 50:
    letterGrade = "F"
else:
    letterGrade = "Too Low"
    
   
    letterGrade = "Too Low"
    print ("Grade is below the lowest value checked.")


print ("The letter grade is:",letterGrade)
