"""
Day 10 - 2026-10-16
Tool: Percentage & Marks Calculator
What it does: Works out percentages for everyday life - exam marks and
grades, what percent one number is of another, discounts as a percent,
and how much a price or salary has gone up or down in percent.
Who it helps: Students checking exam results, shoppers comparing offers,
and anyone checking a pay rise, a bill change, or a savings target.
"""


def percent_of(part, whole):
    """Return what percent 'part' is of 'whole', rounded to 2 decimals."""
    if whole == 0:
        raise ValueError("The whole/total value cannot be zero.")
    return round((part / whole) * 100, 2)


def value_of_percent(percent, whole):
    """Return the actual value of a percent of a total (e.g. 15% of 2000)."""
    return round((percent / 100) * whole, 2)


def marks_result(obtained, total):
    """Return a student's percentage and a simple grade for their marks."""
    pct = percent_of(obtained, total)
    if pct >= 80:
        grade = "A+"
    elif pct >= 70:
        grade = "A"
    elif pct >= 60:
        grade = "A-"
    elif pct >= 50:
        grade = "B"
    elif pct >= 40:
        grade = "C"
    elif pct >= 33:
        grade = "D"
    else:
        grade = "F"
    return {"percentage": pct, "grade": grade}


def percent_change(old_value, new_value):
    """Return the % increase (positive) or decrease (negative)."""
    if old_value == 0:
        raise ValueError("The old value cannot be zero.")
    return round(((new_value - old_value) / old_value) * 100, 2)


if __name__ == "__main__":
    # Example 1: a student checking exam marks out of 600
    print("Marks 468/600:", marks_result(468, 600))

    # Example 2: how much of a 50,000 taka salary is spent on rent of 15,000?
    print("Rent share of salary:", percent_of(15000, 50000), "%")

    # Example 3: a price rose from 800 to 920 taka - how much in percent?
    print("Price change 800 -> 920:", percent_change(800, 920), "%")
    print("15% of 2000 is:", value_of_percent(15, 2000))
