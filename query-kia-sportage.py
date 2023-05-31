from hyundai_kia_connect_api import *
import json
from configuration import *

vm = VehicleManager(region=configuration["region"], brand=configuration["brand"], username=configuration["username"], password=configuration["password"], pin=configuration["pin"])
vm.check_and_refresh_token()
vm.update_all_vehicles_with_cached_state()

#print(vm.vehicles)

class VehicleEncoder(json.JSONEncoder):
    def default(self, vehicle):
        return {
            "id": vehicle.id,
            "name": vehicle.name,
            "vin": vehicle.VIN,
            "car_battery_percentage": vehicle.car_battery_percentage,
            "engine_is_running": vehicle.engine_is_running,
            "last_updated_at": vehicle.last_updated_at.isoformat(),
            "smart_key_battery_warning_is_on": vehicle.smart_key_battery_warning_is_on,
            "washer_fluid_warning_is_on": vehicle.washer_fluid_warning_is_on,
            "brake_fluid_warning_is_on": vehicle.brake_fluid_warning_is_on,

            # Climate
            "air_temperature": vehicle.air_temperature,
            "air_control_is_on": vehicle.air_control_is_on,
            "defrost_is_on": vehicle.defrost_is_on,
            "steering_wheel_heater_is_on": vehicle.steering_wheel_heater_is_on,
            "back_window_heater_is_on": vehicle.back_window_heater_is_on,
            "side_mirror_heater_is_on": vehicle.side_mirror_heater_is_on,
            "front_left_seat_status": vehicle.front_left_seat_status,
            "front_right_seat_status": vehicle.front_right_seat_status,
            "rear_left_seat_status": vehicle.rear_left_seat_status,
            "rear_right_seat_status": vehicle.rear_right_seat_status,

             # Door Status
            "is_locked": vehicle.is_locked,
            "front_left_door_is_open": vehicle.front_left_door_is_open,
            "front_right_door_is_open": vehicle.front_right_door_is_open,
            "back_left_door_is_open": vehicle.back_left_door_is_open,
            "back_right_door_is_open": vehicle.back_right_door_is_open,
            "trunk_is_open": vehicle.trunk_is_open,
            "hood_is_open": vehicle.hood_is_open,

            # Window Status
            "front_left_window_is_open": vehicle.front_left_window_is_open,
            "front_right_window_is_open": vehicle.front_right_window_is_open,
            "back_left_window_is_open": vehicle.back_left_window_is_open,
            "back_right_window_is_open": vehicle.back_right_window_is_open,

            # Tire Pressure
            "tire_pressure_all_warning_is_on": vehicle.tire_pressure_all_warning_is_on,
            "tire_pressure_rear_left_warning_is_on": vehicle.tire_pressure_rear_left_warning_is_on,
            "tire_pressure_front_left_warning_is_on": vehicle.tire_pressure_front_left_warning_is_on,
            "tire_pressure_front_right_warning_is_on": vehicle.tire_pressure_front_right_warning_is_on,
            "tire_pressure_rear_right_warning_is_on": vehicle.tire_pressure_rear_right_warning_is_on,

            "ev_battery_percentage": vehicle.ev_battery_percentage,
            "ev_battery_is_charging": vehicle.ev_battery_is_charging,
            "ev_battery_is_plugged_in": vehicle.ev_battery_is_plugged_in,

            "ev_driving_range": vehicle.ev_driving_range,
            "ev_estimated_current_charge_duration": vehicle.ev_estimated_current_charge_duration,

            "fuel_driving_range": vehicle.fuel_driving_range,

            "total_driving_range": vehicle.total_driving_range,

            "location": vehicle.location
        }

for id in vm.vehicles:
    print(json.dumps(vm.vehicles[id], cls=VehicleEncoder))
    break