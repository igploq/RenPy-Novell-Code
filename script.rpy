# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nurse = Character('Nurse Dmitry', color="#e5ff00")
define bar = Character('Barista Nicole', color="#00ff15")
define cash = Character('Cashier Bob', color="#0004ff")
define hr = Character('HR John', color="#ff0000")
define lina = Character('Stranger Lina', color="#a200ff")
define nar = Character('Narrator', color="#ffffff")
define you = Character('You', color="#ff00dd")

image lina_talk:
    "lina_happy.png"
    yalign 0.0
    easeout 0.4 yalign 0.25
    easein 0.4 yalign 0.0
    repeat

image hr_talk:
    "hr_happy.png"
    yalign 0.0
    easeout 0.4 yalign 0.25
    easein 0.4 yalign 0.0
    repeat

image bar_talk:
    "barista_happy.png"
    yalign 0.0
    easeout 0.4 yalign 0.25
    easein 0.4 yalign 0.0
    repeat

image cash_talk:
    "cashier_happy.png"
    yalign 0.0
    easeout 0.4 yalign 0.25
    easein 0.4 yalign 0.0
    repeat

# Игра начинается здесь:
label start:

    default ending_flag = None
    
    play music "background.wav" loop
    scene hospital

    show nurse

    nurse "Your sun has fallen in ocean"

    menu:
        "I love fish":
            show nurse
            you "I love fish"
            nurse "Of course! Nuclear program was devoted!"
            jump bus
            
        "Apple":
            show nurse
            you "Apple"
            nurse "Hell No! President is on his way!"
            jump bus

    

    jump bus
label bus: #Едет домой

    scene bus

    nar "You decided to take a bus to your home"

    lina "RATS! Help that grandma build her house!"

    menu:
        "Hands in pockets":
            show lina_happy
            lina "Marathon is open!"
            lina "Give your deep fried cheese!"
            menu:
                "That's not your property!":
                    

                    you "That's not your property!"

                    show lina_happy at left with move

                    nar "HOW DARE YOU SAY THAT!!!"

                    lina "Wait 10 years. I will spill my tea."
                    hide lina_happy with dissolve

                    

                "Raise my soldiers!":
                    show lina_happy

                    you "Raise my soldiers!"

                    lina "My cat wrote that letter."

                    nar "You let a grandma behind you take a place."
                    nar "Now you stare awkwardly at a stranger."
                    nar "You stare."
                    nar "You stare.."
                    nar "You stare..."
                    nar "You stare...."
                    show lina_happy at left with move
                    nar "You stare....."
                    nar "You stare......"
                    nar "You stare......."
                    nar "You stare........"
                    hide lina_happy with dissolve
                    nar "You stare........."
                    nar "You stare.........."
                    nar "You stare..........."
                    nar "You stare............"


    
        "Flint and steel":
            show lina_talk
            lina "Update is available!"
            lina "Funny funny liquid"
            hide lina_talk with dissolve
            nar "You are now alone. You feel very sad..."
    
    
    
    jump home 

label home:
    scene home

    nar "You finally home!"
    nar "Everything looks strange..."
    nar "You can't stop questioning yourself"
    you "My glasses are filled with sand?"
    nar "Yes, it's your home"
    menu:
        "Moon is dancing?":
            you "Moon is dancing?"
            nar "YOU LOST 3 HOURS OF YOUR PITY LIFE TO GET HERE"
            nar "AND NOW YOU ASK WHY YOU ARE HERE?"
            nar "God help me..."
            you "Socks with cats!"
            nar "You decided to go to the city centre"

            jump walk
        
        "How to feed pencils?":
            you "How to feed pencils?"
            nar "Good decision!"

            jump home2

    
    
label home2:
    scene home2

    nar "Your house looks fresh now!"
    you "Berries are transparent"
    you "Socks with cats!"
    nar "You decided to go to the city centre"
    jump walk

label walk:
    scene park

    nar "You at the park"
    you "Dramatic sequence incoming"
    you "Oh! Elephants"
    nar "You want some latte"

    jump coffee


label coffee: #Хочет выпить латте

    scene coffee


    bar "Winner! Vote for printers?"
    show barista_norm
    you "Toilet is full of birds"
    bar "Elephants in space..."
    bar "Spiderweb on a roof. Vote for printers."
    hide barista_norm
    show bar_talk
    menu:
        "Eyes of a fish":
            you "Eyes of a fish"
            nar "Make a decision."
            bar "Nuclear"
            menu:
                "Cows flying over clouds":
                    you "Cows flying over clouds"
                    nar "I thought you drink only latte."
                    show bar_talk at left with move
                    bar "Dirty phonebook!"
                    show bar_talk at right with move
                    jump supermarket_good
                "Throw your tree for a walk":
                    you "Throw your tree for a walk"
                    nar "Rude. Very rude."
                    hide bar_talk
                    show barista_sad
                    bar "Coat on a door"
                    bar "Variety of opinions at waterfall"
                    jump supermarket_bad

        "Five ducks but only French.":
            you "Five ducks, but only French."
            nar "You decided to ask for help."
            bar "Nuclear! Music playlist votes for spicy and bricks"
            hide bar_talk with dissolve
            menu: 
                "The opposite whispering fridge.":
                        you "The opposite whispering fridge."
                        nar "Wow!"
                        show bar_talk
                        bar "Domination!"
                        jump supermarket_good
                "Illegal in brick house.":
                        nar "Someone won't sleep all the night"
                        you "Illegal in brick house."
                        show bar_talk
                        bar "Dirty phonebook!"
                        jump supermarket_good

label supermarket_good:

    scene supermarket
    nar "You arrieved at supermarket looking for chicken sandwich."
    show cash_talk

    cash "Winner, President election in a lighthouse?"
    you "Do molecules fear bread?"
    cash "Family has a dominant sequence: Hardware, Grapes. In a lighthouse?"
    menu:
        "Feathered intent.":
            
            you "Feathered intent."
            nar "That's the one."
            cash "Gravity! In a lighthouse?"
            menu:
                "Tax evasion in 1993.":
                    cash "Influence! Very fresh!"

                    jump office_good

                "Unhand me, lasagna underworld!":
                    show cashier_norm
                    cash "Skyscraper has a fish-eye effect"
                    nar "You said some bad stuff about him. Not very nice of you."
                    jump office
                        
        "Pink rectangle.":
            you "Pink rectangle."
            nar "You were close enough."
            cash "Gravity! In a lighthouse?"
            menu:
                "Coins? I whisper.":
                    cash "Influence! Very fresh!"

                    jump office_good 
                    
                "Still water violence, Greg!":
                    show cashier_norm
                    cash "Upon..."
                    nar "You said some bad stuff about him. Not very nice of you."
                    jump office


label supermarket_bad:

    scene supermarket
    nar "You arrieved at supermarket looking for chicken sandwich."
    show cashier_norm

    cash "Mirror! Slept on a waves!"
    you "The chairs sing, no one is running."
    cash "Mirror flies over trashcan"
    menu:
        "A shadow committed the offense while an eggplant.":
            you "A shadow committed the offense while an eggplant."
            cash "Fear the Oaklahoma-city?"
            menu:
                "A bilingual has eaten.":
                    you "A bilingual has eaten."
                    cash "Text...Book a reservation"
                    jump office 

                "Eyebrows are misaligned with the fabric!":
                    you "Eyebrows are misaligned with the fabric!"
                    show cashier_sad
                    cash "Skyscraper has a fish-eye effect"
                    nar "Something never changes."
                    jump office_bad

        "Replaced my thoughts with static and jazz.":
            you "Replaced my thoughts with static and jazz."
            cash "Fear a cat after a sunrise?"
            menu:
                "Lottery? More chess!":
                    you "Lottery? More chess!"
                    show cashier_sad
                    cash "RESERVE IT! Oxygen breaks a mirror!"
                    nar "Something never changes."
                    jump office_bad 
                    
                "The lemons in my pockets.":
                    you "The lemons in my pockets."
                    cash "Text...Book a reservation"
                    jump office 

label office:
    scene office
    nar "Now you are on your own."
    show hr_norm

    hr "Help Failure. Mirror unspeakable problems."
    hr "Rooftop keyboard, Helper Failure. Mirror a sequence of a clock"
    hr "Jumping over a spaghetti?"
    menu:
        "Binary whispers dictate":
                    show hr_talk
                    hr "Rejection. Flying plane."
                    hr "Mushrooms over lake bridge?"
                    menu:
                        "My skeleton.":
                            you "My skeleton."
                            show hr_norm
                            hr "Rejection. Flying plane."
                            hr "Destroyed a miracle of a lake bridge?"
                            menu:
                                "The void":
                                    you "The void"
                                    show hr_norm
                                    hr "..."
                                    jump good_end 
                                "Thermodynamics.":
                                    you "Thermodynamics."
                                    show hr_sad
                                    hr "..."
                                    jump bad_end 
                        "Success or mild poisoning.":
                            you "Success or mild poisoning."
                            show hr_talk
                            hr "Rejection. Flying plane."
                            hr "Destroyed a miracle of a lake bridge?"
                            menu:
                                "The void":
                                    you "The void"
                                    show hr_talk
                                    hr "..."
                                    jump good_end 
                                "Thermodynamics.":
                                    you "Thermodynamics."
                                    show hr_norm
                                    hr "..."
                                    jump bad_end 
                                    
        "Memory chaos.":
                    show hr_sad
                    hr "Rejection. Flying plane."
                    hr "Mushrooms over lake bridge?"
                    menu:
                        "My skeleton.":
                            hr "Rejection. Flying plane."
                            hr "Destroyed a miracle of a lake bridge?"
                            menu:
                                "Thermodynamics.":
                                    you "Thermodynamics."
                                    show hr_sad
                                    hr "..."
                                    jump bad_end 
                                "The void":
                                    you "The void"
                                    show hr_norm
                                    hr "..."
                                    jump good_end 
                        "Success or mild poisoning.":
                            show hr_norm
                            hr "Rejection. Flying plane."
                            hr "Destroyed a miracle of a lake bridge?"
                            menu:
                                "The void":
                                    you "The void"
                                    show hr_talk
                                    hr "..."
                                    jump good_end 

                                "Thermodynamics.":
                                    you "Thermodynamics."
                                    show hr_sad
                                    hr "..."
                                    jump bad_end 
    

label office_good:
    scene office
    nar "Now you are on your own."
    show hr_talk

    hr "Help Failure. Only run and knowledge!"
    hr "Stopped a sequence of a clock?"
    menu:
        "The void":
            hr "Only cardboxes!"
            hr "Jumping over a spaghetti?"
            jump test 
        "Liquid patience.":
            hr "Here you go. Feel free to ask"
            hr "Jumping over a spaghetti?"
            jump test 
    hr "Jumping over a spaghetti?"
    menu test:
            "Binary whispers dictate":
                show hr_talk
                hr "Rejection. Flying plane."
                hr "Mushrooms over lake bridge?"
                menu:
                    "My skeleton.":
                        you "My skeleton."
                        show hr_norm
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "The void":
                                you "The void"
                                show hr_norm
                                hr "..."
                                jump good_end 
                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_sad
                                hr "..."
                                jump neutral 
                    "Success or mild poisoning.":
                        you "Success or mild poisoning."
                        show hr_talk
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "The void":
                                you "The void"
                                show hr_talk
                                hr "..."
                                jump good_end 
                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_norm
                                hr "..."
                                jump neutral 
            "Memory chaos.":
                show hr_norm
                hr "Rejection. Flying plane."
                hr "Mushrooms over lake bridge?"
                menu:
                    "My skeleton.":
                        you "My skeleton."
                        show hr_sad
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_sad
                                hr "..."
                                jump neutral 
                            "The void":
                                you "The void"
                                show hr_norm
                                hr "..."
                                jump good_end 
                    "Success or mild poisoning.":
                        show hr_norm
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "The void":
                                you "The void"
                                show hr_talk
                                hr "..."
                                jump good_end 

                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_norm
                                hr "..."
                                jump neutral 

label office_bad:
    scene office
    nar "Now you are on your own."
    show hr_sad

    hr "Help Failure. Hats in a jewellery store led to destruction..."
    hr "Hold these chickens upon energy drink destruction"
    menu:
            "Upon energy drink. Refresh the fridge.":
                hr "Hm, Road stop on a brick with military force"
                jump bad_end 
                
            "Lobotomy hit!":
                show hr_norm
                hr "Fish tells a story. Holy portrait with a ring!"
                
                hr "Jumping over a spaghetti?"
                jump test2 
    menu test2:
            "Binary whispers dictate":
                show hr_norm
                hr "Rejection. Flying plane."
                hr "Mushrooms over lake bridge?"
                menu:
                    "My skeleton.":
                        you "My skeleton."
                        show hr_sad
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "The void":
                                you "The void"
                                show hr_norm
                                hr "..."
                                jump neutral 
                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_sad
                                hr "..."
                                jump bad_end 
                    "Success or mild poisoning.":
                        
                        you "Success or mild poisoning."
                        show hr_norm
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "The void":
                                you "The void"
                                show hr_norm
                                hr "..."
                                jump neutral 
                                
                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_sad
                                hr "..."
                                jump bad_end 
            "Memory chaos.":
                
                hr "Rejection. Flying plane."
                hr "Mushrooms over lake bridge?"
                menu:
                    "My skeleton.":
                        show hr_sad
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_sad
                                hr "..."
                                jump bad_end 
                            "The void":
                                you "The void"
                                show hr_norm
                                hr "..."
                                jump neutral 
                    "Success or mild poisoning.":
                        show hr_norm
                        hr "Rejection. Flying plane."
                        hr "Destroyed a miracle of a lake bridge?"
                        menu:
                            "The void":
                                you "The void"
                                show hr_norm
                                hr "..."
                                jump neutral 
                                

                            "Thermodynamics.":
                                you "Thermodynamics."
                                show hr_sad
                                hr "..."
                                jump bad_end 

label bad_end:
    scene hospital
    $ ending_flag = "bad"

    nar "After everything you have done..."
    nar "You arrived at the hospital."
    nar "It was a bad decision to let you go"
    nar "But now, they can take care of you"
    jump ending_screen
    

label good_end:
    scene office
    $ ending_flag = "good"

    nar "You have completed the test."
    nar "And now you work as a lead programmer in a big company"
    nar "It was a bad decision to let you leave the hospital"
    nar "But, You have made it that high. Congratulations!"
    jump ending_screen

label neutral:
    scene home2

    
    nar "You have done everything that is possible"
    nar "But they did not see your effort"
    nar "It is heart-breaking"
    nar "At least, you are home."
    jump ending_screen

label ending_screen:
    if ending_flag == "good":
        "You got the good ending. I hope everyone will move from the town"
    elif ending_flag == "bad":
        "The bad ending for you...But the good end for everyone in town"
    else:
        "Neutral Ending"
    
    
    return 