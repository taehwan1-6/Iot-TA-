# 필요한 라이브러리를 불러옵니다.
import RPi.GPIO as GPIO
import time

# 불필요한 warning 제거, GPIO핀의 번호 모드 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#GPIO 18번 핀을 출력으로 설정
GPIO.setup(18, GPIO.OUT)
# PWM 인스턴스 p를 만들고 GPIO 18번을 PW핀으로 설정, 주파수 = 50Hz
p = GPIO.PWM(18, 50)

p.start(0) # PWM 시작, 듀티비 = 0

try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
            
except KeyboardInterrupt:    # 키보드 CTRL+C 눌렀을때 예외발생
    pass                     # 무한반복을 빠져나와 아래의 코드를 실행
p.stop()
GPIO.cleanup()