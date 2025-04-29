
def process_meter_readings():
    # Step 1: Open the file for reading
    with open("meter_readings.txt", "r") as fh:  # Using 'with' ensures automatic closing
        # Step 2: Read all lines
        lines = fh.readlines()  # Correct method name (no fh_readlines)
    
    # Step 3: Process the readings
    readings = [float(line.strip()) for line in lines]  # strip() removes newlines
    average = sum(readings) / len(readings)
    
    print(f"Processed {len(readings)} readings")
    print(f"Calculated average: {average:.2f}")
    
    # Step 5 & 6: Append a new reading
    with open("meter_readings.txt", "a") as fh:  # 'a' for append mode
        new_reading = "190.5"
        fh.write(new_reading + "\n")  # Correct method name (no fh_write)
    
    # Step 8-10: Store the average in a new file
    with open("average_reading.txt", "w") as new_fh:
        new_fh.write(f"{average}\n")  # Simpler than writelines for single value
    
    # Step 11: Verify the average file
    with open("average_reading.txt", "r") as confirm_fh:
        content = confirm_fh.read().strip()  # Read and remove newline
    
    print(f"Average saved to file: {content}")

# Example usage
if __name__ == "__main__":
    # First create a sample file if it doesn't exist
    from pathlib import Path
    if not Path("meter_readings.txt").exists():
        with open("meter_readings.txt", "w") as f:
            f.write("150.5\n162.3\n175.8\n180.2\n")
    
    process_meter_readings()