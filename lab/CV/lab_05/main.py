import dlib
from skimage import io
from scipy.spatial import distance

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

img = io.imread('faces/passport.png')
for k, d in enumerate(detector(img, 1)):
    shape = sp(img, d)
reference = facerec.compute_face_descriptor(img, shape)

for i in range(1, 8):
    try:
        img = io.imread(f'faces/{i}.jpg')
        for k, d in enumerate(detector(img, 1)):
            shape = sp(img, d)
        desc = facerec.compute_face_descriptor(img, shape)

        dist = distance.euclidean(reference, desc)
        print("Test", i, "Euclidean distance is", dist, "meaning these belong to", "the same person" if dist < 0.6 else "different people")
    except FileNotFoundError:
        pass
