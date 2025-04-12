import email
from email import message_from_binary_file
import dns.resolver
from django.shortcuts import render
from django.http import HttpResponseBadRequest

def get_domain_from_email(email_addr):
    return email_addr.split("@")[-1] if email_addr and "@" in email_addr else None

def check_spf(msg):
    domain = get_domain_from_email(msg.get("From"))
    try:
        records = dns.resolver.resolve(domain, 'TXT')
        for r in records:
            if 'v=spf1' in r.to_text():
                return r.to_text().strip('"')
    except:
        return "SPF not found"
    return "SPF record not found"

def check_dkim(msg):
    domain = get_domain_from_email(msg.get("From"))
    selector = "default"
    dkim_domain = f"{selector}._domainkey.{domain}"
    try:
        records = dns.resolver.resolve(dkim_domain, 'TXT')
        for r in records:
            if 'v=DKIM1' in r.to_text():
                return r.to_text().strip('"')
    except:
        return "DKIM not found"
    return "DKIM record not found"

def check_dmarc(msg):
    domain = get_domain_from_email(msg.get("From"))
    dmarc_domain = f"_dmarc.{domain}"
    try:
        records = dns.resolver.resolve(dmarc_domain, 'TXT')
        for r in records:
            if 'v=DMARC1' in r.to_text():
                return r.to_text().strip('"')
    except:
        return "DMARC not found"
    return "DMARC record not found"

def parse_email(request):
    if request.method == 'POST':
        eml_file = request.FILES.get('eml_file')
        if not eml_file:
            return HttpResponseBadRequest("No .eml file provided")

        try:
            # Memory se parse kar rahe hain:
            msg = message_from_binary_file(eml_file.file)

            parsed_info = {
                "From": msg.get("From", "Unknown sender"),
                "To": msg.get("To", "Unknown recipient"),
                "Subject": msg.get("Subject", "No subject"),
                "Date": msg.get("Date", "No date"),
                "Body": "",
                "SPF": check_spf(msg),
                "DKIM": check_dkim(msg),
                "DMARC": check_dmarc(msg),
            }

            # Email body handle
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        parsed_info["Body"] = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                parsed_info["Body"] = msg.get_payload(decode=True).decode(errors="ignore")

            return render(request, "results.html", parsed_info)

        except Exception as e:
            return HttpResponseBadRequest(f"Error parsing file: {e}")
    else:
        return render(request, "email_parser.html")  # Your form template
