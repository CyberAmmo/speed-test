import speedtest


test = speedtest.Speedtest()

print('Loading server list...')
get_servers = test.get_servers() # getting list of all servers
print('Choosing nearest server...')
best_server = test.get_best_server() # choosing the best and nearest server
print(f"Best server is: {best_server['name']} {best_server['country']} {best_server['host']} sponsored by {best_server['sponsor']}")


print('Performing donwload test..')
donwload_test = test.download() # Creating download speed test
print('Performing upload test..')
upload_test = test.upload() # Creating upload speed test
ping = test.results.ping # Checking ping value

# Printing out results of all the tests
print(f'Download speed: {donwload_test / 1024 / 1024:.2f} Mbit/s')
print(f'Upload speed: {upload_test / 1024 / 1024:.2f} Mbit/s')
print(f'Ping is: {ping:.2f} ms')