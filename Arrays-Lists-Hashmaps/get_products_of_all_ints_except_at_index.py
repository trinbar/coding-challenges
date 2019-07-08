#You have a list of integers, and for each index you want to
# find the product of every integer except the integer at that index.

#Write a function get_products_of_all_ints_except_at_index() that
# takes a list of integers and returns a list of the products.

#For example, given:

  #[1, 7, 3, 4]

#your function would return:

  #[84, 12, 28, 21]
 
#by calculating:

  #[7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
 
#Here's the catch: You can't use division in your solution!

def get_products_of_all_ints_except_at_index(int_list):
    """Returns the products of all ints excluding int at index."""

    if len(int_list) < 2:
        return IndexError("Requires 2 numbers")

    #Initialize a list with the length of the input list to hold products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    #to iterate over a list in reverse using for loop and range()...
    for i in range(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    return products_of_all_ints_except_at_index