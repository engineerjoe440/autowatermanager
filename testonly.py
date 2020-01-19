from model import unit_model, system_model


# Define Built-In Test
if __name__ == '__main__':
    # Import Libraries
    import matplotlib.pyplot as plt
    # Define System Parameters
    ambient = 31
    system = system_model(ambient)
    water_temp = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # Process twenty-four hours
    minutes = 60*24
    for i in range(minutes):
        # Update the Model Instances
        system.update(ambient)
        # Retrieve Water Temp
        temp = system.get_temp()
        # Split into Lists
        for ind,item in enumerate(temp):
            water_temp[ind].append(item)
    # Plot Temperatures Over Time
    plt.figure(figsize=(14, 8))
    for i,temp in enumerate(water_temp):
        if i < 12:
            plt.plot(temp,label='water temp '+str(i+1))
        else:
            plt.plot(temp,linestyle=':',label='stock water temp')
    plt.axhline(32)
    plt.xlabel('Time (minutes)')
    plt.ylabel('Temperature (°F)')
    plt.title("Water Tank System Monitor")
    plt.show()