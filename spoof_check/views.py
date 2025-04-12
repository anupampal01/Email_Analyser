from django.shortcuts import render
import re

def spoof_detection(request):
    result = "Waiting for input..."

    if request.method == "POST":
        email_headers = request.POST.get("email_headers", "")
        headers_lower = email_headers.lower()
        spoof_signals = []

        # --- SPF Check ---
        if "spf=fail" in headers_lower or "spf: fail" in headers_lower or "received-spf: fail" in headers_lower:
            spoof_signals.append("SPF Check Failed ❌")
        elif "spf=softfail" in headers_lower or "spf: softfail" in headers_lower:
            spoof_signals.append("SPF Softfail ❌")
        elif "spf=neutral" in headers_lower or "spf: neutral" in headers_lower:
            spoof_signals.append("SPF Neutral Result ❌")
        elif "spf=none" in headers_lower or "spf: none" in headers_lower:
            spoof_signals.append("SPF Record Missing ❌")

        # --- DKIM Check ---
        if "dkim=fail" in headers_lower or "dkim: fail" in headers_lower or "dkim=fail (bad signature)" in headers_lower:
            spoof_signals.append("DKIM Check Failed ❌")
        elif "dkim=none" in headers_lower or "dkim: none" in headers_lower:
            spoof_signals.append("DKIM Record Missing ❌")
        elif "dkim=fail (selector not found)" in headers_lower:
            spoof_signals.append("DKIM Selector Missing ❌")

        # --- DMARC Check ---
        if "dmarc=fail" in headers_lower or "dmarc: fail" in headers_lower:
            spoof_signals.append("DMARC Check Failed ❌")
        elif "dmarc=fail (policy=reject)" in headers_lower:
            spoof_signals.append("DMARC Policy Reject Failed ❌")

        # --- Return-Path Check ---
        from_match = re.search(r"from:\s*([^\n\r<]+@[\w\.-]+)", headers_lower)
        return_path_match = re.search(r"return-path:\s*<([^>]+)>", headers_lower)
        if from_match and return_path_match:
            from_email = from_match.group(1).strip()
            return_path_email = return_path_match.group(1).strip()
            if from_email != return_path_email:
                spoof_signals.append("Return-Path Mismatch ⚠️")

        # --- Display Name Spoofing ---
        if re.search(r'from:\s*".+?"\s*<[^>]+>', headers_lower):
            display_name_email = re.search(r'from:\s*".+?"\s*<([^>]+)>', headers_lower)
            if display_name_email:
                email_addr = display_name_email.group(1)
                if any(domain in email_addr for domain in ['malicious', 'fake', 'phish']):
                    spoof_signals.append("Display Name Spoofing Detected ⚠️")

        # --- Received Header Suspicion ---
        if "received: from unknown" in headers_lower or "via unknown relay" in headers_lower:
            spoof_signals.append("Received Header Mismatch / Unknown Relay 🚨")

        # --- Private IP Detection ---
        if re.search(r"received: from\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", headers_lower):
            ip = re.findall(r"received: from\s+(\d{1,3}(?:\.\d{1,3}){3})", headers_lower)
            if any(ipv.startswith("192.168") or ipv.startswith("10.") or ipv.startswith("172.") for ipv in ip):
                spoof_signals.append("Private IP Detected in Received Header ❌")

        # --- Suspicious Keywords ---
        suspicious_keywords = ["verify", "update account", "urgent", "click here", "login immediately"]
        for keyword in suspicious_keywords:
            if keyword in headers_lower:
                spoof_signals.append(f"Suspicious Keyword Detected: '{keyword}' ⚠️")
                break

        # --- All Auth Fields Missing ---
        auth_present = any(k in headers_lower for k in [
            "spf=", "spf:", "dkim=", "dkim:", "dmarc=", "dmarc:",
            "received-spf: pass", "spf: pass", "dkim: pass", "dmarc: pass"
        ])
        if not auth_present:
            spoof_signals.append("Missing SPF, DKIM, DMARC Authentication ❌")

        # --- Final Decision ---
        if spoof_signals:
            result = "🚨 Spoofing or Phishing Detected!\n" + "\n".join(spoof_signals)
        else:
            result = "✅ Email appears legitimate. No spoofing indicators found."

    return render(request, 'spoof_check.html', {"result": result})
