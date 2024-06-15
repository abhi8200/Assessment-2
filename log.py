import re
from collections import Counter

def analyze_log(log_file_path):
    # Regular expressions to extract useful information
    status_code_pattern = re.compile(r'"\s(\d{3})\s')
    requested_page_pattern = re.compile(r'"\s(\S+)\sHTTP')

    # Variables to store analysis results
    total_requests = 0
    error_404_count = 0
    requested_pages = []
    ip_address_requests = Counter()

    # Read and analyze the log file
    with open(log_file_path, 'r') as file:
        for line in file:
            total_requests += 1

            # Extract status code and requested page
            status_code_match = status_code_pattern.search(line)
            requested_page_match = requested_page_pattern.search(line)

            if status_code_match:
                status_code = status_code_match.group(1)
                if status_code == '404':
                    error_404_count += 1

            if requested_page_match:
                requested_page = requested_page_match.group(1)
                requested_pages.append(requested_page)

                # Extract IP address
                ip_address = line.split()[0]
                ip_address_requests[ip_address] += 1

    # Generate the summary report
    print("Summary Report:")
    print(f"Total Requests: {total_requests}")
    print(f"404 Errors: {error_404_count}")
    print("Top 5 Requested Pages:")
    for page, count in Counter(requested_pages).most_common(5):
        print(f"{page}: {count} requests")
    print("Top 5 IP Addresses with Most Requests:")
    for ip, count in ip_address_requests.most_common(5):
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    log_file_path = "/var/log/apache2/access.log" # Provide the path to your web server log file
    analyze_log(log_file_path)
