print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] =='Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print('Turn on the AC.')
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score?"))

# Determine the letter grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

    if "Arapahoe" in counties or "El Paso" in counties:
        print("Arapahoe or El Paso are in the list of counties.")
    else:
        print("Arapahoe or El Paso is not in the list of counties.")

    if "Arapahoe" in counties and "El Paso" not in counties:
        print("Only Arapahoe is in the list of counties.")
    else:
        print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)        

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for key, value in counties_dict.items():
    print(key,"county has", value,"registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county in range(len(voting_data)):
    print(voting_data[county]['county'])


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

canidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_canidate = (
    f"You received {canidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {canidate_votes / total_votes * 100}% of the total votes.")
print(message_to_canidate)


#Election code
#with open(file_to_save, "w") as txt_file:

    #txt_file.write("Conties in the Election")
    #txt_file.write("\n-------------------------------------")
    #txt_file.write("\nArapahoe")
    #txt_file.write("\nDenver")
    #txt_file.write("\nJefferson")