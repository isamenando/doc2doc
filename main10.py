# Fix the sort_dates function. It takes as input a list of dates in "MONTH-DAY-YEAR" format and returns a list of the dates sorted in ascending chronological order.
# Original code:
# def sort_dates(dates):
#    dates.sort()
#    return dates

#Solution:
def sort_dates(dates):
    # Sort dates using a custom key that reformats the date for correct chronological order
    return sorted(dates, key=format_date)

# Helper function to reformat date for correct sorting
# The function converts "MONTH-DAY-YEAR" to "YEARMONTHDAY"
def format_date(date):
    month, day, year = date.split("-")
    return year + month + day