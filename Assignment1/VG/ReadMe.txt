
>sumofthree.py:
    I take in the input digits as a string via input()
    When getting keyboard input using the input() method, the default type is a string,
    so I separate the digits via string indexing, and change them into integers to sum them. 

> change.py:
    I take the price and payment amount using input(), and convert them to floats.
    I calculate and print the change.
    Instead of manually writing out checks for each bill type, I made each type an element in a list in 
    descending order by amount and iterate over each. I use integer division to find the number of bills needed,
    then subtract that money amount from the change. This starts with the largest bill and ends with the smallest one. 

> tax.py:
    Since the income is taxed according to tiers, and each tier taxes the difference between the that income and the last tier,
    my first step is to first put the income into a tier. Since having a higher tier of income gives a constant lower tier tax,
    the only dynamic variable is the difference between the income and the last tax tier. I initialize each category tax variable at 0, 
    so that if the income doesn't cross into a higher tax bracket, it remains at 0 and adds nothing to the sum of the taxes at the end.
    If the income crosses into a higher tax bracket, the respective category tax variable is assigned the new income tax amount.

> squarecolor.py
    I store each square in a dictionary as a key, with it's color of either black or white being the value. When a position is given
    as user input, it's sent to the dictionary as a a key and the color is returned as a value.