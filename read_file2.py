import os

with open("test_file.txt", "w") as f:
    f.write("Hello world!\nShalom olam\nHey, Hello Baruch\nHello David")
with open("test_file_copy.txt", "w") as f:
    f.write("Hello world!\nShalom olam\nHey, Hello Baruch\nHello David")
with open("test_file_diff.txt", "w") as f:
    f.write("Different content")





def get_lines_starting_with(filename, string):
    result = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip().startswith(string):
                result.append(line.strip())
    return result







def print_file_formatted(filename):
    with open(filename, "r") as f:
        for line in f:
            content = line.strip()
            print(f"{len(content)} ** {content} **")







def compare_files_lazy(file1, file2):
    if file1 == file2:
        return True
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            while True:
                line1 = f1.readline()
                line2 = f2.readline()
                if line1 != line2:
                    return False
                if not line1:
                    return True
    except:
        return False

print(get_lines_starting_with("test_file.txt", "Hello"))
print("-" * 20)
print_file_formatted("test_file.txt")
print("-" * 20)
print(compare_files_lazy("test_file.txt", "test_file_copy.txt"))
print(compare_files_lazy("test_file.txt", "test_file_diff.txt"))