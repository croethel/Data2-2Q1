def meters_to_feet(meters: float) -> float:
    """
    This function takes a float representing a measurement in meters
    and returns the corresponding value converted to feet.
    The result is rounded to 2 decimal places.
    :param meters: A float representing a measurement in meters.
    :return: A float representing the input measurement converted to feet.
    """
    feet = meters / 3.28084
    feet_float = round(feet, 2)
    return feet_float


def feet_to_meters(feet: float) -> float:
    """
    This function takes a float representing a measurement in feet
    and returns the corresponding value converted to meters.
    The result is rounded to 2 decimal places.
    :param feet: A float representing a measurement in feet.
    :return: A float representing the input measurement converted to meters.
    """
    meters = feet * 3.28084
    meters_float = round(meters, 2)
    return meters_float
