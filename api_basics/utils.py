# define the menu function
def get_menu() -> dict:

    menu = {
        'rice':500,
        'beans':300,
        'beef': 1000,
        'chicken': 1500
    }
    return menu

# define the get_order function
def get_order(**order):
    menu = get_menu()
    difference = [x for x in order.keys() if x not in menu.keys()]
    if len(difference) == 0:
        total_cost = 0.0
        price = list(menu.values())
        quantity = list(order.values())
        for i, v in zip(price,quantity):
            total_cost += (i * v)
            
    return total_cost

if __name__ == "__main__":
    print(get_order(rice=2,beans=3, beef = 1))

