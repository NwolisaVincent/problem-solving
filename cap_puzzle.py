def please_conform(gathering):
    gathering_index = []  # used to hold the index of values we'd like to work with
    for position, i in enumerate(gathering):  # let's loop through the given data
        if i == 'F':
            pass
        elif i == 'B':
            gathering_index.append(position)  # if a person has a backward cap append the index of the person.
        else:
            print("Something went wrong!")  # Incase something happens.
            quit()
    if not gathering_index:  # if nothing is in the list tell them it's empty.
        print("Empty list!")
        quit()

    groups = []  # we'd use this to store tuples that are consecutive related
    start_count = gathering_index[0]  # we'd start with the first number for the first tuple

    for i in range(1, len(gathering_index)):  # let's loop through the index of numbers we're working with
        if gathering_index[i] - gathering_index[i - 1] == 1:  # Notice how we're subtracting 'i' from 'i-1'
            continue
        else:
            groups.append((start_count, gathering_index[i - 1]))  # appending the tuples
            start_count = gathering_index[i]  # updating the value of the start_count

    groups.append((start_count, gathering_index[-1]))  # if none again append the last number with the last number

    j = 0
    while j < len(groups):
        if groups[j][0] == groups[j][-1]:
            print(f"People in position {groups[j][0]} flip your caps!")
            j += 1
        elif groups[j][0] != groups[j][-1]:
            print(f"People in position {groups[j][0]} through {groups[j][-1]} flip your caps!")
            j += 1


audience = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
print("Groups of people who are to flip their caps: ")
print(please_conform(audience))
