import random
	from time import sleep
	
	while True:
	    temperature=round(random.uniform(10, 50),2)
	    humidity=round(random.uniform(10, 100),2)
	    print("\nTemperature =", temperature,"degree celsius")
	    print("Humidity = ",humidity,"%")
	    if(temperature>32):
	        print("STATE : ALARM ON")
	    else:
	        print("STATE : ALARM OFF")
	    sleep(5)
