import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class FormHandler:
    def get_forms(self, url):
        """
        URL'den tüm form elemanlarını çeker.
        """
        try:
            resp = requests.get(url, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            return soup.find_all("form")
        except Exception as e:
            print(f"Error getting forms from {url}: {e}")
            return []

    def extract_form_details(self, form, base_url):
        """
        Formun action, method ve input bilgilerini çıkarır.
        """
        details = {}
        action = form.attrs.get("action")
        method = form.attrs.get("method", "get").lower()
        inputs = []

        for input_tag in form.find_all(["input", "textarea", "select"]):
            input_name = input_tag.attrs.get("name")
            input_type = input_tag.attrs.get("type", "text")
            input_value = input_tag.attrs.get("value", "")

            inputs.append({"name": input_name, "type": input_type, "value": input_value})

        details["action"] = urljoin(base_url, action) if action else base_url
        details["method"] = method
        details["inputs"] = inputs
        return details

    def submit_form(self, form_details, payload):
        """
        Formu payload ile doldurup gönderir.
        """
        data = {}
        for input_field in form_details["inputs"]:
            if input_field["type"] == "hidden" and "csrf" in (input_field["name"] or "").lower():
                data[input_field["name"]] = input_field["value"]
            elif input_field["type"] in ["text", "search", "url", "email", "textarea"]:
                data[input_field["name"]] = payload
            elif input_field["name"]:
                data[input_field["name"]] = input_field["value"]

        if form_details["method"] == "post":
            resp = requests.post(form_details["action"], data=data, timeout=50)
        else:
            resp = requests.get(form_details["action"], params=data, timeout=50)

        return resp

    def check_xss(self, response, payload):
        """
        Response'da payload olup olmadığını kontrol eder.
        """
        return payload in response.text
