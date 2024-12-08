# Advent of Code 2024 first day secnd part
input_list1, input_list2 = [], []
with open("input1-1.txt") as f:
    for line in f:
        linepair = line.split('   ')
        # print(linepair[0])
        linepair[1] = linepair[1].strip("\n")
        # print(linepair[1])
        input_list1.append(linepair[0])
        input_list2.append(linepair[1])
# print(input_list1)
input_list1.sort()
input_list2.sort()
# print(input_list1)
similarity_score = 0
for idx,item in enumerate(input_list1):
    running_total = 0
    checknumber = int(item)
    for check_item in input_list2:
        if checknumber == int(check_item):
            running_total += 1
    similarity_score += checknumber * running_total
print(similarity_score)
