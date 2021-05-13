KIND_CHOICES = [
    ("manual", "Manual Exam"),
    ("mammogram", "Mammogram"),
    ("ultrasound", "Ultrasound"),
    ("mri", "MRI"),
    ("biopsy", "Lymph Node Biopsy"),
]

PRIORITY_CHOICES = [
    (30, "High"),
    (20, "Medium"),
    (10, "Low"),
]

PRIORITY_CHOICES_REVERSE = {
    "high": 30,
    "medium": 20,
    "low": 10,
}
