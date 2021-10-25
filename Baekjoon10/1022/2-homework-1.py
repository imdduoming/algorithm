shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["s"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    shop_menus.sort()
    left=0
    right=4
    find=0
    for i in shop_orders:
        while left<=right:
            mid=(left+right)//2
            if shop_menus[mid]==i:
                find=1
                break
            elif shop_menus[mid]<i:
                left=mid+1
            else:
                right=mid-1
        if find!=1:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)