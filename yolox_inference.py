import cv2
import numpy as np
import torch

import sys
from yolox.data.data_augment import preproc
from yolox.exp import get_exp
from yolox.utils import postprocess, vis

## 画像サイズ関連
# 表示画像
DISPLAY_IMAGE_W = 1920
DISPLAY_IMAGE_H = 1080
# 撮影画像
CAPTURE_IMAGE_W = 1280
CAPTURE_IMAGE_H = 720
# 推論画像
PREDICT_IMAGE_W = 1280
PREDICT_IMAGE_H = 704
# 推論画像から表示画像にリサイズする係数
PREDICT_TO_DISPLAY_IMAGE_RATIO_W = DISPLAY_IMAGE_W / PREDICT_IMAGE_W
PREDICT_TO_DISPLAY_IMAGE_RATIO_H = DISPLAY_IMAGE_H / PREDICT_IMAGE_H
print(f"w:{PREDICT_TO_DISPLAY_IMAGE_RATIO_W}  h:{PREDICT_TO_DISPLAY_IMAGE_RATIO_H}")
# 撮影画像から表示画像にリサイズする係数
# CAPTURE_TO_DISPLAY_IMAGE_RATIO_W = DISPLAY_IMAGE_W / CAPTURE_IMAGE_W
# CAPTURE_TO_DISPLAY_IMAGE_RATIO_H = DISPLAY_IMAGE_H / CAPTURE_IMAGE_H

# カスタムクラス名
CUSTOM_CLASSES = ["damage_panel"]

# YOLOXのモデル設定とロード
exp = get_exp(None, "yolox-s")
exp.num_classes = 1
model = exp.get_model()
model.eval()

# 重みのロード
ckpt = torch.load("./../YOLOX/models/4_0920_1000pic_best.pth", map_location="cuda")
model.load_state_dict(ckpt["model"])

# モデル全体をGPUにロード
model.to("cuda")

# カメラデバイスを"/dev/video4"に指定
cap = cv2.VideoCapture("/dev/video4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAPTURE_IMAGE_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_IMAGE_H)

# 推論ループ
while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できません")
        break

    # 前処理（リサイズ）
    img, _ = preproc(frame, (PREDICT_IMAGE_W, PREDICT_IMAGE_H))
    img = torch.from_numpy(img).unsqueeze(0).float().to("cuda")
    frame = cv2.resize(frame, (DISPLAY_IMAGE_W, DISPLAY_IMAGE_H))  # 表示用の画層サイズにリサイズ

    # 推論
    with torch.no_grad():
        outputs = model(img)
        outputs = postprocess(outputs, exp.num_classes, 0.8, exp.nmsthre, class_agnostic=True)

    # 結果の表示
    if outputs[0] is not None:
        bboxes = outputs[0][:, 0:4]
        bboxes[:, 0] = bboxes[:, 0] * PREDICT_TO_DISPLAY_IMAGE_RATIO_W  # x1座標
        bboxes[:, 1] = bboxes[:, 1] * PREDICT_TO_DISPLAY_IMAGE_RATIO_H  # y1座標
        bboxes[:, 2] = bboxes[:, 2] * PREDICT_TO_DISPLAY_IMAGE_RATIO_W  # x2座標
        bboxes[:, 3] = bboxes[:, 3] * PREDICT_TO_DISPLAY_IMAGE_RATIO_H  # y2座標
        cls = outputs[0][:, 6]
        scores = outputs[0][:, 4] * outputs[0][:, 5]
        vis_res = vis(frame, bboxes, scores, cls, 0.8, CUSTOM_CLASSES)
    else:
        vis_res = frame

    # 結果を表示
    cv2.imshow("YOLOX Detection", vis_res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
