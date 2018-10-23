import csv


with open('hotels.csv', mode="r") as hotels_file:
    csv_reader = csv.reader(hotels_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print ('Column names are').join(row)
            line_count += 1
        else:
            print ('Hotel Details: ', row)
            line_count += 1
    print('Processed {line_count} lines.')