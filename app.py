# from flask import Flask, render_template, request
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# app = Flask(__name__)

# # Email sending function
# def send_email(subject, body, to_email):
#     from_email = "enockluhimbo@gmail.com"  # Replace with your email
#     from_password = "pbbp anhf pjyo zser"  # Replace with your email password
    
#     # Set up the server (e.g., Gmail SMTP server)
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(from_email, from_password)
    
#     # Create the email message
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))
    
#     # Send email
#     server.sendmail(from_email, to_email, msg.as_string())
#     server.quit()

# @app.route("/", methods=["GET", "POST"])
# def contact():
#     success_message = None  # Variable to store success message
#     if request.method == "POST":
#         # Get the form data
#         name = request.form["name"]
#         email = request.form["email"]
#         message = request.form["message"]
        
#         # Prepare email content
#         subject = f"Message from {name} ({email})"
#         body = f"Message:\n\n{message}\n\nFrom: {email}"

#         # Send email
#         send_email(subject, body, "enockluhimbo@gmail.com")  # Replace with your email
        
#         success_message = "Email sent successfully!"  # Set the success message
        
#     return render_template("index.html", success_message=success_message)

# if __name__ == "__main__":
#     app.run(debug=True)
