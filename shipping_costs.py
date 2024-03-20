# shipping_costs.py
# Bryn Bijur, s1324044
# CS-175
# Spring 2022
def main():
    state_province, country, cost = get_shipping()
    print("Shipping cost to", state_province, ",", country, ":", cost)


def get_shipping():
    state_province = str(input("Enter the state or province:"))
    country = str(input("Enter the country:"))
    if country == "USA":
        if state_province == "AK" or state_province == "HA":
            cost = "$15.00"
        else:
            cost = "$10.00"
    else:
        cost = "$20.00"
    return state_province, country, cost


main()
