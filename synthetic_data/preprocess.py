label = []
with open('/home/aclab/Documents/direse/dataset/word/ethiopic/label.txt', 'r') as f:
    line = f.readline()
    for i in f:
        i = i.strip()
        i = i.split("/")[-1]
        i = i.split(" , ")[0]
        label.append(i.strip()) 

train = int(len(label)*0.6) #take 
valid = int(len(label)*.2)
test = int(len(label)*.2)
print("train = ",train, "test = ",test, "valid = ", valid)

train_label = label[:train] # take only 30,000 -> train
test_label1 = label[train+1:]

test_label = test_label1[:int(len(test_label1)*.5)]
valid_label = test_label1[int(len(test_label1)*.5)+1:]
print(len(test_label), len(valid_label))

f = open("test_label.txt","w") 
for i in test_label:
    f.writelines(i+"\n") 

f = open("valid_label.txt","w") 
for i in valid_label:
    f.writelines(i+"\n")
    
f = open("train_label.txt","w") 
for i in train_label:
    f.writelines(i+"\n")

 