#Days and their respective names
DaysAndNames={
    "monday":"Kojo",
    "tuesday":"Kobla",
    "wednesday":"kaku",
    "thursday":"Yaw",
    "friday":"kofi",
    "saturday":"kwame",
    "sunday":"Akwasi"
}

#East African countries and their capitals
EastAfricaCountries={
    "rwanda":"Kigali",
    "uganda":"Kampala",
    "kenya":"Nairobi",
    "burundi":"Gitega",
    "tanzania":"Mombasa"
   
}
#Holder for building up sentences
sentences=[]

#List for switching the prompts
prompt=["day you were born","a country in east africa","your profession","your hobby","your age","your gender","your location","your favorite food","your favorite drink","your color"]
counter = 0
while(counter<10):
    value = input("enter "+prompt[counter]+":  ")
    sentences.append(value)
    counter=counter+1
i=0
#Building the sentences
sentences[0]="Since you were born on {} Your name would be {}".format(sentences[0],DaysAndNames.get(sentences[0]))
sentences[1]="The capital of {} is {}".format(sentences[1],EastAfricaCountries.get(sentences[1]))
sentences[2]="Your profession {}".format(sentences[2])
sentences[3]="Your hobby is {}".format(sentences[3])
sentences[4]="Your age {}".format(sentences[4])
sentences[5]="Your gender {}".format(sentences[5])
sentences[6]="Your location is {}".format(sentences[6])
sentences[7]="Your favorite food is {}".format(sentences[7])
sentences[8]="Your favorite drink is {}".format(sentences[8])
sentences[9]="Your favorite color is {}".format(sentences[9])

#Displaying the sentences
while(i<10):
    print(sentences[i])
    i=i+1
    
