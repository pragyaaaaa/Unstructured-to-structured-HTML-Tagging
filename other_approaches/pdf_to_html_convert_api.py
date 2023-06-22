# import cloudconvert



# KEY='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjg1MzQyM2NmOWY3MmYwMmQ0ZDRmYzZmMjJjMDUwMjlmNWVhZTM3NzQzMjY0YmY1Y2VmN2MxZTAzMGFjYmRhM2I3ZjBlNTc2YTQ5NTVmNTciLCJpYXQiOjE2NzUxOTE3NjAuMjgxODU0LCJuYmYiOjE2NzUxOTE3NjAuMjgxODU1LCJleHAiOjQ4MzA4NjUzNjAuMjc0NzMxLCJzdWIiOiI1MjU0OTk4NiIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.YwgZ-USAcsudsC1SVh-eVnzSlevszWxq3HqT_RdbpeDFQV3QP2p7hXEjyjyBO_RbyjYDAnAqDuwuzZChrd4hqh-oItN0kpxf0Y2-i_Wmkangm6MIB3bH_p4Sqaf5-KCD9WpRNsdB_3QU_uOHYz4hAl2qa5_kudkHEExrSQaqA_Osdyni5ixEGDUqyO4rtRRzQkBsq2MvBFrh2OJbhU0KjarzucL88aDbOcJj726NIPbNqI6GiudO6xDq6BaMgX3EzTfhd1IKfWC-iHYS69vyH_XYZBbvNtr3GmSm_VBYGRt7igOUj87jSHgfUxIkpXVkPVGaJlWiGVASPZcOuw0Pff-WbgAz_zPEUjkBFjOMhvafxMPyY7g6BweYGEDbTH_MTNJ1oXplxHsvjH-TTvi6CB_eIFJZJNRj8ygtQ-WRc8xOoFYuMoD4G130jNenWd6bytoVHbCH6JofiAFoXbVVI8fuqXirBfuOs3arfuAvxTNBSaN-q7i7witiWdNNudzQIQOsV0egKArJbytG_QyachUKDytUeTUzoKpaeOaUrK5oV5RKhdcGua_tygSsV5wZpv7SKwicBkLXMbUcPaLkzGvejPt1unTPsLtkvJUeVSGN656YK593hD3zFqEUNLoMkX4ZnoisaiKoFxITAfhiQvQ3Gx6XSrU5f_j12r-EUps'
# cloudconvert.configure(api_key=KEY)

# #upload

# job = cloudconvert.Job.create(payload={

#     'tasks': {

#         'upload-my-file': {

#             'operation': 'import/upload'

#         }

#     }

# })


# upload_task_id = job['tasks'][0]['id']

# upload_task = cloudconvert.Task.find(id=upload_task_id)

# res = cloudconvert.Task.upload(file_name=r"C:/Users/ANKUR/Desktop/NlpProject/TestPdf/ .", task=upload_task)

# #convert

# convert_job = cloudconvert.Job.create(payload={

#     'tasks': {

#         'convert-my-file': {

#             'operation': 'convert',

#             'input': job['tasks'][0]['id'],

#             'output_format': 'html',

#             'some_other_option': 'value'

#         }

#     }

# })


# #export link generate

# export_job=cloudconvert.Job.create(payload={

# 'tasks': {

#     'export-my-file': {

#         'operation': 'export/url',

#         'input': convert_job['tasks'][0]['id']

#     }

#  }

# })

# #download

# res = cloudconvert.Task.wait(id=export_job['tasks'][0]['id'])

# file = res.get("result").get("files")[0]

# res = cloudconvert.download(filename="C:/Users/ANKUR/Desktop/NlpProject/Exports/" + file['filename'], url=file['url'])

import cloudconvert
import os


KEY='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYjE5NzliYzU1Nzg4N2Q2ZWZhMjJlNzk0Yjc1YTJiODU0MTA2MWQ0NGQ4NmFjNjk2M2M4Y2M1MDZlZDY2NzI1ZDUyNjBlOGVkZTE4YmRlMDIiLCJpYXQiOjE2NzYxODY5NjYuMDQ2ODUzLCJuYmYiOjE2NzYxODY5NjYuMDQ2ODU1LCJleHAiOjQ4MzE4NjA1NjYuMDM5OTI4LCJzdWIiOiI2MjEwMTg4MCIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.YG0298bb0-s9YEUPGd5V19SThemJ8aRE2mVWBU0a16hc1xBykUAmjS0WuBhNC6j-qy0XC1-GeU3i6Pk2jP7bfi2kV-YTV_izJ7Yc-5d3Ht36WFgsma50TF3mISLNOmUyyMS9i4DHvNSHaoPso-XGo_rpzfsZFUxra5J9iDvWGzeDhG44DVWP-X28r76ylQia9bce0iZN8I3VpaFbOoeJplcZKiw_JeXwDMmF7inh5EQXAReGrQ-xC8wh31El9h0-p7G3172AZHLWvRboAQublX4hKyFIvFA8DlDCzqctmYSGnljWgXJUEVqcFe9xrVd84krRKrJZK0jenfJb-PYPCbGQ9U-_Bal9XtF-13Yzfuy-0TIxo60wDVWBYgVezTV6PnWWMqO68D_Z4DMYFqVePU86bgLTQsQwJucr9CEI88kdjlkSjAaUJaaKQbjQFjFKO2NlFz2V1j8uZsCUPXK9W2-x4ePzvTOrxrTqvskrvznzmfrvFFny9qyB0L8HIp2vz8ivIZFcigXCsRdzwVgVKLNhS84RelqSa6ViXrxSLwm8R_oHqf8hDDwrzFWXjrQPl1EmdG0cYQLgmAcL52GKy1LmMAMb0H7TTXQ1qgSByGC0beTdafD6fSJ823x-TXXHVH1rN4kDGhh757JHZJzeInBtU8q7PZDR-9ITFqbB5oU'
cloudconvert.configure(api_key=KEY)

folder_path = "D:/NlpProject/10-60"

for pdf_file in os.listdir(folder_path):
    if pdf_file.endswith(".pdf"):
        # upload
        job = cloudconvert.Job.create(payload={
            'tasks': {
                'upload-my-file': {
                    'operation': 'import/upload'
                }
            }
        })
        upload_task_id = job['tasks'][0]['id']
        upload_task = cloudconvert.Task.find(id=upload_task_id)
        res = cloudconvert.Task.upload(file_name=os.path.join(folder_path, pdf_file), task=upload_task)

        # convert
        convert_job = cloudconvert.Job.create(payload={
            'tasks': {
                'convert-my-file': {
                    'operation': 'convert',
                    'input': job['tasks'][0]['id'],
                    'output_format': 'html',
                    'some_other_option': 'value'
                }
            }
        })

        # export link generate
        export_job=cloudconvert.Job.create(payload={
            'tasks': {
                'export-my-file': {
                    'operation': 'export/url',
                    'input': convert_job['tasks'][0]['id']
                }
            }
        })

        # download
        res = cloudconvert.Task.wait(id=export_job['tasks'][0]['id'])
        file = res.get("result").get("files")[0]
        html_file_path = os.path.join("D:/NlpProject/Dataset", file['filename'].replace(".pdf", ".html"))
        res = cloudconvert.download(filename=html_file_path, url=file['url'])












# C:\Users\ANKUR\Desktop\NlpProject\Exports
# C:\Users\ANKUR\Desktop\NlpProject\TestPdf\samplepdf2.pdf
# C:/Users/ANKUR/Desktop/converted_html_file.html
# C:/Users/ANKUR/Desktop/TestPdf/samplepdf3.pdf
# eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjg1MzQyM2NmOWY3MmYwMmQ0ZDRmYzZmMjJjMDUwMjlmNWVhZTM3NzQzMjY0YmY1Y2VmN2MxZTAzMGFjYmRhM2I3ZjBlNTc2YTQ5NTVmNTciLCJpYXQiOjE2NzUxOTE3NjAuMjgxODU0LCJuYmYiOjE2NzUxOTE3NjAuMjgxODU1LCJleHAiOjQ4MzA4NjUzNjAuMjc0NzMxLCJzdWIiOiI1MjU0OTk4NiIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.YwgZ-USAcsudsC1SVh-eVnzSlevszWxq3HqT_RdbpeDFQV3QP2p7hXEjyjyBO_RbyjYDAnAqDuwuzZChrd4hqh-oItN0kpxf0Y2-i_Wmkangm6MIB3bH_p4Sqaf5-KCD9WpRNsdB_3QU_uOHYz4hAl2qa5_kudkHEExrSQaqA_Osdyni5ixEGDUqyO4rtRRzQkBsq2MvBFrh2OJbhU0KjarzucL88aDbOcJj726NIPbNqI6GiudO6xDq6BaMgX3EzTfhd1IKfWC-iHYS69vyH_XYZBbvNtr3GmSm_VBYGRt7igOUj87jSHgfUxIkpXVkPVGaJlWiGVASPZcOuw0Pff-WbgAz_zPEUjkBFjOMhvafxMPyY7g6BweYGEDbTH_MTNJ1oXplxHsvjH-TTvi6CB_eIFJZJNRj8ygtQ-WRc8xOoFYuMoD4G130jNenWd6bytoVHbCH6JofiAFoXbVVI8fuqXirBfuOs3arfuAvxTNBSaN-q7i7witiWdNNudzQIQOsV0egKArJbytG_QyachUKDytUeTUzoKpaeOaUrK5oV5RKhdcGua_tygSsV5wZpv7SKwicBkLXMbUcPaLkzGvejPt1unTPsLtkvJUeVSGN656YK593hD3zFqEUNLoMkX4ZnoisaiKoFxITAfhiQvQ3Gx6XSrU5f_j12r-EUps
