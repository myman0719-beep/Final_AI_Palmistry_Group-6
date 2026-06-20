# palm_logic.py

def get_palm_type(features):

    life = features["life_length"]
    head = features["head_length"]
    heart = features["heart_length"]

    avg = (life + head + heart) / 3

    life_long = int(life > avg)
    head_long = int(head > avg)
    heart_long = int(heart > avg)

    code = f"{life_long}{head_long}{heart_long}"

    mapping = {
        "111": "Sinh-Tri-Tam dai",
        "110": "Sinh-Tri dai, Tam ngan",
        "101": "Sinh-Tam dai, Tri ngan",
        "011": "Tri-Tam dai, Sinh ngan",
        "100": "Sinh dai, Tri-Tam ngan",
        "010": "Tri dai, Sinh-Tam ngan",
        "001": "Tam dai, Sinh-Tri ngan",
        "000": "Ca 3 duong ngan"
    }

    return mapping.get(code, "Khong xac dinh")


def generate_palm_analysis(features, scores):

    analysis = []

    life = features["life_length"]
    head = features["head_length"]
    heart = features["heart_length"]

    life_curv = features["life_curvature"]

    palm_type = get_palm_type(features)

    # =================================
    # TRI DAO
    # =================================

    if head > life * 1.15:

        analysis.append(
            "Duong tri dao noi bat cho thay ban co xu huong suy nghi sau va phan tich ky truoc khi hanh dong."
        )

    elif head < life * 0.85:

        analysis.append(
            "Ban thuong dua ra quyet dinh nhanh va tin vao kinh nghiem thuc te."
        )

    else:

        analysis.append(
            "Ban co su can bang tuong doi giua ly tri va hanh dong."
        )

    # =================================
    # TAM DAO
    # =================================

    if heart > head:

        analysis.append(
            "Cam xuc dong vai tro quan trong trong cac moi quan he va quyet dinh ca nhan."
        )

    elif heart < head * 0.8:

        analysis.append(
            "Ban co xu huong giu ly tri cao hon cam xuc."
        )

    else:

        analysis.append(
            "Ban co kha nang can bang giua cam xuc va ly tri."
        )

    # =================================
    # SINH DAO
    # =================================

    if life > head and life > heart:

        analysis.append(
            "Duong sinh dao noi bat cho thay tinh kien tri va kha nang theo duoi muc tieu lau dai."
        )

    # =================================
    # DO CONG
    # =================================

    if life_curv > 2:

        analysis.append(
            "Ban de thich nghi voi moi truong moi va linh hoat trong cach xu ly van de."
        )

    else:

        analysis.append(
            "Ban co xu huong on dinh va thich nhung ke hoach ro rang."
        )

    # =================================
    # AI TRAITS
    # =================================

    if scores["logic"] > 60:

        analysis.append(
            "Kha nang tu duy logic duoc danh gia kha cao."
        )

    if scores["creativity"] > 60:

        analysis.append(
            "Ban co tu duy sang tao va thuong tim cach tiep can moi."
        )

    if scores["social"] > 60:

        analysis.append(
            "Ban de dang giao tiep va xay dung cac moi quan he."
        )

    if scores["confidence"] > 60:

        analysis.append(
            "Ban co muc do tu tin kha tot trong cong viec va cuoc song."
        )

    return {
        "palm_type": palm_type,
        "analysis": analysis
    }