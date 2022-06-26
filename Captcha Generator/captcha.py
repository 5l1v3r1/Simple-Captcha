import string, random


def main():
    captcha = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4 #длина капчи
    ))
    captchaverify = input(f'Captcha: {captcha}\nEnter captcha: ')
    if captchaverify != captcha:
        print('Invalid Captcha')
    else: print('Success')

if __name__=='__main__':
    main()
    input()