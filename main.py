import csv

user_input = input("please type in an animal name: ").lower()
try:
    with open(f"data/{user_input}.csv") as file:
        data = csv.reader(file, delimiter=",")
        line_count = 0
        for row in data:
            if line_count == 0:
                line_count+=1
                continue
            print(f"{row[0].title()} is a {row[1]} year old {row[2]} {user_input[:-1]}")
            
except:
    print(f"sorry we dont have any {user_input} here")
