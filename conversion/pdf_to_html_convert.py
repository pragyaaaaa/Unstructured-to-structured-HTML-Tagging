import cloudconvert



KEY='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjg1MzQyM2NmOWY3MmYwMmQ0ZDRmYzZmMjJjMDUwMjlmNWVhZTM3NzQzMjY0YmY1Y2VmN2MxZTAzMGFjYmRhM2I3ZjBlNTc2YTQ5NTVmNTciLCJpYXQiOjE2NzUxOTE3NjAuMjgxODU0LCJuYmYiOjE2NzUxOTE3NjAuMjgxODU1LCJleHAiOjQ4MzA4NjUzNjAuMjc0NzMxLCJzdWIiOiI1MjU0OTk4NiIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.YwgZ-USAcsudsC1SVh-eVnzSlevszWxq3HqT_RdbpeDFQV3QP2p7hXEjyjyBO_RbyjYDAnAqDuwuzZChrd4hqh-oItN0kpxf0Y2-i_Wmkangm6MIB3bH_p4Sqaf5-KCD9WpRNsdB_3QU_uOHYz4hAl2qa5_kudkHEExrSQaqA_Osdyni5ixEGDUqyO4rtRRzQkBsq2MvBFrh2OJbhU0KjarzucL88aDbOcJj726NIPbNqI6GiudO6xDq6BaMgX3EzTfhd1IKfWC-iHYS69vyH_XYZBbvNtr3GmSm_VBYGRt7igOUj87jSHgfUxIkpXVkPVGaJlWiGVASPZcOuw0Pff-WbgAz_zPEUjkBFjOMhvafxMPyY7g6BweYGEDbTH_MTNJ1oXplxHsvjH-TTvi6CB_eIFJZJNRj8ygtQ-WRc8xOoFYuMoD4G130jNenWd6bytoVHbCH6JofiAFoXbVVI8fuqXirBfuOs3arfuAvxTNBSaN-q7i7witiWdNNudzQIQOsV0egKArJbytG_QyachUKDytUeTUzoKpaeOaUrK5oV5RKhdcGua_tygSsV5wZpv7SKwicBkLXMbUcPaLkzGvejPt1unTPsLtkvJUeVSGN656YK593hD3zFqEUNLoMkX4ZnoisaiKoFxITAfhiQvQ3Gx6XSrU5f_j12r-EUps'
cloudconvert.configure(api_key=KEY)

#upload

job = cloudconvert.Job.create(payload={

    'tasks': {

        'upload-my-file': {

            'operation': 'import/upload'

        }

    }

})


upload_task_id = job['tasks'][0]['id']

upload_task = cloudconvert.Task.find(id=upload_task_id)

res = cloudconvert.Task.upload(file_name=r"TestPdf\samplepdf17.pdf", task=upload_task)

#convert

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


#export link generate

export_job=cloudconvert.Job.create(payload={

'tasks': {

    'export-my-file': {

        'operation': 'export/url',

        'input': convert_job['tasks'][0]['id']

    }

 }

})

#download

res = cloudconvert.Task.wait(id=export_job['tasks'][0]['id'])

file = res.get("result").get("files")[0]

res = cloudconvert.download(filename="D:\Simplitiv\Exports" + file['filename'], url=file['url'])













# C:\Users\ANKUR\Desktop\NlpProject\Exports
# C:\Users\ANKUR\Desktop\NlpProject\TestPdf\samplepdf2.pdf
# C:/Users/ANKUR/Desktop/converted_html_file.html
# C:/Users/ANKUR/Desktop/TestPdf/samplepdf3.pdf
# eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMjg1MzQyM2NmOWY3MmYwMmQ0ZDRmYzZmMjJjMDUwMjlmNWVhZTM3NzQzMjY0YmY1Y2VmN2MxZTAzMGFjYmRhM2I3ZjBlNTc2YTQ5NTVmNTciLCJpYXQiOjE2NzUxOTE3NjAuMjgxODU0LCJuYmYiOjE2NzUxOTE3NjAuMjgxODU1LCJleHAiOjQ4MzA4NjUzNjAuMjc0NzMxLCJzdWIiOiI1MjU0OTk4NiIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.YwgZ-USAcsudsC1SVh-eVnzSlevszWxq3HqT_RdbpeDFQV3QP2p7hXEjyjyBO_RbyjYDAnAqDuwuzZChrd4hqh-oItN0kpxf0Y2-i_Wmkangm6MIB3bH_p4Sqaf5-KCD9WpRNsdB_3QU_uOHYz4hAl2qa5_kudkHEExrSQaqA_Osdyni5ixEGDUqyO4rtRRzQkBsq2MvBFrh2OJbhU0KjarzucL88aDbOcJj726NIPbNqI6GiudO6xDq6BaMgX3EzTfhd1IKfWC-iHYS69vyH_XYZBbvNtr3GmSm_VBYGRt7igOUj87jSHgfUxIkpXVkPVGaJlWiGVASPZcOuw0Pff-WbgAz_zPEUjkBFjOMhvafxMPyY7g6BweYGEDbTH_MTNJ1oXplxHsvjH-TTvi6CB_eIFJZJNRj8ygtQ-WRc8xOoFYuMoD4G130jNenWd6bytoVHbCH6JofiAFoXbVVI8fuqXirBfuOs3arfuAvxTNBSaN-q7i7witiWdNNudzQIQOsV0egKArJbytG_QyachUKDytUeTUzoKpaeOaUrK5oV5RKhdcGua_tygSsV5wZpv7SKwicBkLXMbUcPaLkzGvejPt1unTPsLtkvJUeVSGN656YK593hD3zFqEUNLoMkX4ZnoisaiKoFxITAfhiQvQ3Gx6XSrU5f_j12r-EUps
