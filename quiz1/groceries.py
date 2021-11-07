def checkout(cash: float, list: dict) -> float:
    """
    build a function that sums up the value of the grocery list and subtracts that
    from the cash passed into the function.
    return the "change" from the cash minus the total groceries value.
    """
    grocery_cost = sum(list.values())
    change = cash - grocery_cost
    return change
