from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Official CSVTU URLs
RESULT_URL = "https://csvtu.digivarsity.online/WebApp/Result/SemesterResult.aspx"
ADMIT_URL = "https://csvtu.digivarsity.online/WebApp/Examination/AdmitCard.aspx"


def build_result_url(semester, session, roll, exam_type):
    type_map = {
        "regular": "Regular",
        "rtrv": "RTRV",
        "backlog": "Backlog"
    }
    t_value = type_map.get(exam_type, "Regular")

    return (
        f"{RESULT_URL}"
        f"?S={semester}"
        f"&E={session}"
        f"&R={roll}"
        f"&T={t_value}"
    )


def build_admit_url(semester, session, roll):
    return (
        f"{ADMIT_URL}"
        f"?RollNo={roll}"
        f"&ExamSession={session}"
        f"&Semester={semester}"
    )


@app.route("/", methods=["GET", "POST"])
def home():
    error = ""

    if request.method == "POST":
        roll = request.form.get("roll", "").strip()
        semester = request.form.get("semester")
        exam_session = request.form.get("exam_session")
        action = request.form.get("action")
        exam_type = request.form.get("exam_type")

        # 🔐 Basic roll validation
        if not roll.isdigit() or len(roll) != 12:
            error = "Invalid roll number format"
            return render_template("index.html", error=error)

        if action == "admit":
            return redirect(build_admit_url(semester, exam_session, roll))

        return redirect(build_result_url(semester, exam_session, roll, exam_type))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
