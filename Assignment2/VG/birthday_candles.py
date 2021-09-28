__author__ = "Tadj Cazaubon"

"""
This program computes how many boxes of candles a person
needs to buy each year for her/his birthday cake given
the following:

+ Each box contains 24 candles
+ The number of candles used each year is the same as the age
+ You save non-used candles from one year to another
+ The person reaches an age of 100

At the end, we print the total number of boxes one has to buy,
and how many candles that are available after having celebrated
the 100th birthday
"""

# Count for the number of candles left between birthdays
candles_left = 0
# Count for the total number of boxes bought over 100 birthdays
total_boxes = 0
# Range of birthdays [1, 100]
years = [year for year in range(1, 101)]


for year in years:
    # We first set boxes to 0 so we determine it year to year
    boxes = 0
    while year > candles_left:
        # If there aren't enough candles left, we buy a box with 24 candles
        candles_left += 24
        boxes += 1
        total_boxes += 1

    # Once we have enough candles for the birthday, we use them
    candles_left -= year

    # Only the birthdays which require us to buy boxes are printed
    if boxes > 0:
        print(f"Before birthday {year}, buy {boxes} box(es)")

print(f"\nTotal number of boxes: {total_boxes}, Remaining candles: {candles_left}\n")
