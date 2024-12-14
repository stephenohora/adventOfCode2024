# Advent of Code 2024 second day first part
safety_lists, input_list2 = [], []
with open("input2-1.txt") as f:
    for line in f:
        safety_lists.append(line.strip("\n").split(" "))

def check_list(safety_list):
    state = ""
    for idx,value in enumerate(safety_list):
        if idx+1 != len(safety_list):
            check = int(value) - int(safety_list[idx+1])
            if check == 0:
                # print(unsafe)
                # print(f"list number {_}")
                print(f"{value} two values the same {safety_list}")
                return 1
            elif check > 0 and state == "increasing":
                # print(unsafe)
                # print(f"list number {_}")
                print(f"{value} {check} decreasing after increasing {safety_list}")
                return 1
            elif check < 0 and state == "decreasing":
                # print(unsafe)
                # print(f"list number {_}")
                print(f"{value} {check} increasing after decreasing {safety_list}")
                return 1
            elif abs(check) > 3:
                # print(unsafe)
                # print(f"list number {_}")
                print(f"{value} {check} change greater than 3 {safety_list}")
                return 1
            elif check < 0:
                # print(f"list number {_}")
                state = "increasing"
            else:
                # print(f"list number {_}")
                state = "decreasing"
    return 0

safer = 0

for _,safety_list in enumerate(safety_lists[0:473]):
    for idx, item in enumerate(safety_list):
        except:
            pass

        list_to_be_popped = list(safety_list)
        if check_list(list_to_be_popped.pop(idx)) == 0:
            print(f"index {_} removed {safety_list[idx]} from {safety_list} to give {list_to_be_popped}")
            safer += 1
            break
print(safer)
print(safer+526)

