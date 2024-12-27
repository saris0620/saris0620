"""ENG 1P13: Integrated Cornerstone Design Projects in Engineering
Design Studio Project 1
Group: Thurs-38
Program encapsulating all individual and team functions to produce the final graphic displaying specific information per plane
using fleet_data.txt and passenger_data.txt V2"""

#Start of code
import turtle

#Passenger data function
def passenger_data():
    """Function opens passanger text file and makes it into a 2D list of said data"""
    file = open("passenger_data_v2.txt")
    passenger= []
    for line in file:
        line = line.strip()
        line = line.split(",") # turn each line into a list of plane details
    
        passenger.append(line)

    file.close()
    return(passenger)

#Fleet data function
def fleet_data():
    """Function opens fleet text file and makes it into a 2D list of said data"""
    file = open("fleet_data.txt")
    fleetdata= []
    for line in file:
        line = line.strip()
        line = line.split(",")
    
        fleetdata.append(line)

    file.close()
    return(fleetdata)

#Graphical function
def graphical_thurs_38(oversoldB,oversoldE,layovers,time_delay,over):
    """Function made to display specific data from oversold, layover, time_delay and overweight
    sorted by plane"""
    
    #Create 2 turtles
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    
    #Setting  window specs
    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 450
    WINDOW_TITLE = "graphical_Thurs-38"
    
    #Set up the screen object
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = turtle.Screen()
    screen.title(WINDOW_TITLE)
    screen.bgpic("clouds.gif")
    
    #Prepare turtles for drawing
    x = -640 
    y = 50
    t1.ht()
    t2.ht()
    t1.speed(9)
    t2.speed(9)
    t1.fillcolor("#0E6ACC")

    t1.up()
    t1.goto(x,y)
    t2.up()
    t2.goto(x,y)

    for i in range(7):
        
        #Specify values wanted for each plane
        oversold_business = oversoldB[i][1]
        oversold_economy = oversoldE[i][1]
        overweight = over[i][1]
        layover = layovers[i][1]
        delay = time_delay[i][1]
        model = oversoldB[i][0]
        
        #Draw headers with plane names
        coord1 = t1.pos()
        t1.down()
        t1.begin_fill()
        t1.left(90)
        t1.fd(30)
        t1.right(90)
        t1.fd(180)
        t1.right(90)
        t1.fd(30)
        t1.right(90)
        t1.fd(180)
        t1.right(90)
        t1.end_fill()
        t1.up()
        t1.fd(5)
        t1.right(90)
        t1.fd(90)
        t1.write(model, align = "center", font =("Arial", 10, 'bold'))
        t1.goto(coord1)
        t1.fd(180)

        #Write plane info
        t2.right(90)
        coord2 = t2.pos()        
        t2.fd(25)
        t2.write("Oversold Business Seats: " + str(oversold_business))
        t2.fd(15)
        t2.write("Oversold Economy Seats: " + str(oversold_economy))
        t2.fd(15)
        t2.write("Overweight Bags: " + str(overweight))
        t2.fd(15)
        t2.write("Layover Passengers: " + str(layover))
        t2.fd(15)
        t2.write("Late Layover Passengers: " + str(delay))
        t2.left(90)
        t2.goto(coord2)
        t2.fd(180)
    
    t1.goto(300,-180)
    t1.write("Bon Voyage!", align = "center", font =("Verdana", 15, 'bold'))


    # Make a clean exit
    screen.exitonclick() 
    turtle.done()


#Start of individual functions    
#Daily data - Sara Reyes
def daily_data(passenger_data):
    """Function that processes passenger data and sorts the number of seats per seat type
    and returns a 2D list with each gate's information"""
    
    #creates list for each gate and main list for all gates
    gates = "H-17","H-12","D-11","B-15","D-7","E-4","F-5"       #ordered this way to match fleet data order and rest of functions
    daily_data = [[gate, 0, 0] for gate in gates]

    for row in passenger_data:
        gate = row[2]
        seat_type = row[4]
        
        #compares passenger_data with daily_data sublist
        for gate_info in daily_data:
            if gate_info[0] == gate:
                if seat_type == "B":
                    gate_info[1] += 1
                elif seat_type == "E":
                    gate_info[2] += 1

    return daily_data

#Overweight - Gaurinanda Abhilash
def overweight(fleet_data,passenger_data):
    """Function that takes output from passenger_data and fleet_data to produce two 2D list that
    sorts number of overweight bags per plane and exceeding weight per passenger"""
    passenger_overweight = []
    passenger_details = []
    
    for plane in fleet_data:
        # scan the fleet data file to get the info of plane
        plane_model = plane[0] 
        gate = plane[4]
        destination = plane[5]
        max_weight = int(plane[7])
        
        num_overweight = 0
        for passenger in passenger_data:
            # scan the passenger data file to get the info of passenger
            first_name = passenger[0] 
            last_name = passenger[1]
            passenger_gate = passenger[2]
            passenger_destination = passenger[3]
            passenger_weight = float(passenger[6])

            
            if passenger_gate == gate and passenger_destination == destination: # match up passenger to plane
                
                if passenger_weight > max_weight: 
                    num_overweight += 1
                    weight_exceeded = round(passenger_weight-max_weight,1) 
                    passenger_details.append([first_name,last_name,passenger_gate,weight_exceeded]) # add info to the second 2D list
                
        passenger_overweight.append([plane_model,num_overweight]) # add info to the first 2D list
                
    return passenger_details,passenger_overweight
    
#Layover - Fares Banat
def layover(fleet_data, passenger_data):
    """Function that uses output from passenger_data and fleet data to produce two 2D lists
    in respect to passengers with layovers; one sorted by passenger, the second by plane"""
    
    # Initialize layover with plane models and counts
    layover = [
        ["Boeing 777-300ER", 0], 
        ["Boeing 777-200LR", 0], 
        ["Airbus A330-300", 0], 
        ["Embraer A330-300", 0], 
        ["Airbus A319-100", 0], 
        ["Boeing 737 MAX 8", 0], 
        ["Airbus A321-200", 0]
    ]
    
    layoverNames = [[] for _ in range(len(passenger_data))]
    
    for i in range(len(passenger_data)):
            if passenger_data[i][7] == "Layover":
                layoverNames[i].append(passenger_data[i][0])
                layoverNames[i].append(passenger_data[i][1])
                layoverNames[i].append(passenger_data[i][2])
                gate = passenger_data[i][2]

                if gate == "H-17":
                    layover[0][1] += 1
                elif gate == "H-12":
                    layover[1][1] += 1
                elif gate == "D-11":
                    layover[2][1] += 1
                elif gate == "B-15":
                    layover[3][1] += 1
                elif gate == "D-7":
                    layover[4][1] += 1
                elif gate == "E-4":
                    layover[5][1] += 1
                elif gate == "F-5":
                    layover[6][1] += 1

    layoverNames = [sublist for sublist in layoverNames if sublist]
    return layoverNames,layover

#Time delay - David Choi
def time_delay(passenger_data, fleet_data):
    """Function that uses output from passenger_data, and fleet_data to produce a 2D list 
    with the plane models and the total number of passengers that will arrive late and have a layover"""
    result = []
    for plane in fleet_data:
        model = plane[0]
        gate = plane[4]
        num_late_layer = 0
        
        for passenger in passenger_data:
            if passenger[2] == gate:
                if len(passenger) == 8 and passenger[5] == "Late" and passenger[7] == "Layover":
                    num_late_layer += 1
        result.append([model, num_late_layer])
    return result

#Oversold - Ifeyinwa Mbielu
def oversold (passenger_data,fleet_data,daily_data):
    """This function uses the outputs of passenger_data, fleet_data and daily_data as inputs. 
    the output is the number of oversold seats for business class and economy in two different lists""" 
    
    economic_oversold=[]
    business_oversold=[]
    
    for daily in daily_data:
        gate = daily[0]
        business_passengers = int(daily[1])
        economy_passengers = int(daily[2])

        # Find the corresponding plane model and its seat capacities
        plane_model = None
        business_capacity = 0
        economy_capacity = 0

        for fleet in fleet_data:
            
            if fleet[4] == gate and daily[0]:  # Match gate to find the correct plane
                plane_model = fleet[0]
                business_capacity = int(fleet[1])
                economy_capacity = int(fleet[2])
               
                # Calculate oversold seats ensuring no negatives
                if business_capacity < business_passengers:
                    boversold =  business_passengers - business_capacity
                else:
                    boversold = 0
                if economy_capacity<economy_passengers:
                    eoversold =  economy_passengers - economy_capacity
                else:
                    eoversold = 0
    
                business_oversold.append([plane_model, boversold])
                economic_oversold.append([plane_model, eoversold])

    return  business_oversold,economic_oversold


#Assigning variables to functions to set parameters
passenger = passenger_data()
fleet = fleet_data()

daily = daily_data(passenger)
layover = layover(fleet,passenger)[1]            #specify which list within function
oversoldB = oversold(passenger,fleet,daily)[0] 
oversoldE = oversold(passenger,fleet,daily)[1]
overweight = overweight(fleet,passenger)[1]
delay = time_delay(passenger,fleet)

graphical_thurs_38(oversoldB,oversoldE,layover,delay,overweight)
















