"""Problem Set 7: Working 9 to 5
https://cs50.harvard.edu/python/2022/psets/7/working/

In a file called working.py, implement a function called convert that expects a str in either of
the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space
before each. Assume that these times are representative of actual times, not necessarily 9:00 AM
and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either
time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone's hours will start
ante meridiem and end post meridiem; someone might work late and even long hours
(e.g., 5:00 PM to 9:00 AM).

"""

import re


def main():
    print(convert_time(input("Hours: ")))


def convert_time(work_hours):
    """Convert string containing start and stop time of work from 12 hour format to 24
    hour (military time) format.

    Parameters
    ----------
    work_hours : str
        start and stop time of work, in 12-hour format.

    Returns
    -------
    str
        Start and stop times in 24-hour time formats

    Raises
    ------
    ValueError
        Raised if work_hours are not in proper 12-hour formats, missing AM/PM, or have
        minutes/hours outside appropriate ranges.
    """
    time_regex = r'(\d\d?)(:\d\d)? (AM|PM)'
    pattern =  ' to '.join([time_regex] * 2)
    match = re.match(pattern, work_hours)

    if match:
        # Put match data into a dictionary for easier processing
        time_data = {
            'start': {
                'hour' : match.group(1),
                'min' : match.group(2),
                'meridiem' : match.group(3)
            },
            'stop' : {
                'hour' : match.group(4),
                'min' : match.group(5),
                'meridiem' : match.group(6)
            }
        }

        for t in ['start', 'stop']:
            # Populate minutes with '00' if it's missing
            if time_data[t]['min'] == None:
                time_data[t]['min'] = '00'

            if time_data[t]['min'].startswith(':'):
                time_data[t]['min'] = time_data[t]['min'][1:]

            # Check that hours and minutes are in appropriate ranges
            if not 1 <= int(time_data[t]['hour']) <= 12:
                raise ValueError('Date is not in a poper format.')

            if not 0 <= int(time_data[t]['min']) <= 59:
                raise ValueError('Date is not in a proper format.')

            # Left pad AM hour values with '0' (that's what the zfill() function does)
            if time_data[t]['meridiem'] == 'AM':
                time_data[t]['hour'] = time_data[t]['hour'].zfill(2)
            # Add 12 to PM hour values
            elif time_data[t]['meridiem'] == 'PM':
                time_data[t]['hour'] = str(int(time_data[t]['hour']) + 12)

        return f"{time_data['start']['hour']}:{time_data['start']['min']} to {time_data['stop']['hour']}:{time_data['stop']['min']}"

    else:
        raise ValueError('Date not in proper format.')



if __name__ == "__main__":
    main()