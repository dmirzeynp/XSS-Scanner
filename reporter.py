import json

def save_json_report(results, filename="report.json"):
    """
    Sonuçları JSON dosyasına kaydeder.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"[+] JSON raporu oluşturuldu: {filename}")
    except Exception as e:
        print(f"[!] JSON raporu kaydedilirken hata oluştu: {e}")

def save_html_report(results, filename="report.html"):
    """
    Sonuçları HTML dosyası olarak kaydeder.
    """
    html_content = """
    <html>
    <head>
        <title>XSS Tarama Raporu</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
            tr:hover { background-color: #f1f1f1; }
        </style>
    </head>
    <body>
        <h1>XSS Tarama Raporu</h1>
        <table>
            <tr>
                <th>URL</th>
                <th>Parametre / Form Input</th>
                <th>Metot</th>
                <th>Payload</th>
            </tr>
    """

    for res in results:
        url = res.get("url", "-")
        param = res.get("param", res.get("vulnerable_input", "-"))
        method = res.get("method", "-")
        payload = res.get("payload", "-")
        html_content += f"""
            <tr>
                <td>{url}</td>
                <td>{param}</td>
                <td>{method}</td>
                <td>{payload}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[+] HTML raporu oluşturuldu: {filename}")
    except Exception as e:
        print(f"[!] HTML raporu kaydedilirken hata oluştu: {e}")
