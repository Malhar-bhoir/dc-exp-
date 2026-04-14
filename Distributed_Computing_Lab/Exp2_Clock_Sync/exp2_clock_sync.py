import ntplib
from time import time
import datetime

def sync_with_ntp(server_list=None):
    if server_list is None:
        server_list = ["pool.ntp.org", "time.google.com", "time.windows.com"]
        
    ntp_client = ntplib.NTPClient()
    
    for server in server_list:
        try:
            print(f"Trying NTP server: {server}")
            response = ntp_client.request(server, version=3)
            
            # Get the system and NTP time
            system_time = time()
            ntp_time = response.tx_time
            
            print(f"System Time: {datetime.datetime.fromtimestamp(system_time)}")
            print(f"NTP Time from {server}: {datetime.datetime.fromtimestamp(ntp_time)}")
            
            # Calculate offset and delay
            time_offset = ntp_time - system_time
            print(f"Clock Offset: {time_offset:.6f} seconds\n")
            break
            
        except ntplib.NTPException as e:
            print(f"Failed to sync with {server}: {e}")
        except Exception as ex:
            print(f"Error: {ex}")

if __name__ == "__main__":
    # NOTE: You may need to run 'pip install ntplib' in your terminal first
    sync_with_ntp()