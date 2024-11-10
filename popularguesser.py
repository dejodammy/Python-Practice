from hangmanart import * 
import random
def main():     
    def generate_people():
        random_people = random.sample(list(instagram_top_people.items()), 2)
        person1, person2 = random_people   
        print(f" The first person is: {person1[0]} and has {person1[1]} followers")
        print(f" The Second Person is {person2[0]} ") 
        return person1 , person2

    score = 0
    person1, person2 = generate_people()
    while True:   
        choice = (input(" Does Person 2 have Higher Or Lower Followers? ")).strip().lower()
        def high_or_low(person1,person2):
            if person1 > person2:
                return "lower"
            elif person1 < person2:
                return "higher"
            elif person1 == person2:
                return "equal"
        answer = high_or_low(person1[1],person2[1])    
        if (choice == "lower" and answer == "lower") or (choice == "higher" and answer == "higher") or (choice == "higher" and answer == "equal") or (choice == "lower" and answer == "equal"):
            
            score += 1
            print(f"Correct! {person2[0]} has {person2[1]} followers.\nYour Score Is {score} ")


            instagram_top_people.pop(person1[0])
            instagram_top_people.pop(person2[0])

            if len(instagram_top_people) < 1:
                print(f"You Finished The Game. Your final score is {score}.")
                break

            # Set the new first and second persons
            person1 = person2
            person2 = random.choice(list(instagram_top_people.items()))
            print(f"The new second person is: {person2[0]}")
            
        else:
            print(f"Wrong! {person2[0]} has {person2[1]} followers.\nYour score is {score}.")
            break
    

if __name__ == "__main__":
    main()