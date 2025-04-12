import dns.resolver

def get_dns_record(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [rdata.to_text() for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoNameservers):
        return ["No record found"]

def get_basic_dns_records(domain):
    """
    Returns a dictionary with A, CNAME, MX, NS, TXT records.
    """
    records = {
        "A": get_dns_record(domain, "A"),
        "CNAME": get_dns_record(domain, "CNAME"),
        "MX": get_dns_record(domain, "MX"),
        "NS": get_dns_record(domain, "NS"),
        "TXT": get_dns_record(domain, "TXT"),
    }
    return records
