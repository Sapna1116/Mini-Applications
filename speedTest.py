import speedtest

def check_speed():
    st = speedtest.Speedtest()
    
    print("Fetching server list...")
    st.get_servers()  # Fetch available servers

    print("Selecting best server...")
    st.get_best_server()  # Select the best server based on ping
    
    print("Testing download speed...")
    download_speed = st.download() / 10**6  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")

    print("Testing upload speed...")
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    check_speed()
