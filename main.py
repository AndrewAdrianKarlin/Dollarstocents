

## Run the calculation for coin
def coincalc(cents, coin):
    coinnum = cents // coin
    remainder = cents % coin
    return (coinnum, remainder)

## call the calculation for each coin
def coins(cents):
    if cents > 24:
        quarters, cents = coincalc(cents, 25)
    if cents > 9:
        dimes, cents = coincalc(cents, 10)
    if cents > 4:
        nickels, cents = coincalc(cents, 5)
    if cents > 1:
        pennies = cents
    return quarters, dimes, nickels, pennies


## Input loop
dollars = float(input('How much do you have in dollars and cents?'))
cents = int(dollars*100)
coins = coins(cents)
print(f'You have {coins[0]} quarters, {coins[1]} dimes, {coins[2]} nickels, and {coins[3]} pennies')