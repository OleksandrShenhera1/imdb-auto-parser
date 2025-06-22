import csv
# Saving data to file => (fileName)
def csvImporter(films, fileName):
    if not films:
        print("(Error) Occurred while trying to import data to csv...")
        return
    
    with open(fileName, mode='w', newline='', encoding='utf-8') as csvfile:
        # Check if dictionary (return true : false)
        if isinstance(films[0], dict):
            # Get names for keys
            fieldnames = films[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writeheader - fieldnames for headers
            writer.writeheader()
            for film in films:
                writer.writerow(film)
        else:
            # If not dictionary
            writer = csv.writer(csvfile)
            for film in films:
                writer.writerow(film)