# Advent of Code 2024 second day first part
safety_lists, input_list2 = [], []
with open("input2-1.txt") as f:
    for line in f:
        safety_lists.append(line.strip("\n").split(" "))
unsafe = 0
# print(safety_lists[0:10])
for _,safety_list in enumerate(safety_lists):
    state = ""
    for idx,value in enumerate(safety_list):
        # if idx+1 != len(safety_list)
        try:
            check = int(value) - int(safety_list[idx+1])
            if check == 0:
                unsafe += 1
                print(unsafe)
                print(f"list number {_}")
                print(f"{value} two values the same {safety_list}")
                break
            elif check > 0 and state == "increasing":
                unsafe += 1
                print(unsafe)
                print(f"list number {_}")
                print(f"{value} {check} decreasing after increasing {safety_list}")
                break
            elif check < 0 and state == "decreasing":
                unsafe += 1
                print(unsafe)
                print(f"list number {_}")
                print(f"{value} {check} increasing after decreasing {safety_list}")
                break
            elif abs(check) > 3:
                unsafe += 1
                print(unsafe)
                print(f"list number {_}")
                print(f"{value} {check} change greater than 3 {safety_list}")
                break
            elif check < 0:
                # print(f"list number {_}")
                state = "increasing"
            else:
                # print(f"list number {_}")
                state = "decreasing"
        except:
            pass
    # print(f"safe {safety_list}")           
print(len(safety_lists))
print(unsafe)
print(len(safety_lists)-unsafe)
