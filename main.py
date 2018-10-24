import csv, sys, json
from encoding import encoder_decoder

source_file='hotels.csv'
destination_json='hotel.json'

row = ''
with open(source_file, mode='r') as hotels_file:
    csv_reader = csv.reader(hotels_file, delimiter=',')
    i = 0
    columns = ''
    try:
        for row in csv_reader:
            if i == 0:
                columns=row
                print ('Column names are', ' '.join(row))
                i += 1
            else:
                # with io.open('data.txt', 'w', encoding='utf-8') as f:
                # boh=split(row)
                # import pdb; pdb.set_trace()
                print ('Hotel Details: ', encoder_decoder.make_unicode(''.join(row)))
                i += 1
                if i > 2:
                    import pdb; pdb.set_trace()
                    
                    break

            print('Processed {} lines.'.format(i))
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (source_file, csv_reader.line_num, e))
