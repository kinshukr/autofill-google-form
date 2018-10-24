import requests
url='https://docs.google.com/forms/d/e/1FAIpQLScK06A4yPw1sDuahSzAJ2yKq-B2fchVF7eLz7FxriYfb0dVyQ/formResponse'
a=100;
b=200;
user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLScK06A4yPw1sDuahSzAJ2yKq-B2fchVF7eLz7FxriYfb0dVyQ/viewform','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
while (1!=0):
	form_data={'entry.10551260':a}
	r = requests.post(url, data=form_data, headers=user_agent)
	a=a+10
	b=b+10