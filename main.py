from collect_telemetry import collect_telemetry
from run_stress_container import run_stress_container
from save_to_csv import save_to_csv

if __name__ == "__main__":
    utilization_levels = [25, 50, 75, 100]
    
    for utilization in utilization_levels:
        duration = 60  
        interval = 1   
        
        print(f"Starting stress container with {utilization}% utilization...")
        container = run_stress_container(utilization, duration)
        
        print("Collecting telemetry data...")
        telemetry_data = collect_telemetry(duration, interval)
        
        save_to_csv(telemetry_data, f'telemetry_data_{utilization}.csv')
        print(f"Telemetry data saved to telemetry_data_{utilization}.csv")
        
        container.wait()
        print("Stress container finished.")
