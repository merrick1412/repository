"""
Name:Merrick Moncure
Date: 1/12/25
Assignmnent: Module 1: EisensteinPrimes
Displays all eisenstein numbers below entered number
Assumptions: NA
All work below was performed by Merrick Moncure
"""
import random
from concurrent.futures import ThreadPoolExecutor

def random_calc(x1,x2): # calculates the random number between the bounds
    randnum = random.randint(x1,x2)
    return randnum**2 - 3 * randnum

def main():
    """
    executes program
    """
    x1, x2 = 0, 20
    num_trials = 100000
    #ThreadPoolExecutor w 3 workers
    with ThreadPoolExecutor(max_workers=3) as executor: #gives 100000 trials to executor
        results = executor.map(random_calc, [x1] * num_trials, [x2] * num_trials)

    total = sum(results)
    area = total * (x2 - x1) / float(num_trials)
    print(f"The area of the integral is: {area}")

main()