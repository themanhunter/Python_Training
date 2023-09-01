
#List of all the states, must be contained inside [] and split with a comma
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Prints out the state that is in the 1st place, which is Pennsylvania, because delaware is in the place of 0
print(states_of_america[1])


#This changes the thing in the list that is in the first place, and adjusts it to whatever you want
states_of_america[1] = "Pencilvania"
print(states_of_america)


#The append function will add something new onto the list at the end
states_of_america.append("Manchester")
print(states_of_america)


#The extend function can add more results onto the end too, but they must be contained inside () and then []
states_of_america.extend(["Liverpool", "Newcastle"])
print(states_of_america)


