# flowchart exists name: Python_task_grading.drawio

bio_score = float(input("What did you score for biology?"))
chem_score = float(input("What did you score for chemistry?"))
phy_score = float(input("What did you score for physics?"))

# creating an average of the 3 scores

ave_score = (bio_score + chem_score + phy_score) / 3 

# bio_score grading

if bio_score >= 70:
    print("Your biology grade is 1st")
elif bio_score >= 60:
    print("Your biology grade is 2:1")
elif bio_score >= 50:
    print("Your biology grade is 2:2")
elif bio_score >= 40:
    print("Your biology grade is pass")
else:
    print ("Your biology grade is fail, but don't let anyone ever tell you that you are a failure")

# chem_score grading

if bio_score >= 70:
    print("Your chemistry grade is 1st")
elif bio_score >= 60:
    print("Your chemistry grade is 2:1")
elif bio_score >= 50:
    print("Your chemistry grade is 2:2")
elif bio_score >= 40:
    print("Your chemistry grade is pass")
else:
    print ("Your chemistry grade is fail, but don't let anyone ever tell you that you are a failure")

# phy_score grading

if phy_score >= 70:
    print("Your physics grade is 1st")
elif phy_score >= 60:
    print("Your physics grade is 2:1")
elif phy_score >= 50:
    print("Your physics grade is 2:2")
elif phy_score >= 40:
    print("Your physics grade is pass")
else:
    print ("Your physics grade is fail, but don't let anyone ever tell you that you are a failure")


# showing the final result: an average of the three scores

print("Your average score from all 3 grades is" , ave_score)

# bonus: add some logic! Task: if any score < 40 print fail
# turns out I have kind of already included this initially

