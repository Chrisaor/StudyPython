import time
count = 1
try:
    while True:
        print(f'\r{count}')
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    print('사용자에 의해 프로그램이 중단되었습니다.')
