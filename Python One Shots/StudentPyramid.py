# num_students=int(input())
# n = ""
# m = ""
# while num_students > 0:
#     m = n + "\\o/\\o/" 
#     while num_students > 2:
#         num_students -= 1
#         n = n + " "
#     m = m + "\\o/"
#     print(m)
#     n = n - " "
# print("student line")

num_students = int(input("Enter the number of students: "))

for i in range(1, num_students):
    spaces = " " * (num_students - i-1)  # Add spaces for alignment
    row = "\\o/" * i  # Create the row with the correct number of \o/
    row = row + "\\o/"
    print(spaces + row)  # Print the aligned row

print("student pyramid")
