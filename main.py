import krpc
from time import sleep
import os
import math
from sympy import integrate, sin, oo, Symbol, cos as sm
from sympy.abc import x

 
    
def main():
    
    conn = krpc.connect(
        name = "PEW SPACE",
        address = '192.168.1.82',
        rpc_port=50000, stream_port=50001
    )
    print("SERVER STATUS: OK")
    
    vessel = conn.space_center.active_vessel
     
    time = 0
        
    with open("air-speed.txt", "w") as file:
        file.write(f"0, 0\n")
        file.close()
                
    with open("mass-time.txt", 'w') as file:
        file.write(f"0, 0\n")
        file.close()
                
    with open("impulse-time.txt", 'w') as file:
        file.write(f"0, 0\n")
        file.close()
            
    with open("vx-time.txt", "w") as file:
        file.write(f"0, 0\n")
        file.close()
            
    with open("vy-time.txt", "w") as file:
        file.write(f"0, 0\n")
        file.close()     
            
    with open("pitch-time.txt", 'w') as file:
        file.write(f"0, 0\n")
        file.close()
        
    with open("thrust-time.txt", 'w') as file:
        file.write(f'0, 0\n')
        file.close()
                
    flag_activate = False
    start_time = 0
    
    times = 0     
        
    # vx, vy, v, angels-time, mass-time, impulse-time        
    while True:       
        refframe = vessel.orbit.body.reference_frame
        flight_info = vessel.flight(reference_frame=refframe)
         
        air_speed = int(flight_info.true_air_speed)
        mass = int(vessel.mass)
        thrust = vessel.thrust
        dry_mass = vessel.dry_mass
        impulse = int(vessel.specific_impulse)
        horizontal_speed = int(flight_info.horizontal_speed)
        vertical_speed = int(flight_info.vertical_speed)
        pitch = int(flight_info.pitch) 
        
        
        if air_speed != 0:
            
            ut = int(conn.space_center.ut) - 21600*times
            
            if flag_activate == False:
                print('y')
                flag_activate = True
                start_time = ut
                ut -= start_time
                
            else:
                ut -= start_time 
                
            print(ut)
            
            if ut >= 21600:
                print('day skipped')
                times+=1

                
            # if ut >= 21600 and (times != 0):
            #     print(ut, times)
            #     ut -= (21600 * times)
            #     times += 1
                
            # elif ut >= 21600:
            #     ut -= 21600
            #     times += 1
                
            # else:
            #     ut -= start_time
                
            with open("resources.txt", "a") as file:
                file.write(f"{ut}, {mass - dry_mass}")
                file.close()
                 
            with open("air-speed.txt", "a") as file:
                file.write(f"{ut}, {air_speed}\n")
                file.close()
                
            with open("mass-time.txt", 'a') as file:
                file.write(f'{ut}, {mass}\n')
                file.close()
                
            with open("impulse-time.txt", 'a') as file:
                file.write(f'{ut}, {impulse}\n')
                file.close()
            
            with open("vx-time.txt", "a") as file:
                file.write(f'{ut}, {horizontal_speed}\n')
                file.close()
            
            with open("vy-time.txt", "a") as file:
                file.write(f'{ut}, {vertical_speed}\n')
                file.close()     
            
            with open("pitch-time.txt", 'a') as file:
                file.write(f'{ut}, {pitch}\n')
                file.close()
                
            with open("thrust-time.txt", 'a') as file:
                file.write(f'{ut}, {thrust}\n')
                file.close()
                
            
            
            time += 2
            sleep(0.01)   
            

if __name__ == "__main__":
    main()
