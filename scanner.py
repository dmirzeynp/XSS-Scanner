from urllib.parse import urlparse, parse_qs
from payload_manager import get_payloads
from crawler import get_all_links
from form_handler import FormHandler
import requests

def scan_site(target_url, payload_level="default", payload_file=None):
    """
    Verilen hedef URL'de XSS zafiyetleri arar.
    
    Args:
        target_url (str): Taranacak site URL'si.
        payload_level (str): 'default' veya 'advanced' gibi payload seviyesi.
        payload_file (str): Dosyadan payload okutmak istersen dosya yolu.
        
    Returns:
        list: Bulunan zafiyetlerin listesi.
    """
    results = []

    payloads = get_payloads(payload_level, from_file=payload_file)
    form_handler = FormHandler()

    urls = get_all_links(target_url)
    urls.append(target_url)  # Ana sayfa dahil

    # GET parametreli URL testleri
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        if not params:
            continue

        for param in params:
            for payload in payloads:
                test_url = url.replace(f"{param}={params[param][0]}", f"{param}={payload}")
                try:
                    resp = requests.get(test_url, timeout=10)
                    if payload in resp.text:
                        results.append({
                            "url": test_url,
                            "param": param,
                            "payload": payload,
                            "method": "GET"
                        })
                        break
                except Exception as e:
                    print(f"Error testing {test_url}: {e}")

    # Form testleri
    for url in urls:
        forms = form_handler.get_forms(url)
        for form in forms:
            form_details = form_handler.extract_form_details(form, url)
            for payload in payloads:
                try:
                    resp = form_handler.submit_form(form_details, payload)
                    if form_handler.check_xss(resp, payload):
                        vulnerable_input = None
                        for input_field in form_details["inputs"]:
                            if input_field["type"] in ["text", "search", "url", "email", "textarea"]:
                                vulnerable_input = input_field["name"]
                                break
                        results.append({
                            "url": url,
                            "form_action": form_details["action"],
                            "method": form_details["method"],
                            "payload": payload,
                            "vulnerable_input": vulnerable_input
                        })
                        break
                except Exception as e:
                    print(f"Error submitting form on {url}: {e}")

    # Basit DOM XSS testleri (placeholder)
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        if not params:
            continue
        try:
            resp = requests.get(url, timeout=10)
            page_text = resp.text.lower()
            for param, values in params.items():
                for payload in payloads:
                    if payload.lower() in page_text and "document.location" in page_text:
                        results.append({
                            "url": url,
                            "param": param,
                            "payload": payload,
                            "method": "DOM"
                        })
                        break
        except Exception as e:
            print(f"Error during DOM XSS check on {url}: {e}")

    # Tekrarlayan sonuçları filtrele
    unique_results = []
    seen = set()
    for r in results:
        key = (r.get("url"), r.get("param", None), r.get("form_action", None), r.get("payload"), r.get("method"))
        if key not in seen:
            seen.add(key)
            unique_results.append(r)

    return unique_results
