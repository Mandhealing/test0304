import time


now_day = time.strftime("%Y/%m/%d")
list_name = '每日歌单推荐---' + now_day
print(list_name)




def gotta():
    file_name = "myaccount.txt"
    dataset = []
    file = open(file_name, mode='r')
    for line in file:
        line = line.split()
        dataset.append(line)
        print(dataset)
    file.close()