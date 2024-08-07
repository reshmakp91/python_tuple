def avg(persons):
    total = 0
    for x in persons:
        total += x[1]
    average = total/len(persons)
    return average

persons = [("Reshma", 33), ("Arun", 39), ("Sreehari", 3)]
print(f"The average age of the group is {avg(persons)} years.")
