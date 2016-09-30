initial_savings = 5000
interest_rate = 0.03

print('Initial savings of $%d' % initial_savings)
print('at %d%% yearly interest.\n' % (interest_rate*100))

years = int(input('Enter years: '))

savings = initial_savings
i = 1  # Loop variable
while savings <= 7500:  # Loop condition
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable
    if(savings>7500):
        print('i', i)

print('\n')