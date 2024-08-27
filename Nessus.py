import nmap
import requests

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')  # Scanning ports 1 to 1024
    return nm

def detect_services(scan_data):
    services = {}
    for host in scan_data.all_hosts():
        for proto in scan_data[host].all_protocols():
            ports = scan_data[host][proto].keys()
            for port in ports:
                service = scan_data[host][proto][port]['name']
                services[port] = service
    return services

def check_vulnerabilities(service_name):
    url = f"https://vulners.com/api/v3/search/lucene/?query={service_name}"
    response = requests.get(url)
    if response.status_code == 200:
        vulnerabilities = response.json()
        return vulnerabilities
    return None

def generate_report(scan_results, filename="report.csv"):
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Service', 'Vulnerability', 'Severity'])
        for result in scan_results:
            writer.writerow([result['port'], result['service'], 
result['vulnerability'], result['severity']])

if __name__ == "__main__":
    target = "192.168.1.1"
    scan_data = scan_network(target)
    services = detect_services(scan_data)

    scan_results = []
    for port, service in services.items():
        vulnerabilities = check_vulnerabilities(service)
        if vulnerabilities:
            for vulnerability in vulnerabilities['data']:
                scan_results.append({
                    'port': port,
                    'service': service,
                    'vulnerability': vulnerability['title'],
                    'severity': vulnerability['cvss']['score']
                })

    generate_report(scan_results)

