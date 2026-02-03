"""א. זיכרון נדיף מייד כשיפסיק החשמל למחשב הוא ימחק וזיכרון שאינו נדיף נשאר תמיד
ב. ssd hard disk
ג. לסגור ולשמור את הקובץ
ד. a- לפתוח את הקובץ ולהוסיף לו מידע, w- לפתוח את הקובץ ולהכניס בו מידע שדורס את המידע הקודם, r- לפתוח את הקובץ ולקרוא אותו
"""

# def open_file():
#     with open("example.txt", "w") as f:
#         f.write("Hello, World")
# open_file()

# def read_file():
#     conect = ""
#     with open("example.txt", "r") as f:
#         for line in f:
#             conect += line
#             if len(conect) == 50:
#                 break
#     print(conect)
# read_file()
 

# def write_file_safe(filename, text):
#     try:
#         with open(filename, "w") as file:
#             file.write(text)
#         return True
#     except Exception:
#         return False

# print(write_file_safe("success_file.txt", "This worked!"))

# print(write_file_safe("folder_not_exist/fail_file.txt", "This will fail"))


# with open("lines_test.txt", "w") as f:
#     f.write("Hello World!\nShalom olam\nHey, Hello Baruch\nHello David")

# def filter_lines_by_start(filename, start_str):
#     result = []
#     with open(filename, "r") as file:
#         for line in file:
#             if line.strip().startswith(start_str):
#                 result.append(line.strip())
#     return result

# print(filter_lines_by_start("lines_test.txt", "Hello"))



# with open("file_a.txt", "w") as f: f.write("Same Content")
# with open("file_b.txt", "w") as f: f.write("Same Content")
# with open("file_c.txt", "w") as f: f.write("Different Content")

# def are_files_identical(file1, file2):
#     try:
#         if file1 == file2:
#             return True
#         with open(file1, "r") as f1, open(file2, "r") as f2:
#             return f1.read() == f2.read()
#     except Exception:
#         return False

# print(are_files_identical("file_a.txt", "file_b.txt"))
# print(are_files_identical("file_a.txt", "file_c.txt"))