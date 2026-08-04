from ultralytics import YOLO
import cv2

# Load the pre-trained YOLOv8 Nano model
model = YOLO("yolov8n.pt")


def detect_objects(image_path):
    """
    Detect objects in an image.
    Returns:
        results -> YOLO detection results
        annotated_image -> Image with bounding boxes
    """

    # Perform prediction
    results = model(image_path)

    # Draw bounding boxes on the image
    annotated_image = results[0].plot()

    return results, annotated_image


# Test the script
if __name__ == "__main__":
    image_path = "sample.jpg"

    results, output = detect_objects(image_path)

    cv2.imshow("YOLOv8 Detection", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()