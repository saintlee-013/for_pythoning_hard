grocery_list = [
    {'name': 'apple', 'quantity': 2, 'price': 3},
    {'name': 'banana', 'quantity': 5, 'price': 2},
    {'name': 'carrot', 'quantity': 4, 'price': 1}
]
l = len(grocery_list)
l_names = []
l_q = []
l_p = []
l_ta = []
element = 0
def cal(items):
 for items in items:
        name_val = items['name']
        l_names.append(name_val)
        q_val = items['quantity']
        l_q.append(q_val)
        p_val = items['price']
        l_p.append(p_val)
 for i in range(len(l_p)):
     ele = l_q[i]*l_p[i]
     l_ta.append(ele)

def total_bill_amount(items):
    cal(grocery_list)
    total_am = []
    global element
    for i in range(l):
     element = element + (l_p[i])*(l_q[i])
    return(element)

def max_quantity_item(items):
    cal(grocery_list)
    maximum = max(l_q)
    index = l_q.index(maximum)
    li = []
    li = grocery_list[index]
    dict_li = dict(li)
    name_of_max = dict_li['name']
    return(name_of_max)

def sort_by_total_amount(items):
     cal(grocery_list)
     sorted_list = sorted(
        items, 
        key=lambda item: item['price'] * item['quantity'],
        reverse=True # Set to True for DESCENDING order (highest total first)
    )
     return sorted_list
    
    
max_quantity_item(grocery_list)   
total_bill_amount(grocery_list)   
sort_by_total_amount(grocery_list)

