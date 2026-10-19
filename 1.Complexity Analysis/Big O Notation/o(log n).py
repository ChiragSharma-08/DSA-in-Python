def find_name(names,target):
    left = 0
    right = len(names)-1

    while left <= right:
        mid = (left+right)//2

        if names[mid] == target:
            return mid

        elif names[mid] < target:
            left = mid+1

        else:
            right = mid-1

    return None

names = ["Aayush", "Abhishek", "Bhavna", "Chandan", "Chirag", "Darshit", "Dhruv" ]

roll_no = find_name(names,"Chandan")

if roll_no != None:
    print(roll_no)
else :
    print("User Not Found")

