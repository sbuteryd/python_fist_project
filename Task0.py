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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def message_print(number):
    # list destructuring
    f_number,f_anwer,f_time= texts[number]
    message = "First record of texts, {} texts {} at time {}".format(f_number,f_anwer,f_time)
    return  message

def  phone_number(figure):
    f_number,f_anwer,f_time,f_second,= calls[figure]
    message = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(f_number,f_anwer,f_time,f_second)
    return message

print(message_print(0))
print(phone_number(0))