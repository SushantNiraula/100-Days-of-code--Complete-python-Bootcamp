def life_left_in_weeks(age):
    """
    This function takes an age as a parameter and calculates the number of weeks left in life.
    
    Parameters:
    age (int): The current age of the person.
    
    Returns:
    int: The number of weeks left in life.
    """
    # Assuming an average lifespan of 90 years
    average_lifespan = 90
    weeks_in_a_year = 52
    weeks_left = (average_lifespan - age) * weeks_in_a_year
    return weeks_left
# Example usage
age = 25
weeks_left = life_left_in_weeks(age)
print(f"You have approximately {weeks_left} weeks left in your life.")  # Output: You have approximately 3380 weeks left in your life.