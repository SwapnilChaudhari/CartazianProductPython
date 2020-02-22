# select only one element from each list, apply square
data = [[1, 2, 3, 4], [5, 6, 7, 8], [8, 9, 10]]

def getCartezianProduct(N):
    # storing 1st row elements as lists in product
    product = [[x] for x in N[0]]
    rest_rows = N[1:]
    for i in range(0, len(rest_rows)):
        # tmp will store cartezian products
        tmp = []
        # iterate through rest rows
        for n in rest_rows[i]:
            # print(n)
            # iterating through list items in product
            for j in product:
                # fetching elements from list items of products
                element = [x for x in j]
                # appending current elemnt of input data
                element.append(n)
                # storing cartezian product in tmp for each elemnts of current row
                tmp.append(element)
                # print(tmp)
        # replacing product with product till ith or current row
        product = tmp
    return product


product = getCartezianProduct(data)
print(product)

