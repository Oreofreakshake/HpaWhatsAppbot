from jsonpy import JsonSource


data_source = JsonSource("data/data.json")
data = data_source.data
listdata = data["en"]["options"]


class Option:
    def __init__(self, option, throwdata="wrong input"):
        self.option = option
        self.throwdata = throwdata

        indexvalue = [
            "1. Statistics",
            "2. Managing COVID 19",
            "3. Vaccination centers",
            "4. Flu clinics & sample collection centers",
            "5. Domestic travel criteria & islands",
            "6. Islands under monitoring",
            "7. Links and contacts",
            "8. Call 1676",
        ]

        if option == "1":
            self.throwdata = listdata[indexvalue[0]]
        if option == "2":
            self.throwdata = listdata[indexvalue[1]]
        if option == "3":
            self.throwdata = listdata[indexvalue[2]]
        if option == "4":
            self.throwdata = listdata[indexvalue[3]]
        if option == "5":
            self.throwdata = listdata[indexvalue[4]]
        if option == "6":
            self.throwdata = listdata[indexvalue[5]]
        if option == "7":
            self.throwdata = listdata[indexvalue[6]]
        if option == "8":
            self.throwdata = listdata[indexvalue[7]]

