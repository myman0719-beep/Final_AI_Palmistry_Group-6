def analyze_personality(scores):

    result = []

    logic = scores["logic"]
    emotion = scores["emotion"]
    leadership = scores["leadership"]
    creativity = scores["creativity"]
    confidence = scores["confidence"]
    social = scores["social"]
    determination = scores["determination"]
    independence = scores["independence"]

    # =====================
    # LY TRI / CAM XUC
    # =====================

    if emotion > logic + 15:

        result.append(
            "Bạn có xu hướng đưa ra quyết định dựa trên trực giác và cảm nhận cá nhân nhiều hơn các phân tích logic."
        )

    elif logic > emotion + 15:

        result.append(
            "Bạn thường phân tích kỹ vấn đề trước khi đưa ra quyết định và ít bị cảm xúc chi phối."
        )

    else:

        result.append(
            "Bạn có xu hướng cân bằng giữa cảm xúc và tư duy phân tích."
        )

    # =====================
    # XA HOI
    # =====================

    if social < 40:

        result.append(
            "Bạn thích môi trường yên tĩnh và thường cảm thấy thoải mái hơn khi làm việc độc lập hoặc trong nhóm nhỏ."
        )

    elif social > 60:

        result.append(
            "Bạn dễ dàng hòa nhập với tập thể và thường chủ động trong giao tiếp."
        )

    # =====================
    # LANH DAO
    # =====================

    if leadership < 40:

        result.append(
            "Bạn thường thích vai trò hỗ trợ, phối hợp hơn là trở thành người dẫn dắt tập thể."
        )

    elif leadership > 60:

        result.append(
            "Bạn có xu hướng chủ động dẫn dắt và tổ chức công việc cho người khác."
        )

    # =====================
    # SANG TAO
    # =====================

    if creativity > 60:

        result.append(
            "Bạn có khả năng nhìn nhận vấn đề từ nhiều góc độ và thường đưa ra những ý tưởng mới."
        )

    elif creativity >= 40:

        result.append(
            "Bạn có tư duy linh hoạt nhưng vẫn ưu tiên những giải pháp thực tế và khả thi."
        )

    # =====================
    # TU TIN
    # =====================

    if confidence < 40:

        result.append(
            "Bạn thường cân nhắc khá kỹ trước khi hành động và hiếm khi đưa ra quyết định vội vàng."
        )

    elif confidence > 60:

        result.append(
            "Bạn khá tự tin vào năng lực của bản thân và sẵn sàng thử sức với những thử thách mới."
        )

    # =====================
    # KIEN TRI
    # =====================

    if determination > 60:

        result.append(
            "Khi đã xác định mục tiêu, bạn thường kiên trì theo đuổi đến cùng."
        )

    elif determination < 40:

        result.append(
            "Bạn có xu hướng điều chỉnh kế hoạch linh hoạt khi gặp trở ngại thay vì cố chấp theo đuổi một hướng duy nhất."
        )

    return result