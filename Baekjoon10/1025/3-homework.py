shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    len_coupons=len(coupons)
    len_prices = len(prices)
    idx=0
    total=0
    while idx<len_coupons:
        total+=prices[idx]*((100-coupons[idx])/100)
        idx+=1

    if idx<len_prices:
        total+=prices[idx]

    return int(total)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.