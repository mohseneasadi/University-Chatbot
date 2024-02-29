# This is a try to make a chatbot for TiTi University. 

# get the personal information from users like name, age, country and favourite colour and make a customize respond

print("Hi there! Welcome to chatbot service of TiTi University:)",
    "\nToday I am here to help you to know better the University!\nLet's get familiar to each other")

# get users name and make a customize respond
print("------------------------------------")
name = input("My name is Chiti! What's yours name? ")
name = name.upper().strip()
print(f"Nice to meet you {name}")

# get users country and make a customize respond
print("------------------------------------")
country = input("Where are you from budy? ")
country = country.lower().strip()

if country == 'france':
    print("I really like your contry. Eiffel Tower, the Louvre Museum and",
        "the charming streets of Paris.")
elif country == 'spain':
    print("Beside lovely and welcoming people, Spain", 
        "offers a rich combination of history and modernity!")
elif country == 'german':
    print("We have very good german students, you should find them and have a chat if you want!")
elif country == 'italy':
    print("The most beautiful country in the world! If I want to say 3 words about Italy,",
        "it has to be: breathtaking beauty, legendary history and pizza!")
elif country == 'brazil':
    print("Brazil is known for its lively festivals, stunning natural wonders, and warm-hearted people,", 
        "\nthere is a celebration of life in all its forms!")
elif country == 'iran':
    print("Great, I've heard a lot about your country! Iran, with its rich history and warm hospitality,",
        "\nis a country that has contributed significantly to the world's art, science, and literature.")
elif country == 'turkey':
    print("Turkey has a rich culture and great places, I can't wait to know more about that!")
elif country == 'us':
    print("Fabulous, you can find lots of students from US in TiTi University!")
else :
    print(f"You are from {country} it's a Lovely country!\nMaybe you can arrange a plan",
        "to represent your country to other students")

# get users age and make a customize respond
print("------------------------------------")
age = float(input("How old are you? "))

if age <= 12.9 :
    print("I suppose you enter your age wrong!\nIt's fine we can pass this question.")
elif 13 <= age <= 17 :
    print("Oh my god!You are a genius!")
elif 17.1 <= age <= 27 :
    print("Way to go! you have a long journey!")
elif 27.1 <= age <= 35 :
    print("I hope you'll have a great expereience at TiTi University.")
elif 35.1 <= age <= 45 :
    print("Good for you! you are really passionate to learn!")
else :
    print("Interesting! It's never late for educating! don't give up.")

# get users favourite colour and make a customize respond
print("------------------------------------")
colour = input("Let's know about our common interest!\nWhat's your favourite colour? ")
colour = colour.lower().strip()

if colour == 'blue' :
    print("Well, Lovely colour!\nDid you know there is a blue-lover club in the Universit?",
        "you should really catch them then")
elif colour == 'red':
    print("It's unbelievable! this is my favourite colour too!\nI think we have to run a Reddi club.")
elif colour == 'yellow' :
    print("God, I like your style!\nDid you know this is the main colour of the University brand!")
elif colour == 'brown':
    print("You know it reminds me the warm tones of wooden architecture, libraries filledwith richly",
    "\ntextured bookshelves, by the way I highly recommend to see the great library in main hall of the university.")
elif colour == 'gray':
    print("Smart choice, it never gets old!\nIt could complement every other colour.")
elif colour == 'purpel' :
    print("Great! I really like this color which represents creativity, wisdom, and elegance.")
elif colour == 'pink':
    print("What a great taste! Pink with its warm and charming tones,",
    "\noften symbolizes qualities like compassion, nurturing, and positivity.")
elif colour == 'green':
    print("Green, often associated with nature, growth, and harmony,",
    "\nthis colour symbolizes the collaborative and inclusive atmosphere within the University.")
else :
    print("Oh, Lovely colour!")

# get the academic information from users like faculty and major and make a customize respond
# I write 6 default faculty name here.
print("------------------------------------")
faculty = input("What faculty do you belong to? (business, engineering, science,"
                "arts design & architecture, law & justice, medicine): ")
faculty = faculty.lower().strip()

if faculty == 'business':
    print("I'm sure you can equip yourself with the knowledge, skills,", 
    "and networking opportunities needed for successful careers in the business world!")

elif faculty == 'medicine':
    print(f"I admire you! It's not easy to enter to {faculty} faculty, you had to study hard!")

elif faculty == 'law & justice' or faculty == 'law' or faculty == 'justice':
    print("TiTi Uiniversity has a strong repution for edducating the best individuals in this field in the whole country.")

elif faculty == 'arts' or faculty == 'design' or faculty == 'architecture' or faculty == 'arts design & architecture':
    print(f"You know, I think {faculty} enrich our lives, stimulate our imaginations, reflect the diverse perspectives", 
    "\nof humanity, fostering creativity, innovation, and a deeper understanding of the world around us.")

elif faculty == 'engineering':
    print("You are in the right place, because TiTi University encourages teamwork and",
    "\nthe exchange of ideas, fostering an environment where creativity and innovation thrive.")

elif faculty == 'science':
    print(f"{faculty} faculty must be greatful to have you and you are really lucky to be here!",
        "\nThey encourage you to question, learn, and adapt your understanding as new information emerges.")

else :
    print(f"Nice work budy! I bet you tried hard to enter to {faculty} faculty!")

print("------------------------------------")
major = input("What's your major? ")
major = major.lower().strip()
print(f"Good luck {name}! The {major} is one of the most amazing majors in the TiTi University.")

print("------------------------------------")
print(f"Well {name} I can't help myself asking question but I think that's enough for now. It's your turn;)")

#make a list for probable questions
question_list = ["what sports team i can attend", 
                "how easy is it to find part time job in university", 
                "what out of classroom support is there at the university", 
                "i can't enter into my portal", 
                "there is a wrong course on my portal, what should i do", 
                "can i get a loan for my tuition", 
                "can i get a leave for a semester", 
                "is there any apps which students can find friends or specific groups", 
                "how can i reach out the professors",  
                ]

#make a list for probable answers
answer_list = ["You can register for swimming, tennis and basketball team, there is a file in entertainment section in your portal you can file more detailed information there", 
                "there is different positions for students in every semester, you can register for them both online and in person in your faculty office.", 
                "We help you to write a good CV, find a intern position and make new professional expreinces", 
                "you have to request a new password by email, if it won't work, call the faculty staff", 
                "from the requests part in your portal, drop a new note to cancle your course", 
                "It depends on some factors including how many pepole request befor you, which major and degree do you study and etc. If you ask me, it's better to speak with a faculty staff", 
                "If you have a good reason, why not. Read the procedures file for student, you can find it on your student portal.", 
                "Ofcourse, we have developed an internal app for student which have differen setion, believe me, that's amazing. Moreover, every major has a unique group in telegram.", 
                "You can find them most of the times in thier offices, but if on the off-chance they are not available, you can send them an email and make an appointment",  
            ]

#make a loop for answering the users question, user can say bye if has no question 
done = True 
while  done :
    question = input("Please let me know if you have any question about the University."
                "\n(if you don't just say bye): ")
    question = question.lower().strip()

    if question in question_list:
        question_num = question_list.index(question)
        answer = answer_list[question_num]
        print (answer)
        print("------------------------------------")  

    elif question == "bye" :
        done = False
        
# if there is a question that not exist in question list, user have to talk with a faculty staff
# here I provide the contact information of 6 the faculties that I named befor 
    else :
        print ("I think you should talk to a faculty staff")
        print("------------------------------------")
        info = input("Do you need the contact information? ") # the answer can be yes, no or anything else
        info = info.lower().strip()

        if info == "yes" :
            print("Sure, I'll send you email and contact number. It is better to make an appointment first.")
            
            if faculty == 'arts' or faculty == 'design' or faculty == 'architecture' or faculty == 'arts design & architecture' :
                    print("Mr Estephan : Estephan@titi.ac.com, 5674890",
                    "\nMs Dayana : Dayana@titi.ac.com, 873564",
                    "\nI hope that helps you")

            elif faculty == "business" :
                    print("Mr Mark : Mark@titi.ac.com, 5674890",
                    "\nMs Mery : Mery@titi.ac.com, 873564",
                    "\nI hope that helps you")

            elif faculty == "engineering" :
                    print("Mr john : john@titi.ac.com, 12345",
                    "\nMs Alison : Alison@titi.ac.com, 54321",
                    "\nI hope that helps you")

            elif faculty == 'law & justice' or faculty == 'law' or faculty == 'justice' :
                    print("Mr Ross : Ross@titi.ac.com, 67890",
                    "\nMs Kate : Kate@titi.ac.com, 98760",
                    "\nI hope that helps you")

            elif faculty == "medicine" :
                    print("Mr jack : jack@titi.ac.com, 13579",
                    "\nMs Anna : Anna@titi.ac.com, 24680",
                    "\nI hope that helps you")

            elif faculty == "science" :
                    print("Mr Alex : Alex@titi.ac.com, 34215",
                    "\nMs Suzi : Suzi@titi.ac.com, 95678",
                    "\nI hope that helps you")

            else :
                    print("Mr jeremy : jeremy@titi.ac.com, 567489",
                    "\nMs Dilan : Dilam@titi.ac.com, 87356",
                    "\nI hope that helps you")
        
        elif info == "no" :
            print("Great! please don't hesitate and make a call or drop an email. Good luck!")
        
        else :
            print ("I suppose I can't help you anymore, sorry:(",
                    "\nDo call a faculty staff, they help you properly.")
        
        print("------------------------------------")

# the last sentence for saying goodbye
print("------------------------------------")          
print (f"Really nice to meet you {name}. It was a great chat!", 
    "\nLooking forward to hearing from you.", 
    "\nGood luck with your new journy and take care:)")
print("------------------------------------")