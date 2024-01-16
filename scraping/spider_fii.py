import requests

def colect_fund(name):
    url = "https://statusinvest.com.br/fii/tickerprice"
    payload = f"ticker={name}&type=1&currences%5B%5D=1"
    headers = {
        "cookie": "suno_checkout_userid=9f9f01fa-caba-49d5-ba79-5836c7070368; _adasys=ed077ce2-9cff-4f67-955b-eb85114e71ca; _ga=GA1.1.1376835253.1691862092; _fbp=fb.2.1691862092810.2047580892; G_ENABLED_IDPS=google; pg_mm2_cookie_a=878a9b3f-77d4-4278-9184-66d14d41429f; hubspotutk=736daadd9b95a6cdc3111c3720e8d033; messagesUtk=0a3cbd7c01e74b1fa1cb99b9dcb0df90; _fs=16454808308-15173641745; AdoptVisitorId=OwMwxsBGCmCMBsBaYBDeSAsIME5EA5YBmYRABnkiIBMAmFWyeMSIA===; _hjSessionUser_1931042=eyJpZCI6IjAxZDcxNzQzLWM2ZDgtNTMwYS1iOTUxLTdmN2E0MjVhMGY4NSIsImNyZWF0ZWQiOjE2OTY1OTUxNTcxODAsImV4aXN0aW5nIjp0cnVlfQ==; AdoptConsent=N4Ig7gpgRgzglgFwgSQCIgFwgBwQOwCMAzAMYCcZAtBAGYAMBlALOY1DQY/SXdgQGx4AhjSgAmEABoQAewAOCZADsAKkIDmMTAG0QACwCuRIgYBSAGQBi5gLJSQTAMoBFPQHlzJAPoBRbPb0vBHUoAC0ANRIAWwBhEABdaXkENwMENU0dEAAPK0cALwQAaQANS0t7MgAhHwgACQBVLzh1AE17ACUAOTofIkcyeCh7NxS8WmxzAhl7fnNsbJ8lKr0ABWd7AHUAVjwYgBMvKAgwADd7GX4o8wBrKsswOrh7bDwaODEbNwArdSUL5x4IjIbYAQXMYEc9gQNiKTCI+wg4SKUOk2T0cG+21aZAQBlB9iUYHMq0sBiYe349mQS34/B8lFOUHC9igjjkACcojcbgAbOpeewQG4EGiUIS8sRRYbSACejga6i6ShgKhulHs2waxg5XRkTA5CHsvKKHJi2RKXgAjt8ivZQjFeRyZDQGvk6G57D5zEUiLyGiVnDZtgkAL5AA===; _hjDonePolls=938105; .StatusInvest=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJBY2NvdW50SWQiOiIzNDIyOTMiLCJOYW1lIjoiSmVmZXJzb24iLCJFbWFpbCI6ImRhbGFybWkuamVmZXJzb25Ab3V0bG9vay5jb20iLCJJbnRlcmZhY2VUeXBlIjoiV2ViIiwiSXAiOiI6OmZmZmY6MTAuMTAwLjkuMTYyIiwibmJmIjoxNjk5NTMyMTY2LCJleHAiOjE2OTk2MTg1NjYsImlhdCI6MTY5OTUzMjE2NiwiaXNzIjoiU3RhdHVzSW52ZXN0IiwiYXVkIjoiU3RhdHVzSW52ZXN0In0.AZIgMIZz0MKZdUWWEneXuPQwo4kFPyq4zaJCKUAkfxCk65ksJBDHlR3AChiziD2nux1R87dMxlWbZ_Sn5vjuXA; pg_preload_gpt_check=1; pg_beacon=1; pg_custom_timeout=; pg_ip=187.66.147.41; pg_ua=Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36; __gads=ID=402e19e238d00c57:T=1691862106:RT=1701261364:S=ALNI_MbFxCHgCPsRxhybFO6qbDQH8XHfYQ; __gpi=UID=00000d9ec0426cf7:T=1691862106:RT=1701261364:S=ALNI_MbYunA3_W3ajmyCwTXAhNQcgX7CaA; _hjIncludedInSessionSample_1931042=0; _hjSession_1931042=eyJpZCI6IjljY2IyOGFjLTM3MmUtNGI5MC04YWUxLTJjMTUwOGM0OTllYiIsImNyZWF0ZWQiOjE3MDE1NTE1MDIzMjMsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=1; _clck=1nwv16w%7C2%7Cfh7%7C0%7C1319; cf_clearance=nCaUgRFGS70Lbj2wX8FvcKGTsFdvp_RkX1cLAUIKrrw-1701551500-0-1-844fdeed.26c8da0a.d34e810d-0.2.1701551500; __hstc=176625274.736daadd9b95a6cdc3111c3720e8d033.1691862107297.1701459314768.1701551520755.41; __hssrc=1; _clsk=14t6eyk%7C1701551534872%7C3%7C1%7Cr.clarity.ms%2Fcollect; _gcl_au=1.1.930955107.1699920290.641255453.1701551504.1701551543; __hssc=176625274.2.1701551520755; pg_buildfile=231115-cdb-nc-f6a2515cc2a2f45044e5791efedc16ed; pg_unq_cohort_key=2245:2311281534; pg_lazy=1; pg_driftingTypePercent=0; pg_chaser=1; pg_outstream=0; pg_vignettePercent=0; pg_autoAd=0; pg_session_depth=1; pg_session_id=067a2b80-3905-42e7-88c1-573638aa26bd; pg_tc=not-sampled; pg_preconnecting=enabled; pg_after_init_response_time=132; FCNEC=%5B%5B%22AKsRol-9HMUK5yA51LSeK1_5lE2l3oDfJTszlZwWhdFzApnyabv4Eraef3Tur-0J4w1bhWdgSlMmBWfVBA6zI59AH8IwfeI9jUemZqsXR-2xcUN7UzyVl4pvOCtQDmexDTJH8wQfI3Pab0Jmk79-GTE0fMtMd28uIA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; _ga_69GS6KP6TJ=GS1.1.1701551502.63.1.1701551583.60.0.0",
        "authority": "statusinvest.com.br",
        "accept": "*/*",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://statusinvest.com.br",
        "referer": "https://statusinvest.com.br/fundos-imobiliarios/vrta11",
        #"sec-ch-ua": ""Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"",
        "sec-ch-ua-mobile": "?1",
        #"sec-ch-ua-platform": ""Android"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    """Iniciando a requisição a API para coletar os dados e armazenar"""
    response = requests.request("POST", url, data=payload, headers=headers)
    funds= []
    if response.status_code == 200:
        data = response.json()
        prices = data[0]['prices']
        for entry in prices:
            date= entry['date'].split()[0]
            value = entry['price']
            funds.append(value)
    else:
        print('Erro na requisição')
    return funds


    