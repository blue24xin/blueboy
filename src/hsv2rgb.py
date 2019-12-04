import  cv2
import os,string,math


def image():
    imag=cv2.imread("D:\/303.jpg")
    cv2.imshow("BRG",imag)
    hsv = cv2.cvtColor(imag,cv2.COLOR_BGR2HSV)
    print(hsv[0,0])
    cv2.imshow("HSV",hsv)
    cv2.imwrite("D:\/e.jpg",hsv)
    cv2.waitKey(0)

def hsv2rgb(h, s, v): #h: 0~360, s:0-1 ,v: 0-1
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


def rgb2hsv(r, g, b):
    scal = 1000
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * (g-b)/df ) % 360
    elif mx == g:
        h = (60 * (b-r)/df+ 120) % 360
    elif mx == b:
        h = (60 * (r-g)/df+ 240) % 360

    if mx == 0:
        s = 0
    else:
        s = df*scal/mx

    v = mx*scal/255
    return h, s, v
image()
print (hsv2rgb(344,0.18,0.58))

print (rgb2hsv(35.723205, 37.485, 37.250094))

print (rgb2hsv(147,120,127))