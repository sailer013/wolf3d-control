import argparse
import cv2
import numpy as np


def get_point(event, x, y, flags, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'{x=}, {y=}')

        cv2.circle(img, (x, y), 3, (0, 255, 255), -1)


def get_colour(event, x, y, flags, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        colorsB = img[y, x, 0]
        colorsG = img[y, x, 1]
        colorsR = img[y, x, 2]
        colors = img[y, x]
        hsv_value = np.uint8([[[colorsB, colorsG, colorsR]]])
        hsv = cv2.cvtColor(hsv_value, cv2.COLOR_BGR2HSV)
        print(f"HSV: {hsv}")
        print(f'RGB: {colors}')


def main():
    parser = argparse.ArgumentParser(
        prog='Image debugger',
        description='Program to help debug image/video imput',
    )
    parser.add_argument('file_path')
    parser.add_argument('-p', '--position', action='store_true')
    parser.add_argument('-l', '--lower', dest='lower_limit', nargs=3)
    parser.add_argument('-u', '--upper', dest='upper_limit', nargs=3)
    parser.add_argument('-c', '--colour', action='store_true')
    args = parser.parse_args()

    img = cv2.imread(args.file_path)
    cv2.namedWindow('debug')

    if args.position:
        cv2.setMouseCallback('debug', get_point, param=img)

    if args.lower_limit and args.upper_limit:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([int(nr) for nr in args.lower_limit])
        upper_bound = np.array([int(nr) for nr in args.upper_limit])
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        masked_img = cv2.bitwise_and(img, img, mask=mask)

    if args.colour:
        cv2.setMouseCallback('debug', get_colour, param=img)

    while True:
        if args.lower_limit and args.upper_limit:
            cv2.imshow('debug', img)
            cv2.waitKey(2000)
            cv2.imshow('debug', masked_img)
        else:
            cv2.imshow('debug', img)
        k = cv2.waitKey(2000) & 0xFF == ord('q')
        if k:
            break


if __name__ == '__main__':
    main()
