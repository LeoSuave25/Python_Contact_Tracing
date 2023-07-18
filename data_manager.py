import csv

class DataManager:
    def save_data(filename, questions, data):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)

            # Check if the file is empty
            if file.tell() == 0:
                writer.writerow(questions)

            writer.writerow(data)
