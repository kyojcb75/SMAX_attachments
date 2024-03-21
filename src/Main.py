import json

from attachments import down_atta, save_attachments
from authenticator import get_token
from case import get_all_request_cases


def attachments_organizer():
    token = get_token()
    cases_info = get_all_request_cases()

    for case in cases_info:
        info_attachment_json = json.loads(case['json_attachments'])
        case_id = case['request_id']
        folder_path = 'C:/attachmentsSmax/' + str(case_id)
        for propiedad in info_attachment_json['complexTypeProperties']:
            pr_id = propiedad['properties']['id']
            pr_file_name = propiedad['properties']['file_name']
            pr_file_exten = propiedad['properties']['file_extension']
            file_data = down_atta(pr_id, token)
            save_attachments(folder_path, pr_file_name + "." + pr_file_exten, file_data)


attachments_organizer()
