import matplotlib.pyplot as plt
import numpy as np
import cv2

def split_video():
    filename = '' # multicate video

    out1 = cv2.VideoWriter('ex_test_1.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (300,400))
    out2 = cv2.VideoWriter('ex_test_2.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (300,400))
    out3 = cv2.VideoWriter('ex_test_3.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (300,400))
    out4 = cv2.VideoWriter('ex_test_4.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (300,400))

    cap = cv2.VideoCapture(filename)
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    # Read until video is completed
    idx = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        idx += 1
        
        if ret == True:
            frame1 = frame[100:500,60:360,:]
            frame2 = frame[100:500,360:660,:]
            frame3 = frame[100:500,660:960,:]
            frame4 = frame[100:500,960:1260,:]
        
            # Display the resulting frame
            cv2.imshow('Frame',frame)
            
            out1.write(frame1)
            out2.write(frame2)
            out3.write(frame3)
            out4.write(frame4)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else: 
            break

    # When everything done, release the video capture object
    cap.release()
    out1.release()
    out2.release()
    out3.release()
    out4.release()

    # Closes all the frames
    cv2.destroyAllWindows()



def get_video_frames(path):
    cap = cv2.VideoCapture(path)
    if(cap.isOpened() == False):
        print("error: cannot open file")
    
    frames = list()
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frames.append(frame)
        else:
            break
    
    cap.release()
    return frames



def combine_result():
    # combine video
    frames1 = get_video_frames('ex_test_1_result.mp4')
    frames2 = get_video_frames('ex_test_2_result.mp4')
    frames3 = get_video_frames('ex_test_3_result.mp4')
    frames4 = get_video_frames('ex_test_4_result.mp4')

    out = cv2.VideoWriter('ex_test_result.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 30, (1200,400))
    for idx in range(len(frames1)):
        f1, f2, f3, f4 = frames1[idx], frames2[idx], frames3[idx], frames4[idx]
        frame = np.concatenate([f1, f2, f3, f4], axis=1)
        out.write(frame)
    out.release()
