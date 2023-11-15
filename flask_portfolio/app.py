from flask import Flask, render_template, send_file
import io


app = Flask(__name__)


@app.route("/downloadResume", methods=["GET"])
def download_resume():
    # Define the path to your resume file
    path_to_resume = "static/nolanCareyResume.pdf"

    # Define the correct MIME type for pdf
    resume_mimetype = "application/pdf"

    # Send the file to the user
    return send_file(
        path_to_resume,
        mimetype=resume_mimetype,
        as_attachment=True,  # User will be prompted to download the file
        download_name="Nolan_Carey_Resume.pdf",  # The name of the file as it will be downloaded
    )


@app.route("/")
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
