'''
1. User information.
2. All required data. 
3. calculation. 
4. probability.
5. class.
6. symtoms confirmation.
7. How prevent COVID-19.
8. Some information about how this COVID-19 generated.
9. Some information about the vaccine.
'''

def AskUserinfo():
    # getting the user info
    print('HELLO!\nMY name is Catherine.\nToday I will be helping you to predict the chances of being infected to COVID-19!!\nSo, go ahead with typing in your name.\n')
    Name = str(input('What is your name ?\n'))
    Name = Name[0].upper()+Name[1:].lower()
    print('Hello', name ,'it is nice to meet you :)')
    
    # this piece of code handles if user doesnot enter an integer age of age<0 or age>120
    global age
    while True:
        try:
            age  =  int(input('what is your age ?\n'))
            if(age<0 or age>120):
                print("Oops!  That was no valid age.  Try again...")
            else:
                break
        except ValueError:
            print("Oops!  That was no valid age.  Try again...")
            
    # note the gender of user
    
    while True:
        gender = (str(input('What is your gender ?\n'))).lower()
        if(gender=="male" or gender=="female"):
            break
        else:
            print("Oops! Invalid gender, Please type male or female. Try again...")
  

def required_data():
    #collecting data from where the person lives.
    print('Now I will take some of your data for my prediction\n')
    
    while True:
        city = (str(input('Do you live in a densely populated city ?\n( yes / no):\n'))).lower()
        if(city=="yes" or city=="no"):
            break
        else:
            print("Oops! Invalid input, Please type yes or no. Try again...")
    
    if (city == "yes"):
        chance_city = 50
    if (city == "no"):
        chance_city = 10 

    
    while True:
        try:
            cases_area = int(input('How many cases have been reported in your area ?\n(Within the range of 2 miles) . Please Enter Integer value:\n'))
            if(cases_area<0):
                print("Oops! That was no valid input. Try again...")
            else:
                break
        except ValueError:
            print("Oops!  That was no valid input.  Try again...")
    
    if (cases_area == 0):
        chance_area = 1
    elif (cases_area > 1 and cases_area < 10):
        chance_area = 5
    elif (cases_area >= 10 and cases_area < 50):
        chance_area = 20
    elif (cases_area >= 50 and cases_area < 150):
        chance_area = 50
    else:
        chance_area = 75
    
    #calculating travel history information
    while True:
        travelh = (str(input('Have you travelled anywhere in last 2 weeks ?\n( yes / no )\n'))).lower()
        if(travelh=="yes" or travelh=="no"):
            break
        else:
            print("Oops! Invalid input, Please type yes or no. Try again...")
    
    if (travelh == "no"):
        chance_travel = 0
        
    if (travelh == "yes"):
        while True:
            persons = (str(input('Have you travelled alone or with more than 2 people ?\n( alone / with someone)\n'))).lower()
            if(persons=="alone" or persons=="with someone"):
                break
            else:
                print("Oops! Invalid input, Please type alone or with someone. Try again...")
    
        if (persons == "alone"):
            chance_travel = 10
        if (persons == "with someone"):
            chance_travel = 50
    

    # calculating contact information
    while True:
        contact = (str(input('Have you been in contact with a COVID-19 infected person ?\n( yes / no / i do not know)\n'))).lower()
        if(contact=="yes" or contact=="no" or contact =="i do not know"):
            break
        else:
            print("Oops! Invalid input, Please type yes, no or i do not know. Try again...")
    
    if (contact == "yes"):
        chance_contact = 50
    elif (contact == "no"):
        while True:
            sure = (str(input('Are you sure ?\n( yes / no )\n'))).lower()
            if(sure=="yes" or sure=="no"):
                break
            else:
                print("Oops! Invalid input, Please type yes or no. Try again...")
        
        if (sure == "yes"):
            chance_contact = 0
        elif (sure == "no"):
            chance_contact = 50
    elif(contact == "i do not know"):
        chance_contact = 50

    #Symptoms
    while True:
        cough = (str(input('Are you suffering from cough ?\n( yes / no )\n'))).lower()
        if(cough=="yes" or cough =="no"):
            break
        else:
            print("Oops! Invalid input, Please type yes or no. Try again...")
    if (cough == "yes"):
        cough_chance = 50
    if (cough == "no"):
        cough_chance = 0
    
    while True:
        difficulty_breath = (str(input('Do you have any issues in breathing ?\n( yes / no / severe )\n'))).lower()
        if(difficulty_breath=="yes" or difficulty_breath=="no"):
            break
        else:
            print("Oops! Invalid input, Please type yes or no or severe. Try again...")
    if (difficulty_breath == "yes"):
        chance_difficulty_breath = 50
    if (difficulty_breath == "no"):
        chance_difficulty_breath = 0
    if difficulty_breath == "severe":
        chance_difficulty_breath = 75
    
    while True:
        try:
            extra_symptoms = int(input('\n1. Fever\n2. Chills\n3. Repeated shaking with chills\n4. Muscle pain\n5. Headache\n6. Sore throat\n7. New loss of taste or smell\nDo you have any one of these ^ symptoms\n Enter in integer value:\n'))
            if(extra_symptoms>0 and extra_symptoms<8):
                break
            else:
                print("Oops!  That was no valid number.  Try again...")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    if (extra_symptoms >= 0 and extra_symptoms < 2):
        chance_extra_symptoms = 0
    elif (extra_symptoms == 2):
        chance_extra_symptoms = 28
    elif (extra_symptoms == 3):
        chance_extra_symptoms = 42
    elif (extra_symptoms == 4):
        chance_extra_symptoms = 57
    elif (extra_symptoms == 5):
        chance_extra_symptoms = 71
    elif (extra_symptoms == 6):
        chance_extra_symptoms = 85
    elif(extra_symptoms == 7):
        chance_extra_symptoms = 100
    
    #calculations ... 

    total = 700
    av =  chance_area + chance_contact + cough_chance + chance_difficulty_breath + chance_extra_symptoms + chance_city + chance_travel
    prediction = (av/total)*100
    print(prediction)

#calculations
def staterisk():
    print("Now i would like tell you about risk of being affected of your age group by covid 19 virus")
    states_list = ["west virginia", "kentucky","arkansas", "louisiana","mississippi","alabama","tennessee","oklahoma","michigan","indiana","missouri","south carolina","new hamisphere" ,"maine","ohio","delaware","north carolina","oregon","florida","georgia","pennsylvania","kanas","maryland","rhode island","texas","new mexico","arizona","new york","illinois","nebraska","alaska","nevada","vermont","district of columbia","hawaii","montana","virginia","washington","wisconsin","iowa","idaho","north dakota","minnesota","utah","colorado"]
    while True:
        state = (str(input('Which state of America do you live in ?:\n '))).lower()
        if(state in states_list):
            break
        else:
            print("Oops! That was no valid State.  Try again...")
            
    global age
    if (age <= 65 ):
        if (state =="west virginia"): 
            chance_state ="more than 25%"
        elif (state == "kentucky"):
            chance_state ="more than 25%"
        elif (state == "arkansas"):
            chance_state ="more than 25%"
        elif (state == "louisiana"):
            chance_state ="more than 25%"
        elif (state == "mississippi"):
            chance_state ="more than 25%"
        elif (state == "alabama"):
            chance_state ="more than 25%"
        elif (state == "tennessee"):
            chance_state ="more than 25%"
        elif (state == "oklahoma"):
            chance_state ="more than 25%"
        elif (state == "michigan"):
            chance_state ="20-25%"
        elif (state == "indiana"):
            chance_state ="20-25%"
        elif (state == "missouri"):
            chance_state ="20-25%"
        elif (state == "south carolina"):
            chance_state ="20-25%"
        elif (state == "new hamisphire"):
            chance_state ="20-25%"
        elif (state == "maine"):
            chance_state ="20-25%"
        elif (state == "ohio"):
            chance_state ="20-25%"
        elif (state == "delaware"):
            chance_state ="20-25%"
        elif (state == "north carolina"):
            chance_state ="20-25%"
        elif (state == "oregon"):
            chance_state ="20-25%"
        elif (state == "florida"):
            chance_state ="20-25%"
        elif (state =="georgia"):
            chance_state ="20-25%"
        elif (state == "pennslyvania"):
            chance_state ="20-25%"
        elif (state == "kanas"):
            chance_state ="20-25%"
        elif (state == "maryland"):
            chance_state ="20-25%"
        elif (state == "rhode island"):
            chance_state ="20-25%"
        elif (state == "texas"):
            chance_state ="20-25%"
        elif (state == "new mexico"):
            chance_state ="20-25%"
        elif (state == "arizona"):
            chance_state ="20-25%"
        elif (state == "new york"):
            chance_state ="20-25%"
        elif (state == "illinois"):
            chance_state ="20-25%"
        elif (state == "nebraska"):
            chance_state ="20-25%"
        elif (state == "alaska"):
            chance_state ="less than 20%"
        elif (state == "nevada"):
            chance_state ="less than 20%"
        elif (state == "vermont"):
            chance_state ="less than 20%"
        elif (state == "district of columbia"):
            chance_state ="less than 20%"
        elif (state == "hawaii"):
            chance_state ="less than 20%"
        elif (state == "montana"):
            chance_state ="less than 20%"
        elif (state == "virginia"):
            chance_state ="less than 20%"
        elif (state == "washington"):
            chance_state ="less than 20%"
        elif (state == "wiscosin"):
            chance_state ="less than 20%"
        elif (state == "iowa"):
            chance_state ="less than 20%"
        elif (state == "idaho"):
            chance_state ="less than 20%"
        elif (state == "north dakota"):
            chance_state ="less than 20%" 
        elif (state == "wyoming"):
            chance_state ="less than 20%"
        elif (state == "connecticut"):
            chance_state ="less than 20%"
        elif (state == "california"):
            chance_state ="less than 20%"
        elif (state == "new jersey"):
            chance_state ="less than 20%"
        elif (state == "massachusetts"):
            chance_state ="less than 20%"
        elif (state == "south dakota"):
            chance_state ="less than 20%"
        elif (state == "minnesota"):
            chance_state ="less than 20%"
        elif (state == "utah"):
            chance_state ="less than 20%"
        elif (state == "colorado"):
            chance_state ="less than 20%"
        print(chance_state)

    if (age > 65):
        if (state == "hawaii"):
            chance_state ="more than 60%" 
        elif (state == "monatana"):
            chance_state ="more than 60%"
        elif (state == "vermont"):
            chance_state ="more than 60%"
        elif (state == "south dakota"):
            chance_state ="more than 60%"
        elif (state == "florida"):
            chance_state ="more than 60%"
        elif (state == "wyoming"):
            chance_state ="more than 60%"
        elif (state == "iowa"):
            chance_state ="more than 60%"
        elif (state == "massachusetts"):
            chance_state ="more than 60%"
        elif (state == "minnesota"):
            chance_state ="more than 60%"
        elif (state == "connecticut"):
            chance_state ="55-60%"
        elif (state == "new jersey"):
            chance_state ="55-60%"
        elif (state == "idaho"):
            chance_state ="55-60%"
        elif (state == "maine"):
            chance_state ="55-60%"
        elif (state == "wiscosin"):
            chance_state ="55-60%"
        elif (state == "arizona"):
            chance_state ="55-60%"
        elif (state == "colorado"):
            chance_state = "55-60%"
        elif (state == "new mexico"):
            chance_state ="55-60%"
        elif (state == "delaware"):
            chance_state ="55-60%"
        elif (state == "pennsylvania"):
            chance_state ="55-60%"
        elif (state == "nevada"):
            chance_state ="55-60%"
        elif (state == "virginia"):
            chance_state ="55-60%"
        elif (state == "washington"):
            chance_state ="55-60%"
        elif (state == "nebraska"):
            chance_state ="55-60%"
        elif (state =="north dako0ta"):
            chance_state ="55-60%"
        elif (state == "oregon  "):
            chance_state ="55-60%"
        elif (state == "new york"):
            chance_state ="55-60%"
        elif (state == "rhode island"):
            chance_state ="55-60%"
        elif (state == "california"):
            chance_state ="55-60%"
        elif (state == "south carolina"):
            chance_state ="55-60%"
        elif (state == "illinois"):
            chance_state ="55-60%"
        elif (state == "new hamisphire"):
            chance_state ="55-60%"
        elif (state == "ohio"):
            chance_state ="55-60%"
        elif (state == "kanas"):
            chance_state ="55-60%"
        elif (state == "north carolina"):
            chance_state ="55-60%"
        elif (state == "missouri"):
            chance_state ="55-60%"
        elif (state == "maryland"):
            chance_state ="55-60%"
        elif (state == "michigan"):
            chance_state ="55-60%"
        elif (state == "utah"):
            chance_state ="55-60%"
        elif (state == "indiana"):
            chance_state ="55-60%"
        elif (state == "west virginia"):
            chance_state ="55-60%"
        elif (state == "alabama"):
            chance_state ="55-60%"
        elif (state == "georgia"):
            chance_state ="55-60%"
        elif (state == "oklahoma"):
            chance_state ="55-60%"
        elif (state == "tennessee"):
            chance_state ="55-60%"
        elif (state == "arkansas"):
            chance_state ="55-60%"
        elif (state == "mississippi"):
            chance_state ="less than 50%"
        elif (state == "alaska"):
            chance_state ="less than 50%"
        elif (state == "kentucky"):
            chance_state ="less than 50%"
        elif (state == "texas"):
            chance_state ="less than 50%"
        elif (state == "louisiana"):
            chance_state ="less than 50%"
        elif (state == "disrict of columbia"):
            chance_state ="less than 50%"
        print(chance_state)
        exit("Hit Enter")

if __name__ == "__main__":
    age = 0
    AskUserinfo()
    required_data()
    staterisk()





