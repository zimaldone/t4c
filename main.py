import csv, sys, json
from encoding import encoder_decoder

source_file='hotels.csv';
destination_json='hotel.json'

with open(source_file, mode='r') as hotels_file:
    csv_reader = csv.reader(hotels_file, delimiter=',')
    i = 0
    columns = '';
    try:
        for row in csv_reader:
            if i == 0:
                columns=row
                print ('Column names are', ' '.join(row))
                i += 1
            else:
                # with io.open('data.txt', 'w', encoding='utf-8') as f:
                # boh=split(row)
                print ('Hotel Details: ', encoder_decoder.make_unicode(''.join(row)))
                i += 1
            print('Processed {line_count} lines.')
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (source_file, csv_reader.line_num, e))
