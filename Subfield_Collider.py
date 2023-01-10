
#Part 1: Create List of Topics
path="C:\\...\\" #add the file path where the ScienceDisciplines.txt file is located on your computer
file="ScienceDisciplines.txt"

topic_list=[]
for line in open(path+file):
    if ' - ' in line:
        topic=line.split(' - ')[0]
    elif ' â€“ ' in line:
        topic=line.split(' â€“ ')[0]
    else:
        topic=line.strip('\n')
    topic_list.append(topic)    

#Part 2: Function For Selecting 2 Random Topics
def collider():
    print("How many collisions do you want?: ")
    x = int(input())
    seq = [i+1 for i in range(x)]
    for j in seq:
        pair=random.sample(topic_list, 2)
        print(pair[0] + ' + ' + pair[1]+ '\n')

