class Ingest_Data:
    def __init__(self, data_file):
        """Ingest data from labview export

        Args:
            data_file (str): name of the to be ingested file

        Returns:
            tuple: tuple of lists with both columns of the datafile in their own respective lists
        """
        with open(data_file, "r") as dataFile:
            data = [line.split() for line in dataFile]
            data.pop(0)
        self.x = []
        self.y = []

        for line in data:
            line = [i.replace(",", ".") for i in line]
            self.x.append(float(line[0]))
            self.y.append(float(line[1]))

        
    def returndata(self):
        return self.x, self.y
