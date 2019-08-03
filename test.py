from datetime import datetime
from datetime import timedelta


strdate = '2019-07-31'

objDate = datetime.strptime(strdate, '%Y-%m-%d')
final = objDate + timedelta(days=1)
print(final.date())
