def find_paper(Papers, name):
    for paper in Papers:
        if paper == name:
            return True

    return False

papers = names = ["Chandan", "Abhishek", "Bhavna", "Chirag", "Darshit","Aayush", "Dhruv" ]

search_name = "Karan"

result = find_paper(papers,search_name)

if result:
    print("Paper found")
else:
    print("Paper not found")