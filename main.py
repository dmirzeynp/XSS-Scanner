from scanner import scan_site
from reporter import save_json_report, save_html_report
from colorama import init, Fore, Style

def print_banner():
    init(autoreset=True)  # Renklerin otomatik sıfırlanması için

    print(Fore.RED + Style.BRIGHT + "\n====================================")
    print(Fore.RED + Style.BRIGHT + "     🚨 XSS Scanner Başlatıldı 🚨")
    print(Fore.RED + Style.BRIGHT + "====================================")
    print(Fore.YELLOW + "UYARI: Bu araç sadece yetkilendirilmiş güvenlik testleri için kullanılmalıdır!\n")
    print(Fore.CYAN + "Kullanım:")
    print(Fore.CYAN + "- Hedef URL'yi tam olarak girin (örn: https://example.com)")
    print(Fore.CYAN + "- Tarama tamamlandığında raporlar 'report.json' ve 'report.html' olarak kaydedilecek.\n")

def main():
    print_banner()
    url = input(Fore.GREEN + "Hedef URL'yi girin: " + Style.RESET_ALL).strip()

    if not (url.startswith("http://") or url.startswith("https://")):
        print(Fore.RED + "[!] Lütfen geçerli bir URL girin. Örn: https://example.com")
        return

    print(Fore.BLUE + f"[+] Taranıyor: {url}\n" + Style.RESET_ALL)
    results = scan_site(url)

    if results:
        print(Fore.MAGENTA + f"[+] {len(results)} zafiyet bulundu.")
        save_json_report(results)
        save_html_report(results)
        print(Fore.MAGENTA + "[+] Raporlar oluşturuldu: report.json & report.html")
    else:
        print(Fore.YELLOW + "[-] XSS zafiyeti bulunamadı.")

if __name__ == "__main__":
    main()
