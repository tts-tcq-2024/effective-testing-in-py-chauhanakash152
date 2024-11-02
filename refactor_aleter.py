# alert_module.py

alert_failure_count = 0

def network_alert_real(celcius):
    """Real network alert function that sends alerts over the network."""
    # Here, actual network code would go, e.g., sending a HTTP request.
    print(f'ALERT: Temperature is {celcius} celcius')
    # For demonstration, simulate success or failure
    if celcius > 100:
        return 500  # Simulated failure for high temperatures
    return 200  # Simulated success

def alert_in_celcius(fahrenheit, network_alert):
    """Converts Fahrenheit to Celsius and sends an alert if threshold is breached."""
    global alert_failure_count
    celcius = (fahrenheit - 32) * 5 / 9
    return_code = network_alert(celcius)
    if return_code != 200:
        alert_failure_count += 1
