import cv2

def start_capture(rx, ry):
    vc = cv2.VideoCapture(0)
    vc.set(3, rx)
    vc.set(4, ry)
    vc.set(38, 1)

    return vc

def stop_capture(vc_handle):
    vc_handle.release()


fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

def get_frames(vc_handle):
    is_capturing, frame = vc_handle.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    return (frame, fgmask)

def write_frames(frame, mask, path):
    cv2.imwrite(path + 'frame.png', frame)
    cv2.imwrite(path + 'mask.png', mask)
