
def simple_response(data):
    if ("message" in data) and (data["message"] is not None):
        print(data["message"])
    elif ("error" in data) and (data["error"] is not None):
        print(data["error"])
    elif ("detail" in data) and (type(data["detail"]) is list) and (data["detail"] is not None) :
        print(data["detail"][0]["msg"])
    elif ("detail" in data) and (data["detail"] is not None):
        print(data["detail"])
    else:
        print(data)

def simple_response_containing_list(data):
    if ("message" in data) and (data["message"] is not None):
        return data["message"]
    elif ("error" in data) and (data["error"] is not None):
        return data["error"]
    elif ("detail" in data) and (type(data["detail"]) is list) and (data["detail"] is not None):
        return data["detail"][0]["msg"]
    elif ("detail" in data) and (data["detail"] is not None):
        return data["detail"]
    else:
        return data

def external_server_status_response(data):
    server_name = data["server_name"]
    is_active = "Active" if data["is_active"] else "Not Active"
    last_accessed = data["last_accessed"][:10]
    print(f"{server_name} - {is_active} - last accessed : {last_accessed}")
    print("\n----------------------------------------------------------------------------")

def external_server_details_response(data):
    server_name = data["server_name"]
    api_key = data["api_key"]
    print(f"{server_name} - <{api_key}>")
    print("\n----------------------------------------------------------------------------")


def article_details_response(article):
    print(f"\nArticle Id: {article['article_id']}")
    print(f"{article['title']}\n\n{article['description']}\n")
    print(f"source: {article['source']}")
    print(f"URL:\n{article['url']}")
    print("\n----------------------------------------------------------------------------")

def notification_details_response(data):
    print(f"\n{data}")

def reported_articles_details_response(article):
    print(f"\nArticle Id: {article['article_id']}")
    print(f"\n Reason: {article['report_reason']}\n")
    print(f"reported_at: {article['reported_at']}")
    print("\n----------------------------------------------------------------------------")
