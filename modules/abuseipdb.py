def check_ip(ip):
    # Simulated IP reputation check
    blacklist = ['123.123.123.123', '10.10.10.10']
    return ip in blacklist
