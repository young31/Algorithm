def solution(price, money, count):
    total_price = price * count*(count+1)//2
    answer = 0 if total_price <= money else total_price-money

    return answer