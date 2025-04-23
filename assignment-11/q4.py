import pandas as pd
def cal_days(schedule):
    schedule['days_til_party']=None
    next_party_in=None
    for idx in reversed(schedule.index):
        if schedule.loc[idx,'John'] and schedule.loc[idx,'Judy']:
            next_party_in=0
        elif next_party_in is not None:
            next_party_in+=1
    schedule.loc[idx,'days_til_party']=next_party_in

    return schedule

data = {
'John': [False, False, True, False, True, False, True,
False, False, False],
'Judy': [False, False, True, False, True, False, True,
True, False, False],
}
index = ['d1','d2','d3','d4','d5','d6','d7','d8','d9','d10']
schedule=pd.DataFrame(data,index=index)
result=cal_days(schedule)
print(result)