a = "19"
limit = 3
count = 0

while count < limit:
    age = input("Guess my age:")

    if age == a:
        print("You are goddam right!")
        break
    else :
        print("Wrong, Remaining guesses:" + str(limit - count - 1))
        count += 1

if count == limit:
    print("You are out of guesses, My age is 19")
