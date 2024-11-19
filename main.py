import cv2
import os

def crop_face(img_path, output_path):
    """
    얼굴을 중앙으로 1024x1024 크기로 자르는 함수

    Args:
        img_path (str): 입력 이미지 파일 경로
        output_path (str): 출력 이미지 파일 경로
    """

    # 캐스케이드 파일 로드 (얼굴 검출 모델)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    # 이미지 읽기
    img = cv2.imread(img_path)

    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 검출된 얼굴이 없으면 함수 종료
    if len(faces) == 0:
        print("얼굴이 검출되지 않았습니다.")
        return

    # 첫 번째 검출된 얼굴 기준으로 크롭 (여러 얼굴이 검출될 경우 수정 필요)
    (x, y, w, h) = faces[0]

    # 얼굴 중심 좌표 계산
    center_x = x + w // 2
    center_y = y + h // 2

    # 크롭할 영역 설정 (1024x1024 크기, 이미지 경계 고려)
    crop_x = max(center_x - 512, 0)
    crop_y = max(center_y - 512, 0)
    crop_w = min(1024, img.shape[1] - crop_x)
    crop_h = min(1024, img.shape[0] - crop_y)

    # 얼굴 영역 크롭
    cropped_face = img[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]

    # 이미지 저장
    cv2.imwrite(output_path, cropped_face)
    print("이미지가 성공적으로 저장되었습니다.")


img_path = "./img/hair.png"
output_path = "./haircolor/Style-Your-Hair/ffhq_image/hair.png"
crop_face(img_path, output_path)

img_path = "./img/face.png"
output_path = "./haircolor/Style-Your-Hair/ffhq_image/face.png"
crop_face(img_path, output_path)

os.system("python os.py")
