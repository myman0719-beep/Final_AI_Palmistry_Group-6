def suggest_career(scores):

    careers = []

    logic = scores["logic"]
    emotion = scores["emotion"]
    leadership = scores["leadership"]
    creativity = scores["creativity"]
    confidence = scores["confidence"]
    social = scores["social"]
    determination = scores["determination"]
    independence = scores["independence"]

    # =====================
    # KỸ THUẬT
    # =====================

    if logic >= 60:

        careers.extend([
            "Software Developer",
            "Data Analyst",
            "AI Engineer",
            "System Engineer"
        ])

    # =====================
    # SÁNG TẠO
    # =====================

    if creativity >= 60:

        careers.extend([
            "Graphic Designer",
            "UI/UX Designer",
            "Content Creator",
            "Marketing Creative"
        ])

    # =====================
    # GIAO TIẾP
    # =====================

    if social >= 60:

        careers.extend([
            "Sales Executive",
            "Customer Success",
            "HR Specialist",
            "Public Relations"
        ])

    # =====================
    # LÃNH ĐẠO
    # =====================

    if leadership >= 60:

        careers.extend([
            "Project Manager",
            "Team Leader",
            "Business Manager"
        ])

    # =====================
    # CẢM XÚC
    # =====================

    if emotion >= 60:

        careers.extend([
            "Teacher",
            "Psychology Assistant",
            "Counselor",
            "Social Worker"
        ])

    # =====================
    # ĐỘC LẬP
    # =====================

    if independence >= 60:

        careers.extend([
            "Freelancer",
            "Consultant",
            "Researcher"
        ])

    # =====================
    # KHÔNG CÓ ĐIỂM NỔI BẬT
    # =====================

    if len(careers) == 0:

        careers = [

            "Office Staff",
            "Administrative Assistant",
            "Technician",
            "Accountant",
            "Customer Support"
        ]

    # loại bỏ trùng lặp

    careers = list(dict.fromkeys(careers))

    return careers[:5]