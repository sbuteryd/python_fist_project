"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records.
"""
# def count_number(text,call):
#     del_number = []
#     for i in zip(text,call):
#         del_number.append(i[0])
#         del_number.append(i[1])
#     finall_number = set(del_number)
#     return  len(finall_number)
#
#
# count_number= count_number(texts,calls)
#
def finall_number(text,call):
    list_all =[]
    for text,call in zip(texts,calls):
        list_all.append(text[0])
        list_all.append(call[0])
        list_all.append(text[1])
        list_all.append(call[1])
    return  len(set(list_all))

count_number = finall_number(texts,calls)

print("There are {} different telephone numbers in the records.".format(count_number))
