import nmap
import requests
import csv

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
        if 'data' in vulnerabilities and 'search' in vulnerabilities['data']:
            return vulnerabilities['data']['search']
    return []

def generate_report(scan_results, filename="report.csv"):
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Service', 'Vulnerability', 'Severity'])
        for result in scan_results:
            writer.writerow([
                result['port'],
                result['service'],
                result['vulnerability'],
                result['severity']
            ])

if __name__ == "__main__":
    target = "192.168.1.1"
    scan_data = scan_network(target)
    services = detect_services(scan_data)

    scan_results = []
    for port, service in services.items():
        vulnerabilities = check_vulnerabilities(service)
        for vulnerability in vulnerabilities:
            source = vulnerability['_source']
            scan_results.append({
                'port': port,
                'service': service,
                'vulnerability': source.get('description', 'N/A'),
                'severity': source.get('cvss3', {}).get('cvssV3', {}).get('baseSeverity', 'N/A')
            })

    generate_report(scan_results)
