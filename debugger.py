import argparse
import cv2

def get_point(event, x, y, flags, img):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'{x=}, {y=}')

        cv2.circle(img, (x, y), 3, (0, 255, 255), -1)

def main():
    parser = argparse.ArgumentParser(
        prog = 'Image debugger',
        description= 'Program to help debug image/video imput',
    )
    parser.add_argument('file_path')
    args = parser.parse_args()

    img = cv2.imread(args.file_path)
    cv2.namedWindow('debug')

    cv2.setMouseCallback('debug', get_point, param=img)





    while True:
        cv2.imshow('debug', img)
        k = cv2.waitKey(1) & 0xFF == ord('q')
        if k:
            break   

if __name__ == '__main__':
    main()