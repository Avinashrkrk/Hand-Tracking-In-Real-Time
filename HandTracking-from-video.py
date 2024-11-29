import cv2
import mediapipe as mp
import time

# Function to Initialize video capture and return the video properties
def initialize_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError("Error: Unable to open video file.")
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return cap, fps, (width, height)


# Function to Initialize the video writer for saving output video
def initialize_video_writer(output_path, fps, frame_size):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    return cv2.VideoWriter(output_path, fourcc, fps, frame_size)


# Function to Process each video frame to detect and visualize hand landmarks.
def process_frame(frame, hands, mp_draw, frame_size):
    height, width = frame_size
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * width), int(lm.y * height)

                if id == 0:
                    cv2.circle(frame, (cx, cy), 12, (0, 255, 255), cv2.FILLED)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
    return frame

# Function to Display frames per second on the video frame.
def display_fps(frame, fps):
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

def main():
    video_path = './Input_videos/2.mp4' 
    output_video_path = './output_videos/o2.mp4' 

    cap, fps, frame_size = initialize_video(video_path)
    out = initialize_video_writer(output_video_path, fps, frame_size)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False, 
        max_num_hands=2, 
        min_detection_confidence=0.8, 
        min_tracking_confidence=0.8   
    )
    mp_draw = mp.solutions.drawing_utils

    prev_time = 0

    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("End of video or error reading frame.")
                break

            frame = process_frame(frame, hands, mp_draw, frame_size)

            current_time = time.time()
            fps = 1 / (current_time - prev_time)
            prev_time = current_time

            frame = display_fps(frame, fps)

            cv2.imshow("Hand Detection", frame)

            out.write(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Video playback interrupted by user.")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        hands.close()
        print("Resources released successfully.")

if __name__ == "__main__":
    main()
