select_all_female_bears_return_name_and_age = """
    SELECT 
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT bears.name 
    FROM bears
    ORDER BY name ASC
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT bears.name,bears.age
    FROM bears
    WHERE bears.alive = TRUE
    ORDER BY bears.age ASC
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT bears.name,MAX(age)
    FROM bears
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT bears.name,MIN(age)
    FROM bears
"""
