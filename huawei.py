

import requests


def get_search_headers():
    return {"Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; Android SDK built for x86_64 Build/SC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
            "Origin": "https://appgallery.huawei.com",
            "X-Requested-With": "org.chromium.webview_shell",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Dest":"empty",
            "Referer":"https://appgallery.huawei.com/",
            "Connection":"close"
            }


def get_download_headers():
    return {"User-Agent":"UpdateSDK##4.0.1.300##Android##Pixel 2##com.huawei.appmarket##12.0.1.301"}

def client_api_body(app_id):
    return f"agVersion=12.0.1&brand=Android&buildNumber=QQ2A.200405.005.2020.04.07.17&density=420&deviceSpecParams=%7B%22abis%22%3A%22arm64-v8a%2Carmeabi-v7a%2Carmeabi%22%2C%22deviceFeatures%22%3A%22U%2CP%2CB%2C0c%2Ce%2C0J%2Cp%2Ca%2Cb%2C04%2Cm%2Candroid.hardware.wifi.rtt%2Ccom.google.hardware.camera.easel%2Ccom.google.android.feature.PIXEL_2017_EXPERIENCE%2C08%2C03%2CC%2CS%2C0G%2Cq%2CL%2C2%2C6%2CY%2CZ%2C0M%2Candroid.hardware.vr.high_performance%2Cf%2C1%2C07%2C8%2C9%2Candroid.hardware.sensor.hifi_sensors%2CO%2CH%2Ccom.google.android.feature.TURBO_PRELOAD%2Candroid.hardware.vr.headtracking%2CW%2Cx%2CG%2Co%2C06%2C0N%2Ccom.google.android.feature.PIXEL_EXPERIENCE%2C3%2CR%2Cd%2CQ%2Cn%2Candroid.hardware.telephony.carrierlock%2Cy%2CT%2Ci%2Cr%2Cu%2Ccom.google.android.feature.WELLBEING%2Cl%2C4%2C0Q%2CN%2CM%2C01%2C09%2CV%2C7%2C5%2C0H%2Cg%2Cs%2Cc%2C0l%2Ct%2C0L%2C0W%2C0X%2Ck%2C00%2Ccom.google.android.feature.GOOGLE_EXPERIENCE%2Candroid.hardware.sensor.assist%2Candroid.hardware.audio.pro%2CK%2CE%2C02%2CI%2CJ%2Cj%2CD%2Ch%2Candroid.hardware.wifi.aware%2C05%2CX%2Cv%22%2C%22dpi%22%3A420%2C%22preferLan%22%3A%22en%22%7D&emuiApiLevel=0&firmwareVersion=10&getSafeGame=1&gmsSupport=0&hardwareType=0&harmonyApiLevel=0&harmonyDeviceType=&installCheck=0&isFullUpgrade=0&isUpdateSdk=1&locale=en_US&magicApiLevel=0&magicVer=&manufacturer=Google&mapleVer=0&method=client.updateCheck&odm=0&packageName=com.huawei.appmarket&phoneType=Pixel%202&pkgInfo=%7B%22params%22%3A%5B%7B%22isPre%22%3A0%2C%22maple%22%3A0%2C%22oldVersion%22%3A%221.0%22%2C%22package%22%3A%22{app_id}%22%2C%22pkgMode%22%3A0%2C%22shellApkVer%22%3A0%2C%22targetSdkVersion%22%3A19%2C%22versionCode%22%3A1%7D%5D%7D&resolution=1080_1794&sdkVersion=4.0.1.300&serviceCountry=IE&serviceType=0&supportMaple=0&ts=1649970862661&ver=1.2&version=12.0.1.301&versionCode=120001301"




def search(searchterm, proxies):

    r = requests.get(f"https://web-dre.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum=1&uri=searchApp%7C{searchterm}&maxResults=25&zone=&locale=en",headers=get_search_headers(),proxies=proxies)
    r.raise_for_status()
    return r.json()



def download(app_id,proxies):
    r = requests.post("https://store-dre.hispace.dbankcloud.com/hwmarket/api/clientApi",data=client_api_body(app_id),headers=get_download_headers(),proxies=proxies)

    list = r.json()['list']
    if(len(list)==0):
        return "App not found in appgallery"
    down_url = list[0]['fullDownUrl']

    return requests.get(down_url, stream = True, proxies=proxies)
  

