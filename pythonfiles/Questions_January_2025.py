from datetime import datetime

def display_dev_log():
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Version: 1.0.0")
    print("Status: Initial Implementation")
    print("\nChangelog:")
    print("- Added framework for 10 distinct question sections")
    print("- Implemented basic section selection logic")
    print("- Prepared structure for future question implementation")
    print("- Added scoring system to track correct answers")
    print("\nPending Tasks:")
    print("- Added United States questions (Section 1)")  # More specific
    print("\nNote: This is a development build. Questions for other sections will be implemented in future updates.") # Clearer
    print("==================\n")
    print("=== Development Log ===")

def ask_question(question, correct_answers):
    answer = input(question).lower()
    if answer in correct_answers:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The answer is {', '.join(correct_answers)}.")
        return 0


def section_one_quiz():
    score = 0
    questions = [
        ("What iss the capital of the United States?", {"washington dc", "washington d.c."}),
        ("How many states are there in the United States?", {"50","id Honstly accept 45 but thats not accurote most people just think 45 so if you got that you can just feel proud that you got close :D if you got even closer you can feel even better but if you dare get beleoow 45 or above 50 ur so dum lol im jocking but its true not gonna lie wait no im just contrevisign myself and im typing too much and i dont know if im goign to be able to stop can anyone help me ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh wait i know what to do ill try and stop typing big brain ?"}),
        ("What year was the Declaration of Independence signed?", {"1776","good try tho i really didnt know this one till i reasearched it"}),
        ("Who was the first President of the United States?", {"george washington"}),
        ("Which city is known as the 'Big Apple'?", {"new york", "new york city"}),
        ("Who is the current President of the United States?", {"joe biden"}),
        ("When was the 45'th president of the United States in office?", {"2017-2021", "2017 to 2021"})
    ]

    for question, answers in questions:
        score += ask_question(question, answers)

    print(f"\nYour score for this section: {score}/{len(questions)}")
    print("\nRestarting quiz...\n")
    return score

def main():
    show_dev_log = input("Do you wish to see the development log log? ").lower()
    if show_dev_log == "yes":
        display_dev_log()
    else:
        print("Alright, let's continue.")

    while True:
        try:
            choice_selection = int(input("Pick your question group (1-10):\n"))
            if 1 <= choice_selection <= 10:
                if choice_selection == 1:
                    print("You have chosen Section 1: United States Questions")
                    section_one_quiz()
                elif 2 <= choice_selection <= 10:
                    print(f"You have chosen Section {choice_selection}. Questions for this section are not yet implemented.")

            else:
                print("Invalid selection. Please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
option = input (" do you wish to here me rant")#
if option == "yes":
        print("ok ill start so basically i am going to be ranting and talkign to myself in this bit becausei  do not know what else to add and i know this might seem werid but people like me like to write when we dont know what to do now im talking to myself whenever i message myself i feel like im just talking to myself its how i felel ok oh lol i got 1 hour batteryy left xd thats os mebarising to people like me because my screen birghnesss is on a a high level i cannot do my full potentialso yes and yes i am ehreing stupid people outside and are being silly like dayum its so dum hering kids yelling outside whalst im trying to code whalst there are some people talking in here but it is not as bad as those poeple outside sinse they are working togheter my ownly comment on it is that it is a bit too louad for normall people to be talking about but it should not really effect me and i do not want ti to so ye ignore all of this i am just typign to test the askii speed a"
              "dn as of now it is perfect i dont know how it got to a new line i guess it just lowered as i prob typed too much on one line for python to handle xd that is so funny oh i also think that this lession is about to end but i dont know for sure so i will keep typing till im told to stop all of this typing is making my hand hurt but its not mu normal hand its because my rgiht hand needs to keep moving up and down becuase it uses more a high key register so i need to move it up mroe or ive got it posstiiond lower but i dont know which one is ture so yes i also gotta go ill see yall later have a good day ")
else:
        print("ok ill stop now :(:( ")
