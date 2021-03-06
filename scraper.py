import http.client, urllib.request, urllib.parse, urllib.error, base64, json
# Store keys in a separate file because don't push them to github
import config

def get_tag_image(imageURL):
    body = {"url" : imageURL}
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{}'.format(config.API_VISION),
    }

    params = urllib.parse.urlencode({
        # This API call does not need params
    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/tag?{}".format(params), "{}".format(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        data = "HTTPSConnection failed"
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    data = data.decode('utf-8')
    data = json.loads(data)
    print("Tag image received successfully")
    return data

def get_celebrity(imageURL):
    body = {"url" : imageURL}
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{}'.format(config.API_VISION),
    }

    params = urllib.parse.urlencode({

    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/models/{}/analyze?{}".format("celebrities", params), "{}".format(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        data = "HTTPSConnection failed"
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    data = data.decode('utf-8')
    data = json.loads(data)
    print("Celeb info received successfully")
    return data

def get_ocr(imageURL):
    body = {"url" : imageURL}
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '{}'.format(config.API_VISION),
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'language': 'unk',
        'detectOrientation ': 'true',
    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/ocr?{}".format(params), "{}".format(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        data = "HTTPSConnection failed"
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    data = data.decode('utf-8')
    data = json.loads(data)
    return data

def format_json(js):
    # return json.dumps((json.loads(js.decode('utf-8'))), indent = 4, sort_keys = True)
    return json.dumps(js, indent=4)