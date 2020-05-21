
def set(elements):
    print(elements)
    elements.add("motorola")
    print(elements)
    elements.update(["micromax","ficco","blackberry"])
    print(elements)
    print(len(elements))
    elements.remove("ficco")
    print(elements)
    print(elements.pop())
    set1 = {1,4,3,5,8,6}
    set2 = elements.union(set1)
    print(set2)
    set3 = {"apple","mango","pineapple"}
    set2.update(set3)
    print(set2)

n_list = {"iphone", "samsung","xiomi"}
set(n_list)
    
