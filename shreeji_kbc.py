import random
kbc={"Which city is known as city of SHREENATHJI":(["Nathdwara","Udaipur","Jaipur","Banswara"],"Nathdwara"),
    "Which city is known as city of 100 ISLANDS":(["Nathdwara","Udaipur","Jaipur","Banswara"],"Banswara"),
    "Which city is known as city of LAKES":(["Nathdwara","Udaipur","Jaipur","Banswara"],"Udaipur"),
    "Which city is known as PINK CITY":(["Nathdwara","Udaipur","Jaipur","Banswara"],"Jaipur")}
score=0
used=0
for question,data in kbc.items():
    options,ans=data
    print("This question is for :",(score+1)*10000)
    print("Type LIFELINE if you want to use lifeline")
    print(question)
    count=1
    for i in options:
        print(count, i)
        count+=1
    answer=input("Choose your answer :")
    if answer=="LIFELINE" and used==0:
        used=1
        remaining=[ans]
        while len(remaining)<2:
            opt2=random.choice(options)
            if opt2!=ans:
                remaining.append(opt2)
            random.shuffle(remaining)
            count=1
            for i in remaining:
                print(count, i)
                count+=1
            answer=input("Choose your answer :")
        if answer.isdigit() and int(answer)>=1 and int(answer)<=2:
            if remaining[int(answer)-1]==ans:
                print("Correct Answer")
                print()
                score+=1
                continue
            else:
                print("Wrong Answer")
                break
        else:
            print("You entered wrong output! Restart")
    if answer=="LIFELINE" and used==1:
        print("no lifeline left")
        answer=input("enter your answer: ")
    
    if answer.isdigit() and int(answer)>=1 and int(answer)<=4:
        if options[int(answer)-1]==ans:
            print("Correct Answer")
            print()
            score+=1
            continue
        else:
            print("Wrong Answer")
            break
    else:
        print("You entered wrong output! Restart")

print()
print("You won : ",score*10000)