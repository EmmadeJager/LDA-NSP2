# code voor het opnemen van frequentie-data vanuit LabView

class Ingest_Data:
    def __init__(self, data_file):
        """Ingest data from labview export

        Args:
            data_file (str): name of the to be ingested file

        Returns:
            tuple: tuple of lists with both columns of the datafile in their own respective lists
        """
        with open(data_file[0], "r") as dataFile:
            data = [line.split() for line in dataFile]
            data.pop(0)
        self.x = []
        self.y = []

        for line in data:
            line = [i.replace(",", ".") for i in line]
            self.x.append(float(line[0]))
            self.y.append(float(line[1]))

    # functie om data terug te geven (x and y value)
    def returndata(self):
        return self.x, self.y

# class om data op te nemen (voor histogrammen)
class Ingest_Data_1D:
    def __init__(self, data_file):
        """Ingest data from labview export

        Args:
            data_file (str): name of the to be ingested file

        Returns:
            tuple: tuple of lists with both columns of the datafile in their own respective lists
        """
        # lees data uit file
        with open(data_file, "r") as dataFile:
            data = [line.split() for line in dataFile]
        
        self.one_d = []

        for line in data:
            line = [i.replace(",", ".") for i in line]
            self.one_d.append(float(line[0]))
            
    # geef gelezen data terug
    def returndata(self):
        return self.one_d
