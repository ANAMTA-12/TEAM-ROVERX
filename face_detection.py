import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import os

class FaceDetector(Node):
    def __init__(self):
        super().__init__('face_detector_node')

        # Publisher for the image
        self.publisher = self.create_publisher(Image, 'face_detected_stream', 10)

        # Bridge between ROS and OpenCV
        self.bridge = CvBridge()

        # Get absolute path to haarcascade file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        cascade_path = os.path.join(current_dir, "haarcascade_frontalface_default.xml")

        # Load the cascade
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        # Start camera
        self.cap = cv2.VideoCapture(0)

        # Timer to process frames
        self.timer = self.create_timer(0.03, self.timer_callback)

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Webcam frame not received")
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scalefactor=1.1, minNeighbours=4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Publish the image
        msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher.publish(msg)

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = FaceDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
