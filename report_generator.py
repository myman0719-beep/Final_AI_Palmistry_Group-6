from analysis_engine import analyze_personality
from career_engine import suggest_career
from summary_engine import create_summary

def generate_report(scores):


    analysis = analyze_personality(scores)

    summary = create_summary(scores)

    overview = []

    # Logic
    if scores["logic"] >= 60:
        overview.append(
            "Bạn có xu hướng suy nghĩ logic và phân tích tốt."
        )
    else:
        overview.append(
            "Bạn thường đưa ra quyết định dựa trên cảm nhận cá nhân."
        )

    # Emotion
    if scores["emotion"] >= 60:
        overview.append(
            "Bạn là người giàu cảm xúc và dễ đồng cảm."
        )
    else:
        overview.append(
            "Bạn có khả năng kiểm soát cảm xúc khá tốt."
        )

    # Social
    if scores["social"] >= 60:
        overview.append(
            "Bạn thích giao tiếp và mở rộng các mối quan hệ."
        )
    else:
        overview.append(
            "Bạn có xu hướng hướng nội và thích không gian riêng."
        )

    # Creativity
    if scores["creativity"] >= 60:
        overview.append(
            "Bạn có khả năng sáng tạo nổi bật."
        )
    else:
        overview.append(
            "Bạn thiên về tư duy thực tế."
        )

    # ==========================
    # CAREER FIELDS
    # ==========================

    career_fields = []

    if (
        scores["logic"] > 60
        and
        scores["creativity"] > 60
    ):

        career_fields.append(
            "Công nghệ thông tin, AI, kỹ thuật, nghiên cứu."
        )

    elif (
        scores["social"] > 60
        and
        scores["leadership"] > 60
    ):

        career_fields.append(
            "Kinh doanh, quản lý, marketing, nhân sự."
        )

    elif scores["emotion"] > 60:

        career_fields.append(
            "Giáo dục, tâm lý học, công tác xã hội."
        )

    else:

        career_fields.append(
            "Các lĩnh vực yêu cầu tính ổn định và chuyên môn sâu."
        )

    careers = suggest_career(scores)

    return {

        "personality": analysis,

        "summary": summary,

        "overview": overview,

        "career_fields": career_fields,

        "careers": careers
    }

