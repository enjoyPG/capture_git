from PIL import ImageGrab
import time
import keyboard

def takeshot():
    print('takeshot')
    for i in range(120):
        now = time.localtime()
        ntime = "%04d-%02d-%02d-%02dh-%02dm-%02ds--%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour,now.tm_min, now.tm_sec, i)
        print(ntime)
        #color
        img = ImageGrab.grab((0, 0, 800, 550))
        fname = "{}{}".format(ntime, '.png')
        img.save('./img/lie/' + fname)
        #grayscale
        imgG = img.convert('L')
        fname = "{}{}".format(ntime, '.png')
        imgG.save('./img/lieG/' + fname)
        time.sleep(0.5)
# img.show()

print("F12키를 누르면 50초간 0.5초마다 스샷을찍어줌")
print("저장폴더는 img/lie 폴더, img/lieG 폴더")


while 1:
    if(keyboard.is_pressed('F12')):
        takeshot()
        keyboard.release('F12')
    time.sleep(0.1)
