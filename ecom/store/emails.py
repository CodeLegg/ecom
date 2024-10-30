import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Brevo API with API key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = os.environ.get("SENDINBLUE_API_KEY")

def send_welcome_email(user_email, user_name):
    # Create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
    # Define professional welcome email content with logo and styling
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": user_email, "name": user_name}],
        sender={"email": "no-reply@stickerneeks.co.uk", "name": "StickerNeeks"},
        subject="Welcome to StickerNeeks!",
        html_content="""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
                    
                    <div style="text-align: center;">
                        <img src="https://www.stickerneeks.co.uk/logo.png" alt="StickerNeeks Logo" style="width: 150px; margin-bottom: 20px;">
                    </div>
                    
                    <h1 style="color: #4CAF50; text-align: center;">Welcome, {}</h1>
                    
                    <p style="font-size: 16px; line-height: 1.6;">
                        Thank you for joining StickerNeeks! We're thrilled to have you with us. Our community of creators and enthusiasts is growing, and we’re excited to have you on board.
                    </p>
                    
                    <p style="font-size: 16px; line-height: 1.6;">
                        At StickerNeeks, we’re committed to providing you with the best stickers and accessories. Explore our latest collections, or reach out to us if you have any questions!
                    </p>
                    
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="https://www.stickerneeks.co.uk" style="background-color: #4CAF50; color: #ffffff; text-decoration: none; padding: 10px 20px; font-size: 16px; border-radius: 5px;">
                            Subscribe Now
                        </a>
                    </div>

                    <p style="font-size: 14px; text-align: center; color: #777;">
                        Follow us on social media for the latest updates and special offers!
                    </p>
                    
                    <div style="text-align: center; margin-top: 20px;">
                        <a href="https://www.facebook.com/profile.php?viewas=100000686899395&id=61566480197200" style="margin-right: 20px; text-decoration: none; color: #333;">
                            <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook" style="width: 24px; height: 24px; vertical-align: middle;">
                            <span style="font-size: 16px; vertical-align: middle;">Facebook</span>
                        </a>
                        <a href="https://www.instagram.com/stickerneeks" style="margin-right: 20px; text-decoration: none; color: #333;">
                            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" style="width: 24px; height: 24px; vertical-align: middle;">
                            <span style="font-size: 16px; vertical-align: middle;">Instagram</span>
                        </a>
                        <a href="https://www.twitter.com/stickerneeks" style="text-decoration: none; color: #333;">
                            <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" style="width: 24px; height: 24px; vertical-align: middle;">
                            <span style="font-size: 16px; vertical-align: middle;">Twitter</span>
                        </a>
                    </div>
                    
                    <p style="font-size: 12px; text-align: center; color: #aaa; margin-top: 30px;">
                        © 2024 StickerNeeks. All rights reserved.<br>
                        123 Sticker Street, Stickerville, SK 12345
                    </p>
                
                </div>
            </body>
        </html>
        """.format(user_name)
    )
    
    try:
        # Send the welcome email
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(f"Welcome email sent successfully: {api_response}")
    except ApiException as e:
        print(f"Exception when calling API: {e}")
