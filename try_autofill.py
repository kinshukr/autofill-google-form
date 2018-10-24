import requests
url="https://docs.google.com/forms/d/e/1FAIpQLSfUyj1HauCuAEKqG7zSP8Xid6TgVT6fNBAevlyRyf3rc7RZZQ/formResponse"
a='the first entry';
c='the second entry '
b=1;
user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSfUyj1HauCuAEKqG7zSP8Xid6TgVT6fNBAevlyRyf3rc7RZZQ/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
while (1!=0):
	form_data={'entry.1514287646':a, 'entry.340210684':c+str(b)}
	r = requests.post(url, data=form_data, headers=user_agent)
	b=b+1
