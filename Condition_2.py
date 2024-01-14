# member_grade = [normal, super_normal, VIP, super_VIP, VVIP]
# region = [seoul, cheonan, deagu, gwangju]
# price_1 = 10,000
# price = price_1 * number

# if member_grade == seoul:
#     if region == super_normal:
#        price_1 = price * 0.85
#     if region == VIP:
#        price_1 = price * 0.75
#     if region == super_VIP:
#        price_1 = price * 0.65   
#     if region == VVIP:
#        price_1 = price * 0.55
    
# else:
#    price_1 = price * 1.00
   
   # 회원 등급과 지역, 가격 정의
member_grade = 'VIP'  # 예시로 'VIP'를 사용
region = 'seoul'      # 예시로 'seoul'을 사용
price = 10000         # 초기 가격

# 지역이 서울일 경우
if region == 'seoul':
    if member_grade == 'super_normal':
        price = price * 0.85
    elif member_grade == 'VIP':
        price = price * 0.75
    elif member_grade == 'super_VIP':
        price = price * 0.65
    elif member_grade == 'VVIP':
        price = price * 0.55
# 그 외 지역일 경우
else:
    price = price * 1.00

print(price)
