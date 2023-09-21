def linear_search_product(productsList, targetProduct):
    indices = []

    for index,product in     enumerate(productsList):     
      if product == targetProduct:
            indices.append(index)
        
    return indices

#Example usage:
products =["shoes","boot","loafer","shoes","sandal","shoes"]
target ="shoe"
target2 ="apple"
result = linear_search_product(products, target2)
print(result)