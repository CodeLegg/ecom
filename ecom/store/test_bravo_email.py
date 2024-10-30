import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

# Initialize Brevo API with API key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Define test email details
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
    to=[{"email": "michaelraymondlegg@gmail.com", "name": "Test User"}],  # Sending to michaelleggbusiness@gmail.com
    sender={"email": "no-reply@stickerneeks.co.uk", "name": "StickerNeeks"},
    subject="Test Email from Brevo",
    html_content="<html><body><h1>This is a test email from Brevo!</h1></body></html>"
)

try:
    # Send the test email
    api_response = api_instance.send_transac_email(send_smtp_email)
    print(f"Email sent successfully: {api_response}")
except ApiException as e:
    print(f"Exception when calling API: {e}")
