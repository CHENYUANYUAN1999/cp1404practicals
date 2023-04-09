"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    my_list = []
    data = get_data()
    print(data)
    find_teacher(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_list.append(tuple(parts))
    input_file.close()
    return data_list

def find_teacher(datas):
    for data in datas:
        print(f"{data[0]} is taught by {data[1]} and has {data[2]} students.")
main()