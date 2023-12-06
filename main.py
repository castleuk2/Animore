from typing import List
import pandas as pd
from geopy.geocoders import Nominatim
import folium
# 제작한 Class들 import
from Pet_Customer_Class import Pet, Customer 
from Savesystem_Class import SaveSystem
from AppointSystem_Class import AppointSystem
from ReviewSystem_Class import ReviewSystem
from Ceneter_Class import Center

from folium_func import real_address, geocoding, phone_number, facility_name
def main():
    while True:
        customer1 = Customer()
        print(customer1)
        file_path = "C:\\Users\\monog\\OneDrive\\바탕 화면\\Python_Project\\Animore\\center.csv"
        save_list = SaveSystem(file_path)
        find_address = customer1.contact_SaveSys(save_list)
        result = save_list.filter_data_by_region(find_address)
        center_list = result.values.tolist()
        print(center_list)
        if not result.empty: 
            address1 = real_address(result)
            phone_numbers = phone_number(result)
            facility_names = facility_name(result)
        
        hospital_locations = get_locations(address1)
        
        m = folium.Map(location=geocoding(customer1.address), 
                zoom_start=14, 
                )
        folium.Marker(
        location=geocoding(customer1.address),
        popup="현재 나의 위치",
        icon=folium.Icon(color="purple", icon="home"),).add_to(m)
        for i in range(len(hospital_locations)):
            folium.Marker(location=hospital_locations[i],popup=f"{haversine(hospital_locations[i],geocoding(customer1.address),unit = 'km'):.2f} km", tooltip = f"{facility_names[i]} {phone_numbers[i]}").add_to(m)
        m.save('location.html')
        webbrowser.open_new('location.html')
        
        
        
        customer1.appoint_Center()
        appoint_center = Center()
        appoint = AppointSystem()
        appoint.request_appoint()
        appoint_center.accept_appoint(appoint.patient_info, appoint.time)
    
        review_system = ReviewSystem(center_list,file_path)
        review_system.write_review_interaction(center_list)

    

    
    

if __name__ == "__main__":
    main()
