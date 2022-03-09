from datetime import datetime

def solution(fees, records):
    
    car = {} #차량 번호, 누적 주차시간
    car_in = {} #차량 번호, 입차 시간 일시적으로 저장
    answer = []
    
    for r in records:
        if r.split()[1] not in car:
            car[r.split()[1]] = 0
            car_in[r.split()[1]] = ''
    
    n = len(car)
    
    for r in records:
        if r.split()[2] == "IN":
            car_in[r.split()[1]] = r.split()[0]
        else:
            tin = datetime.strptime(car_in[r.split()[1]],"%H:%M")
            tout = datetime.strptime(r.split()[0], "%H:%M")
            car[r.split()[1]] += (tout - tin).seconds//60
            
            car_in[r.split()[1]] = '' #입차 시간 초기화
    
    for key in car_in:
        if car_in[key] != '':
            #나간 시간이 나오지 않으면
            tin = datetime.strptime(car_in[key],"%H:%M")
            tout = datetime.strptime("23:59", "%H:%M")
            car[key] += (tout - tin).seconds//60
            
            car_in[key] = '' #입차 시간 초기화
    
    
    car = sorted(car.items(), key = lambda x:x[0])
    
    for c, time in car:
        count = 0
        if time < fees[0]:
            answer.append(fees[1])
        else:
            q,r = divmod(time-fees[0], fees[2])
            if r != 0:
                q += 1
            
            count = fees[1] + q*fees[3]
            answer.append(count)
    
    
        
    return answer
