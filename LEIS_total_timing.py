import datetime

def wc_dictionary(input_file):
    wc_list = []
    wc_time = []
    wc_dic = {}
    for line in input_file:
        if line.find("Bulk Refresh") != -1:
            wc_list.append(line.split()[0])
        if line.find("Refresh:") != -1:
            wc_time.append(line.split()[1])
    for i in range(len(wc_list)):
        wc_dic.update({wc_list[i]:wc_time[i]})
    return wc_dic

def elapsed_time(input_file):
    timestamp1, timestamp2 = '',''
    for line in input_file:
        if line.find("Initialize Run:") != -1:
           timestamp1 = (line.split()[3][1:])
        break
    for line in reversed(list(f)):
        if line.find("Final Clean-up:") != -1:
            timestamp2 = (line.split()[5][:8])
        break
    print (timestamp1, timestamp2)
   # return timestamp2 - timestamp1

f = open("d:/OneDrive/1.txt")


elapsed_time(f)
refresh_time = [int(i) for i in list(wc_dictionary(f).values())]
print('Total refresh time : ', sum(refresh_time), "seconds\n")
#print('Total refresh time HH:MM:SS : ', datetime.timedelta(seconds=sum(refresh_time)))


f.close