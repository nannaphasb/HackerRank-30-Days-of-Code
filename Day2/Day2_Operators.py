def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    total_cost = meal_cost + (meal_cost/100 * tip_percent) + (tax_percent/100 * meal_cost)
    rounded_total_cost = round(total_cost)
    print(rounded_total_cost)
    
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)