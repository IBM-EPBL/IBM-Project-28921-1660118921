
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "!Alert Mail On Product Shortage! - Regards' "
sender = {"name":"IMSR","email":"arunkumarc0610@gmail.com"}
to = [{"email":"carunkumar19cs@srishakthi.ac.in","name":""}]

def alert(main_msg):
    try:
        html_content = "<html><body><h1>"+main_msg+"</h1></body></html>"
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
        print("Mail sent successfully!")
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)