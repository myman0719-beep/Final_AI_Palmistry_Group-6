from ultralytics import YOLO
from report_generator import generate_report
from palm_logic import generate_palm_analysis
from utils import (
    average_y,
    bbox_size,
    count_intersections,
    curvature,
    curve_length,
    line_angle,
    max_curvature,
    palm_height,
    palm_width
)

import joblib
import numpy as np
import pandas as pd


# =====================================
# CONFIG
# =====================================

YOLO_MODEL = r"runs\pose\train-5\weights\best.pt"

# =====================================
# LOAD YOLO
# =====================================

pose_model = YOLO(YOLO_MODEL)

# =====================================
# LOAD FEATURE LIST
# =====================================

feature_columns = joblib.load(
    "feature_columns.pkl"
)

# =====================================
# LOAD MODEL
# =====================================

trait_model = joblib.load(
    "traits_model.pkl"
)

trait_names = [
    "logic",
    "emotion",
    "leadership",
    "creativity",
    "confidence",
    "social",
    "determination",
    "independence"
]
def predict_palm(image_path):

# =====================================
# YOLO DETECT
# =====================================

    results = pose_model(
        image_path,
        verbose=False
    )

    life_points = None
    head_points = None
    heart_points = None

    for r in results:

        classes = r.boxes.cls.cpu().numpy()

        keypoints = (
            r.keypoints.xy
            .cpu()
            .numpy()
        )

        for cls_id, pts in zip(
            classes,
            keypoints
        ):

            pts = [
                tuple(p)
                for p in pts
            ]

            if int(cls_id) == 3:
                life_points = pts

            elif int(cls_id) == 1:
                head_points = pts

            elif int(cls_id) == 2:
                heart_points = pts


    if (
    life_points is None
    or head_points is None
    or heart_points is None
    ):
        return {
        "error": "Không tìm thấy đủ 3 đường chỉ tay"
    }

    # =====================================
    # BASIC FEATURES
    # =====================================

    life_length = curve_length(
        life_points
    )

    head_length = curve_length(
        head_points
    )

    heart_length = curve_length(
        heart_points
    )

    life_curvature = curvature(
        life_points
    )

    head_curvature = curvature(
        head_points
    )

    heart_curvature = curvature(
        heart_points
    )

    life_max_curvature = max_curvature(
        life_points
    )

    head_max_curvature = max_curvature(
        head_points
    )

    heart_max_curvature = max_curvature(
        heart_points
    )

    life_angle = line_angle(
        life_points
    )

    head_angle = line_angle(
        head_points
    )

    heart_angle = line_angle(
        heart_points
    )

    # =====================================
    # BBOX
    # =====================================

    life_bbox_width, life_bbox_height = bbox_size(
        life_points
    )

    head_bbox_width, head_bbox_height = bbox_size(
        head_points
    )

    heart_bbox_width, heart_bbox_height = bbox_size(
        heart_points
    )

    # =====================================
    # RATIOS
    # =====================================

    head_ratio = (
        head_length / life_length
    )

    heart_ratio = (
        heart_length / life_length
    )

    head_heart_ratio = (
        head_length / heart_length
    )

    # =====================================
    # POSITION
    # =====================================

    life_y = average_y(
        life_points
    )

    head_y = average_y(
        head_points
    )

    heart_y = average_y(
        heart_points
    )

    # =====================================
    # GAPS
    # =====================================

    head_heart_gap = abs(
        head_y - heart_y
    )

    life_head_gap = abs(
        life_y - head_y
    )

    life_heart_gap = abs(
        life_y - heart_y
    )

    # =====================================
    # INTERSECTIONS
    # =====================================

    line_intersections = (

        count_intersections(
            life_points,
            head_points
        )

        +

        count_intersections(
            life_points,
            heart_points
        )

        +

        count_intersections(
            head_points,
            heart_points
        )

    )

    # =====================================
    # PALM SIZE
    # =====================================

    pw = palm_width(
        life_points,
        head_points,
        heart_points
    )

    ph = palm_height(
        life_points,
        head_points,
        heart_points
    )

    # =====================================
    # ADVANCED FEATURES
    # =====================================

    total_length = (
        life_length
        + head_length
        + heart_length
    )

    life_length_ratio = (
        life_length / total_length
    )

    head_length_ratio = (
        head_length / total_length
    )

    heart_length_ratio = (
        heart_length / total_length
    )

    life_aspect = (
        life_bbox_width /
        (life_bbox_height + 1e-6)
    )

    head_aspect = (
        head_bbox_width /
        (head_bbox_height + 1e-6)
    )

    heart_aspect = (
        heart_bbox_width /
        (heart_bbox_height + 1e-6)
    )

    life_pos = (
        life_y / ph
    )

    head_pos = (
        head_y / ph
    )

    heart_pos = (
        heart_y / ph
    )

    # =====================================
    # BUILD FEATURE DICT
    # =====================================

    data = {

        "life_length": life_length,
        "head_length": head_length,
        "heart_length": heart_length,

        "life_curvature": life_curvature,
        "head_curvature": head_curvature,
        "heart_curvature": heart_curvature,

        "life_max_curvature": life_max_curvature,
        "head_max_curvature": head_max_curvature,
        "heart_max_curvature": heart_max_curvature,

        "life_angle": life_angle,
        "head_angle": head_angle,
        "heart_angle": heart_angle,

        "life_bbox_width": life_bbox_width,
        "life_bbox_height": life_bbox_height,

        "head_bbox_width": head_bbox_width,
        "head_bbox_height": head_bbox_height,

        "heart_bbox_width": heart_bbox_width,
        "heart_bbox_height": heart_bbox_height,

        "head_ratio": head_ratio,
        "heart_ratio": heart_ratio,
        "head_heart_ratio": head_heart_ratio,

        "life_y": life_y,
        "head_y": head_y,
        "heart_y": heart_y,

        "head_heart_gap": head_heart_gap,
        "life_head_gap": life_head_gap,
        "life_heart_gap": life_heart_gap,

        "line_intersections": line_intersections,

        "palm_width": pw,
        "palm_height": ph,

        "life_length_ratio": life_length_ratio,
        "head_length_ratio": head_length_ratio,
        "heart_length_ratio": heart_length_ratio,

        "life_aspect": life_aspect,
        "head_aspect": head_aspect,
        "heart_aspect": heart_aspect,

        "life_pos": life_pos,
        "head_pos": head_pos,
        "heart_pos": heart_pos
    }

    # =====================================
    # CREATE DATAFRAME
    # =====================================

    # =====================================
    # PREDICT
    # =====================================

    X = pd.DataFrame([data])

    # đảm bảo đúng thứ tự feature
    X = X.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = trait_model.predict(X)[0]

    scores = {}

    for trait, value in zip(
        trait_names,
        prediction
    ):

        value = float(value)

        value = max(
            0,
            min(100, value)
        )

        scores[trait] = value

    analysis_data = generate_palm_analysis(
    data,
    scores
)


    # =====================================
    # REPORT
    # =====================================

    report = generate_report(scores)


    # =====================================
    # RAW SCORES
    # =====================================

    # analysis_data may contain detailed analysis and palm type
    palm_type = None
    if isinstance(analysis_data, dict):
        palm_type = analysis_data.get("palm_type")

    return {
    "scores": scores,
    "palm_type": palm_type,
    "analysis": analysis_data,

    "personality": report["personality"],
    "summary": report["summary"],
    "overview": report["overview"],
    "career_fields": report["career_fields"],
    "careers": report["careers"]
}

if __name__ == "__main__":

    result = predict_palm(
        r"test_images\16.jpg"
    )

    print(result)
