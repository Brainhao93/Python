from datetime import datetime
date= datetime.now()
print('today is: '+str(date))

brithday =input('when is you borthadyu dd/mm/yyyy')
birthdaydate=datetime.strptime(brithday,'%d/%m/%Y')
print('brithday is' + str(birthdaydate))
