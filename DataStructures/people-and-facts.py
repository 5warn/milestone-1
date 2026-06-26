#creating a dictionary of a list of people and one fact about them
people_dict={ 
             "Jeff": "Is afraid of dogs",
             "David":"Plays the piano",
             "Jason":"Can fly an airplane"}

#creating a function for displaying the facts 
def display_facts():
    for key,value in people_dict.items():
        print(key,":",value)
    
#calling to display    
display_facts()

#change a fact about a person
people_dict["Jeff"]="Is afraid of heights"

#add additional person and fact
people_dict["Jill"]="Can hula dance"

#calling multiple times for display 
display_facts()
display_facts()
display_facts()
 
''''after running the program mutiple times, and the order does not change'''
