import cv2
from matplotlib import pyplot as plt
ref_img = cv2.imread('path_ref.jpg')
ref_img = cv2.resize(ref_img, (400, 300))
ref_edges = cv2.Canny(ref_img, 100, 200)

images = ['path_ref.jpg', 'image_1.jpg',
          'image_2.jpg', 'image_3.jpg', 'image_4.jpg']

percent_list = []



height, width = ref_edges.shape
whites = 0
matches = 0

# percent_list = []

for k in range(5):
    img = cv2.imread(images[k])
    img = cv2.resize(img, (400, 300))
    edges = cv2.Canny(img, 100, 200)

    ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.subplot(121), plt.imshow(ref_img)
    # plt.title('Reference Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(img)
    plt.title('Captured Image'), plt.xticks([]), plt.yticks([])
    # plt.show()

    # plt.subplot(121), plt.imshow(ref_edges, cmap='gray')
    # plt.title('Reference Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(edges, cmap='gray')
    # plt.title('Captured Image'), plt.xticks([]), plt.yticks([])
    # plt.show()

    for i in range(0, height):
        for j in range(0, width):
            if ref_edges[i, j] == 255:
                whites = whites + 1
            if (ref_edges[i, j] == 255) and edges[i, j] == 255:
                matches = matches + 1

    match_percent = (matches/whites)*100
    percent_list.append(match_percent) 
    print("Similarity in image {}: {}%".format(k+1, match_percent))




