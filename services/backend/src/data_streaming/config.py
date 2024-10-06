from cv2_detection import Camera, HSVThresher


hsv_range_of_center = [
    [[40, 40, 40], [90, 255, 255]],
]

hsv_ranges_of_point = [
    [[0, 150, 150], [10, 255, 255]],
    [[175, 0, 150], [180, 255, 255]],
]

center_point_thresher = HSVThresher(hsv_range_of_center)
corner_point_thresher = HSVThresher(hsv_ranges_of_point)

# camera = Camera(debug=True)
camera = Camera(debug=False)

