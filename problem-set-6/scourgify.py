"""CS50P -- Problem Set 6: Scourgify
Source: https://cs50.harvard.edu/python/2022/psets/6/scourgify/

"""

# Pandas way
# import pandas as pd

# hogwarts = pd.read_csv('https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv')

# hogwarts['first_name'], hogwarts['last_name'] = hogwarts['name'].str.split(', ').str
# hogwarts.drop(columns=['name'], inplace=True)

# hogwarts.to_csv('new_hogwarts.csv', index=False)
# print(hogwarts.to_string(index=False))

# With urlopen

from urllib.request import urlopen


in_file_URL = 'https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv'
out_file = 'new_hogwarts2.csv'

with open(out_file, 'w') as _out:
    for i, line in enumerate(urlopen(in_file_URL)):
        # Convert from bytes to string
        line = line.decode('utf-8')

        if i == 0:
            # Replace the header row string with appropriate column labels
            line = line.replace('name', 'first_name,last_name').replace('\r', '')
            # NB: Somewhat surprisingly, the line endings appear have both a Carriage Return
            # and a Line Feed (CR/LF or `\r\n` in the string). Maybe that's happening in the
            # decoding? Therefore, we need to strip one of them off, otherwise
            # the output file will have blank lines written out between each line.

        # For all other rows, remove the "s, remove the space after the comma inside the
        # (former) "name" column, and remove the carriage return.
        else:
            line = line.replace('"', '').replace(', ', ',').replace('\r', '')

        _out.write(line)


in_file = 'C:/Users/kevinp/Downloads/before.csv'
out_file = 'new_hogwarts3.csv'

with open(out_file, 'w') as _out, open(in_file) as _in:
    for i, line in enumerate(_in):

        # For the header row,
        # Replace the string with old 'name' column label with the two new column labels
        if i == 0:
            line = line.replace('name', 'first_name,last_name')

        # For all other rows,
        # remove the "s, and the space after the comma inside the (former) "name" column
        else:
            line = line.replace('"', '').replace(', ', ',')

        _out.write(line)

