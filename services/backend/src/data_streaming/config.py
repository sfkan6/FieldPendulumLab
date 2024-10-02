from .services.cv2_detection import CV2Camera, CV2HSVThresher


hsv_range_of_center = [
    [[40, 40, 40], [90, 255, 255]],
]

hsv_ranges_of_point = [
    [[0, 150, 150], [10, 255, 255]],
    [[175, 0, 150], [180, 255, 255]],
]

center_point_thresher = CV2HSVThresher(hsv_range_of_center)
corner_point_thresher = CV2HSVThresher(hsv_ranges_of_point)

# camera = CV2Camera(debug=True)
camera = CV2Camera(debug=False)

