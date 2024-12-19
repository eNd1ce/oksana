# models/face_recognition.py
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image

class FaceRecognizer:
    def __init__(self):
        self.mtcnn = MTCNN()
        self.resnet = InceptionResnetV1(pretrained='vggface2').eval()
        self.known_faces = {}

    def register_face(self, name, image_path):
        img = Image.open(image_path)
        face = self.mtcnn(img)
        if face is not None:
            embedding = self.resnet(face.unsqueeze(0))
            self.known_faces[name] = embedding
            return True
        return False

    def recognize_face(self, image_path):
        img = Image.open(image_path)
        face = self.mtcnn(img)
        if face is not None:
            embedding = self.resnet(face.unsqueeze(0))
            min_dist = float('inf')
            identity = None
            for name, known_embedding in self.known_faces.items():
                dist = (embedding - known_embedding).norm().item()
                if dist < min_dist:
                    min_dist = dist
                    identity = name
            if min_dist < 1.0:
                return identity
        return None
