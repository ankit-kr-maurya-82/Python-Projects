import datetime
import json


def load_data():
    try:
        with open('trainTicket.json','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data(tickets):
    with open('trainTicket.json','w') as file:
        json.dump(tickets, file)

def underline(val=70):
    print("-" * val)
    return val

def welcome():
    print("Welcome to the Train Journey Booking System!")

def disDate():
    while True:
        travel_date = input("Travel date (dd-mm-yyyy): ").strip()
        try:
            day, month, year = map(int, travel_date.split('-'))
            datetime.datetime(year, month, day)  # Validate date
            if year == 2025:
                return travel_date
            else:
                print("Invalid date. Year must be 2025.")
        except ValueError:
            print("Invalid format or invalid date. Use dd-mm-yyyy.")

# Converts station code to name
def resolve_station_name(input_val, trains):
    upper_val = input_val.upper()
    for train in trains:
        route_codes = train.get("route_code", {})
        if upper_val in route_codes:
            return route_codes[upper_val]
    return input_val.title()

# Journey input + station resolution
def getJourneyDetails(all_trains):
    print("Please enter your journey details:")

    departure = input("Departure city: ").strip()
    arrival = input("Arrival city: ").strip()

    dep_resolved = resolve_station_name(departure, all_trains)
    arr_resolved = resolve_station_name(arrival, all_trains)

    # The date is now handled outside this function
    return dep_resolved, arr_resolved, None
# get all train from json file
def getAllTrains(date):
    return [
    {
        "train_no": "13240",
        "train_name": "Kota-Patna Express",
        "date": date,
        "route": [
            "Kota",
            "Indargarh Sumerganj Mandi",
            "Sawai Madhopur",
            "Gangapur City",
            "Hindaun City",
            "Bayana",
            "Bharatpur",
            "Mathura",
            "Agra Cantt",
            "Etwah",
            "Rura",
            "Kanpur",
            "Lucknow",
            "Maharaja Bijli Pasi",
            "Sultanpur",
            "Varanasi",
            "Pt. DD Upadhyaya",
            "Zamania",
            "Buxar",
            "Ara",
            "Bihta",
            "Danapur",
            "Patna"
        ],
        "route_code": {
            "KOTA": "Kota",
            "IDG": "Indargarh Sumerganj Mandi",
            "SWM": "Sawai Madhopur",
            "GGC": "Gangapur City",
            "HNDA": "Hindaun City",
            "BXN": "Bayana Junction",
            "BTE": "Bharatpur Junction",
            "MTJ": "Mathura Junction",
            "AGC": "Agra Cantt",
            "ETW": "Etwah",
            "RURA": "Rura",
            "CNB": "Kanpur Central",
            "LKO": "Lucknow",
            "MBPR": "Maharaja Bijli Pasi",
            "SLN": "Sultanpur",
            "BSB": "Varanasi",
            "DDU": "Pt. Deen Dayal Upadhyaya",
            "ZNA": "Zamania",
            "BXR": "Buxar",
            "ARA": "Ara",
            "BTA": "Bihta",
            "DNR": "Danapur",
            "PNBE": "Patna"
        }
    },
    {
        "train_no": "13238",
        "train_name": "Kota-Patna Express",
        "date": date,
        "route": [
            "Kota",
            "Indargarh Sumerganj Mandi",
            "Sawai Madhopur",
            "Narayanpur Tatwara",
            "Gangapur City",
            "Hindaun City",
            "Bayana",
            "Bharatpur",
            "Mathura",
            "Agra Cantt",
            "Etwah",
            "Kanpur",
            "Unnao",
            "Lucknow",
            "Ayodhya Cantt",
            "Ayodhya Dham",
            "Akbarpur",
            "Shahganj",
            "Jaunpur",
            "Varanasi",
            "Pt. DD Upadhyaya",
            "Zamania",
            "Buxar",
            "Dumroan",
            "Ara",
            "Bihta",
            "Danapur",
            "Patna"
        ],
        "route_code": {
            "KOTA": "Kota",
            "IDG": "Indargarh Sumerganj Mandi",
            "SWM": "Sawai Madhopur",
            "NRYN": "Narayanpur Tatwara",
            "GGC": "Gangapur City",
            "HNDA": "Hindaun City",
            "BXN": "Bayana",
            "BTE": "Bharatpur",
            "MTJ": "Mathura",
            "AGC": "Agra Cantt",
            "ETW": "Etwah",
            "CNB": "Kanpur",
            "ON": "Unnao",
            "LKO": "Lucknow",
            "AYC": "Ayodhya Cantt",
            "AY": "Ayodhya Dham",
            "ABP": "Akbarpur",
            "SHG": "Shahganj",
            "JNU": "Jaunpur",
            "BSB": "Varanasi",
            "DDU": "Pt. DD Upadhyaya",
            "ZNA": "Zamania",
            "BXR": "Buxar",
            "DURE": "Dumroan",
            "ARA": "Ara",
            "BTA": "Bihta",
            "DNR": "Danapur",
            "PNBE": "Patna"
        }
    },
    {
        "train_no": "13237",
        "train_name": "Patna-Kota Express",
        "date": date,
        "route": [
            "Patna",
            "Danapur",
            "Bihta",
            "Ara",
            "Dumroan",
            "Buxar",
            "Zamania",
            "Pt. DD Upadhyaya",
            "Varanasi",
            "Jaunpur",
            "Shahganj",
            "Akbarpur",
            "Ayodhya Dham",
            "Ayodhya Cantt",
            "Lucknow",
            "Unnao",
            "Kanpur Central",
            "Etwah",
            "Agra Cantt",
            "Mathura",
            "Bharatpur",
            "Bayana",
            "Hindaun City",
            "Gangapur City",
            "Narayanpur Tatwara",
            "Sawai Madhopur",
            "Indargarh Sumerganj Mandi",
            "Kota"
        ],
        "route_code": {
            "PNBE": "Patna",
            "DNR": "Danapur",
            "BTA": "Bihta",
            "ARA": "Ara",
            "DURE": "Dumroan",
            "BXR": "Buxar",
            "ZNA": "Zamania",
            "DDU": "Pt. DD Upadhyaya",
            "BSB": "Varanasi",
            "JNU": "Jaunpur",
            "SHG": "Shahganj",
            "ABP": "Akbarpur",
            "AY": "Ayodhya Dham",
            "AYC": "Ayodhya Cantt",
            "LKO": "Lucknow",
            "ON": "Unnao",
            "CNB": "Kanpur Central",
            "ETW": "Etwah",
            "AGC": "Agra Cantt",
            "MTJ": "Mathura",
            "BTE": "Bharatpur",
            "BXN": "Bayana",
            "HNDA": "Hindaun City",
            "GGC": "Gangapur City",
            "NRYN": "Narayanpur Tatwara",
            "SWM": "Sawai Madhopur",
            "IDG": "Indargarh Sumerganj Mandi",
            "KOTA": "Kota"
        }
    },
    {
        "train_no": "13239",
        "train_name": "Patna-Kota Express",
        "date": date,
        "route": [
            "Patna",
            "Danapur",
            "Bihta",
            "Ara",
            "Buxar",
            "Zamania",
            "Pt. DD Upadhyaya",
            "Varanasi",
            "Sultanpur",
            "Maharaja Bijli Pasi",
            "Lucknow",
            "Kanpur Central",
            "Rura",
            "Etwah",
            "Agra Cantt",
            "Mathura",
            "Bharatpur",
            "Bayana",
            "Hindaun City",
            "Gangapur City",
            "Sawai Madhopur",
            "Indargarh Sumerganj Mandi",
            "Kota"
        ],
        "route_code": {
            "PNBE": "Patna",
            "DNR": "Danapur",
            "BTA": "Bihta",
            "ARA": "Ara",
            "BXR": "Buxar",
            "ZNA": "Zamania",
            "DDU": "Pt. DD Upadhyaya",
            "BSB": "Varanasi",
            "SLN": "Sultanpur",
            "MBPR": "Maharaja Bijli Pasi",
            "LKO": "Lucknow",
            "CNB": "Kanpur Central",
            "RURA": "Rura",
            "ETW": "Etwah",
            "AGC": "Agra Cantt",
            "MTJ": "Mathura",
            "BTE": "Bharatpur",
            "BXN": "Bayana",
            "HNDA": "Hindaun City",
            "GGC": "Gangapur City",
            "SWM": "Sawai Madhopur",
            "IDG": "Indargarh Sumerganj Mandi",
            "KOTA": "Kota"
        }
    },
    {
        "train_no": "12239",
        "train_name": "Hisar Duronto Express",
        "date": date,
        "route": [
            "Ratlam",
            "Kota",
            "Sawai Madhopur",
            "Jaipur"
        ],
        "route_code": {
            "RTM": "Ratlam",
            "KOTA": "Kota",
            "SWM": "Sawai Madhopur",
            "JP": "Jaipur"
        }
    },
    {
        "train_no": "12465",
        "train_name": "Ranthambhore SF Express",
        "date": date,
        "route": [
            "Dakaniya Talav",
            "Kota",
            "Kapren",
            "Lakheri",
            "Indargarh Sumerganj Mandi",
            "Sawai Madhopur",
            "Chauth ka Barwara",
            "Isarda",
            "Banasthali Niwai",
            "Durgapura",
            "Jaipur"
        ],
        "route_code": {
            "DKAE": "Dakaniya Talav",
            "KOTA": "Kota",
            "KPZ": "Kapren",
            "LKE": "Lakheri",
            "IDG": "Indargarh Sumerganj Mandi",
            "SWM": "Sawai Madhopur",
            "CKB": "Chauth ka Barwara",
            "ISA": "Isarda",
            "BNLW": "Banasthali Niwai",
            "DPA": "Durgapura",
            "JP": "Jaipur"
        }
    },
    {
        "train_no": "22933",
        "train_name": "Jaipur SF Express",
        "date": date,
        "route": [
            "Bandra Terminus",
            "Borivali",
            "Vapi",
            "Surat",
            "Bharuch Jn",
            "Vadodara ",
            "Dahod",
            "Ratlam ",
            "Nagda ",
            "Bhawani Mandi",
            "Ramganj Mandi",
            "Kota",
            "Sawai Madhopur",
            "Durgapura",
            "Jaipur"
        ],
        "route_code": {
            "BDTS": "Bandra Terminus",
            "BVI": "Borivali",
            "VAPI": "Vapi",
            "ST": "Surat",
            "BH": "Bharuch Jn",
            "BRC": "Vadodara",
            "DHD": "Dahod",
            "RTM": "Ratlam",
            "NAD": "Nagda",
            "BWM": "Bhawani Mandi",
            "RMA": "Ramganj Mandi",
            "KOTA": "Kota",
            "SWM": "Sawai Madhopur",
            "DPA": "Durgapura",
            "JP": "Jaipur"
        }
    },
    {
        "train_no": "22935",
        "train_name": "Jaipur SF Express",
        "date": date,
        "route": [
            "Jaipur",
            "Durgapura",
            "Sawai Madhopur",
            "Kota",
            "Ramganj Mandi",
            "Bhawani Mandi",
            "Nagda ",
            "Ratlam ",
            "Dahod",
            "Vadodara ",
            "Bharuch J",
            "Vapi",
            "Surat",
            "Borivali",
            "Bandra Terminus"
        ],
        "route_code": {
            "SWM": "Sawai Madhopur",
            "KOTA": "Kota",
            "RMA": "Ramganj Mandi",
            "BWM": "Bhawani Mandi",
            "NAD": "Nagda",
            "RTM": "Ratlam",
            "DHD": "Dahod",
            "BRC": "Vadodara",
            "BH": "Bharuch Jn",
            "VAPI": "Vapi",
            "ST": "Surat",
            "BVI": "Borivali",
            "BDTS": "Bandra Terminus"
        }
    },
    {
        "train_no": "12955",
        "train_name": "Mumbai Central Jaipur SF Express",
        "date": date,
        "route": [
            "Mumbai Central",
            "Borivali",
            "Vapi",
            "Surat",
            "Ankleshwar",
            "Vadodara",
            "Dahod",
            "Meghnagar",
            "Ratlam",
            "Nagda",
            "Shamgarh",
            "Bhawani Mandi",
            "Ramganj Mandi",
            "Kota",
            "Sawai Madhopur",
            "Gangapur City",
            "Hindaun City",
            "Bayana",
            "Bharatpur",
            "Mathura",
            "Agra Cantt",
            "Gwalior",
            "VGL Jhansi",
            "Bhopal",
            "Itarsi",
            "Nagpur",
            "Balharshah",
            "Warangal",
            "Khammam",
            "Vijayawada",
            "MGR Chennai Central"
        ],
        "route_code": {
            "BCT": "Mumbai Central",
            "BVI": "Borivali",
            "VAPI": "Vapi",
            "ST": "Surat",
            "AKV": "Ankleshwar",
            "BRC": "Vadodara",
            "DHD": "Dahod",
            "MGN": "Meghnagar",
            "RTM": "Ratlam",
            "NAD": "Nagda",
            "SGZ": "Shamgarh",
            "BWM": "Bhawani Mandi",
            "RMA": "Ramganj Mandi",
            "KOTA": "Kota",
            "SWM": "Sawai Madhopur",
            "GGC": "Gangapur City",
            "HNDA": "Hindaun City",
            "BXN": "Bayana",
            "BTE": "Bharatpur",
            "MTJ": "Mathura",
            "AGC": "Agra Cantt",
            "GWL": "Gwalior",
            "VGLB": "Virangana Lakshmibai (Jhansi)",
            "BPL": "Bhopal",
            "ET": "Itarsi",
            "NGP": "Nagpur",
            "BPQ": "Balharshah",
            "WL": "Warangal",
            "KMT": "Khammam",
            "BZA": "Vijayawada",
            "MAS": "MGR Chennai Central"
        }
    },
    {
        "train_no": "67890",
        "train_name": "Kolkata-Delhi Superfast",
        "date": date,
        "route": [
            "Kolkata",
            "Patna",
            "Varanasi",
            "Kanpur Central",
            "Lucknow",
            "Agra Cantt",
            "New Delhi"
        ],
        "route_code": {
            "Kolkata": "Kolkata",
            "PNBE": "Patna",
            "BSB": "Varanasi",
            "CNB": "Kanpur Central",
            "LKO": "Lucknow",
            "AGC": "Agra Cantt",
            "NDLS": "New Delhi"
        }
    },
    {
        "train_no": "12904",
        "train_name": "Golden Temple Mail",
        "date": date,
        "route": [
            "Hazrat Nizamuddin",
            "Faridabad",
            "Mathura",
            "Bharatpur",
            "Bayana",
            "Hindaun City",
            "Shiv Mahaveerji",
            "Gangapur City",
            "Sawai Madhopur",
            "Kota",
            "Ramganj Mandi",
            "Bhawani Mandi",
            "Shamgarh",
            "Nagda",
            "Ratlam",
            "Meghnagar",
            "Dahod",
            "Godhra",
            "Vodadara",
            "Surat",
            "Borivali",
            "Mumbai Central"
        ],
        "route_code": {
            "NZM": "Hazrat Nizamuddin",
            "FDB": "Faridabad",
            "MTJ": "Mathura",
            "BTE": "Bharatpur",
            "BXN": "Bayana",
            "HNDA": "Hindaun City",
            "SMVJ": "Shiv Mahaveerji",
            "GGC": "Gangapur City",
            "SWM": "Sawai Madhopur",
            "KOTA": "Kota",
            "RMA": "Ramganj Mandi",
            "BWM": "Bhawani Mandi",
            "SGZ": "Shamgarh",
            "NAD": "Nagda",
            "RTM": "Ratlam",
            "MGN": "Meghnagar",
            "DHD": "Dahod",
            "GDA": "Godhra",
            "BRC": "Vadodara",
            "ST": "Surat",
            "BVI": "Borivali",
            "BCT": "Mumbai Central"
        }
    },
    {
        "train_no": "12622",
        "train_name": "Tamil Nadu Express",
        "date": date,
        "route": [
            "New Delhi",
            "Agra Cantt",
            "Gwalior",
            "VGL Jhansi",
            "Bhopal",
            "Itarsi",
            "Nagpur",
            "Balharshah",
            "Warangal",
            "Khammam",
            "Vijayawada",
            "MGR Chennai Central"
        ],
        "route_code": {
            "NDLS": "New Delhi",
            "AGC": "Agra Cantt",
            "GWL": "Gwalior",
            "VGLB": "Virangana Lakshmibai (Jhansi)",
            "BPL": "Bhopal",
            "ET": "Itarsi",
            "NGP": "Nagpur",
            "BPQ": "Balharshah",
            "WL": "Warangal",
            "KMT": "Khammam",
            "BZA": "Vijayawada",
            "MAS": "MGR Chennai Central"
        }
    },
    {
        "train_no": "10622",
        "train_name": "Delhi Chennai Rajdhani Express",
        "date": date,
        "route": [
            "New Delhi",
            "Jaipur",
            "Kota",
            "Surat",
            "Mumbai ",
            "Nagpur",
            "Balharshah",
            "Warangal",
            "Khammam",
            "Vijayawada",
            "MGR Chennai Central"
        ],
        "route_code": {
            "NDLS": "New Delhi",
            "JP": "Jaipur",
            "KOTA": "Kota",
            "ST": "Surat",
            "BCT": "Mumbai Central",
            "NGP": "Nagpur",
            "BPQ": "Balharshah",
            "WL": "Warangal",
            "KMT": "Khammam",
            "BZA": "Vijayawada",
            "MAS": "MGR Chennai Central"
        }
    },
    {
        "train_no": "12424",
        "train_name": " Dibrugarh Rajdhani Express",
        "date": date,
        "route": [
            "New Delhi",
            "Jaunpur Central",
            "Prayagraj",
            "Pt.DD Upadhyaya",
            "Danapur",
            "Patliputra",
            "Barauni",
            "Mansi",
            "Naugachia",
            "Katihar",
            "KishanGanj",
            "New Jalpaiguri",
            "New Cooch Behar",
            "Kokrajhar",
            "New Bongaigaon",
            "Rangia",
            "Guwahati",
            "Chaparmukh",
            "Lumding",
            "Dimapur",
            "Mariani",
            "New Tinsukia",
            "Dibrugarh"
        ],
        "route_code": {
            "NDLS": "New Delhi",
            "JNU": "Jaunpur Junction",
            "PRYJ": "Prayagraj",
            "DDU": "Pt. Deen Dayal Upadhyaya",
            "DNR": "Danapur",
            "PPTA": "Patliputra",
            "BJU": "Barauni",
            "MNE": "Mansi",
            "NNA": "Naugachia",
            "KIR": "Katihar",
            "KNE": "Kishanganj",
            "NJP": "New Jalpaiguri",
            "NCB": "New Cooch Behar",
            "KOJ": "Kokrajhar",
            "NBQ": "New Bongaigaon",
            "RNY": "Rangia",
            "GHY": "Guwahati",
            "CPK": "Chaparmukh",
            "LMG": "Lumding",
            "DMV": "Dimapur",
            "MXN": "Mariani",
            "NTSK": "New Tinsukia",
            "DBRG": "Dibrugarh"
        }
    },
    {
        "train_no": "20506",
        "train_name": " Dibrugarh Rajdhani Express",
        "date": date,
        "route": [
            "New Delhi",
            "Moradabad",
            "Bareilly",
            "Lucknow",
            "Varanasi",
            "Ballia",
            "Chhapra",
            "Hajipur",
            "Barauni",
            "Begusarai",
            "Katihar",
            "KishanGanj",
            "New Jalpaiguri",
            "New Cooch Behar",
            "New Alipurduar",
            "Kokrajhar",
            "New Bongaigaon",
            "Rangia",
            "Tangla",
            "Udalguri",
            "New Missamari",
            "Rangapara North",
            "Harmuti",
            "North Lakhimpur",
            "Dibrugarh"
        ],
        "route_code": {
            "NDLS": "New Delhi",
            "MB": "Moradabad",
            "BE": "Bareilly",
            "LKO": "Lucknow",
            "BSB": "Varanasi",
            "BUI": "Ballia",
            "CPR": "Chhapra",
            "HJP": "Hajipur",
            "BJU": "Barauni",
            "BGS": "Begusarai",
            "KIR": "Katihar",
            "KNE": "Kishanganj",
            "NJP": "New Jalpaiguri",
            "NCB": "New Cooch Behar",
            "NOQ": "New Alipurduar",
            "KOJ": "Kokrajhar",
            "NBQ": "New Bongaigaon",
            "RNY": "Rangia",
            "TNL": "Tangla",
            "ULG": "Udalguri",
            "NMM": "New Missamari",
            "RPAN": "Rangapara North",
            "HMY": "Harmuti",
            "NLP": "North Lakhimpur",
            "DBRG": "Dibrugarh"
        }
    },
    {
        "train_no": "20503",
        "train_name": " New Delhi Rajdhani Express",
        "date": date,
        "route": [
            "Dibrugarh",
            "North Lakhimpur",
            "Harmuti",
            "Rangapara North",
            "New Missamari",
            "Udalguri",
            "Tangla",
            "Rangia",
            "New Bongaigaon",
            "Kokrajhar",
            "New Alipurduar",
            "New Cooch Behar",
            "New Jalpaiguri",
            "KishanGanj",
            "Katihar",
            "Begusarai",
            "Barauni",
            "Hajipur",
            "Chhapra",
            "Ballia",
            "Varanasi",
            "Lucknow",
            "Bareilly",
            "Moradabad",
            "New Delhi"
        ],
        "route_code": {
            "DBRG": "Dibrugarh",
            "NLP": "North Lakhimpur",
            "HMY": "Harmuti",
            "RPAN": "Rangapara North",
            "NMM": "New Missamari",
            "ULG": "Udalguri",
            "TNL": "Tangla",
            "RNY": "Rangia",
            "NBQ": "New Bongaigaon",
            "KOJ": "Kokrajhar",
            "NOQ": "New Alipurduar",
            "NCB": "New Cooch Behar",
            "NJP": "New Jalpaiguri",
            "KNE": "Kishanganj",
            "KIR": "Katihar",
            "BGS": "Begusarai",
            "BJU": "Barauni",
            "HJP": "Hajipur",
            "CPR": "Chhapra",
            "BUI": "Ballia",
            "BSB": "Varanasi",
            "LKO": "Lucknow",
            "BE": "Bareilly",
            "MB": "Moradabad",
            "NDLS": "New Delhi"
        }
    },
    {
        "train_no": "10324",
        "train_name": " Dibrugarh Rajdhani Express",
        "date": date,
        "route": [
            "Dibrugarh",
            "Dimapur",
            "Rangia",
            "Guwahati",
            "Patna",
            "Buxar",
            "Varansi",
            "Jaunpur Central",
            "Sultanpur",
            "Lucknow",
            "Agra Cantt",
            "Mathura",
            "New Delhi"
        ],
        "route_code": {
            "DBRG": "Dibrugarh",
            "DMV": "Dimapur",
            "RNY": "Rangia",
            "GHY": "Guwahati",
            "PNBE": "Patna",
            "BXR": "Buxar",
            "BSB": "Varanasi",
            "JNU": "Jaunpur Junction",
            "SLN": "Sultanpur",
            "LKO": "Lucknow",
            "AGC": "Agra Cantt",
            "MTJ": "Mathura",
            "NDLS": "New Delhi"
        }
    },
    {
        "train_no": "10623",
        "train_name": "Delhi Rajdhani Express",
        "date": date,
        "route": [
            "Chennai",
            "Vijayawada",
            "Khammam",
            "Warangal",
            "Balharshah",
            "Nagpur",
            "Mumbai ",
            "Surat",
            "Kota",
            "Jaipur",
            "New Delhi"
        ],
        "route_code": {
            "MAS": "Chennai Central",
            "BZA": "Vijayawada",
            "KMT": "Khammam",
            "WL": "Warangal",
            "BPQ": "Balharshah",
            "NGP": "Nagpur",
            "BCT": "Mumbai Central",
            "ST": "Surat",
            "KOTA": "Kota",
            "JP": "Jaipur",
            "NDLS": "New Delhi"
        },
        "KMT": "Khammam",
        "WL": "Warangal",
        "BPQ": "Balharshah",
        "NGP": "Nagpur",
        "BCT": "Mumbai Central",
        "ST": "Surat",
        "KOTA": "Kota",
        "JP": "Jaipur",
        "NDLS": "New Delhi"
    },
    {
        "train_no": "15667",
        "train_name": "Kamakhya Express",
        "date": date,
        "route": [
            "Kota",
            "Sawai Madhopur",
            "Bayana",
            "Agra Fort",
            "Tundla",
            "Kanpur",
            "Lucknow ",
            "Ayodhya Cantt",
            "Varanasi",
            "Pt. DD Upadhyaya",
            "Buxar",
            "Ara",
            "Patna",
            "New Barauni",
            "Begusarai",
            "Khagaria",
            "Katihar",
            "New Jalpaiguri"
        ],
        "route_code": {
            "KOTA": "Kota",
            "SWM": "Sawai Madhopur",
            "BXN": "Bayana",
            "AF": "Agra Fort",
            "TDL": "Tundla",
            "CNB": "Kanpur Central",
            "LKO": "Lucknow",
            "AYC": "Ayodhya Cantt",
            "BSB": "Varanasi",
            "DDU": "Pt. Deen Dayal Upadhyaya",
            "BXR": "Buxar",
            "ARA": "Ara",
            "PNBE": "Patna",
            "NBJU": "New Barauni",
            "BGS": "Begusarai",
            "KGG": "Khagaria",
            "KIR": "Katihar",
            "NJP": "New Jalpaiguri"
        }
    },
    {
        "train_no": "15635",
        "train_name": "Guwahati Dwarka Express",
        "date": date,
        "route": [
            "Okha",
            "Dwarka",
            "Khambhalia",
            "Jamnagar",
            "Hapa",
            "Rajkot",
            "Surendranagar",
            "Viramgam",
            "Ahmedabad",
            "Nadiad",
            "Chhayapuri",
            "Ratlam",
            "Nagda",
            "Bhawani Mandi",
            "Kota",
            "Sawai Madhopur",
            "Gangapur City",
            "Bayana",
            "Agra Fort",
            "Tundla",
            "Kanpur",
            "Lucknow ",
            "Ayodhya Cantt",
            "Akbarpur",
            "Varanasi",
            "Pt. DD Upadhyaya",
            "Buxar",
            "Patna",
            "New Barauni",
            "Begusarai",
            "Khagaria",
            "Katihar",
            "New Jalpaiguri"
        ],
        "route_code": {
            "OKHA": "Okha",
            "DWK": "Dwarka",
            "KMBL": "Khambhalia",
            "JAM": "Jamnagar",
            "HAPA": "Hapa",
            "RJT": "Rajkot",
            "SUNR": "Surendranagar",
            "VG": "Viramgam",
            "ADI": "Ahmedabad",
            "ND": "Nadiad",
            "CYI": "Chhayapuri",
            "RTM": "Ratlam",
            "NAD": "Nagda",
            "BWM": "Bhawani Mandi",
            "KOTA": "Kota",
            "SWM": "Sawai Madhopur",
            "GGC": "Gangapur City",
            "BXN": "Bayana",
            "AF": "Agra Fort",
            "TDL": "Tundla",
            "CNB": "Kanpur Central",
            "LKO": "Lucknow",
            "AYC": "Ayodhya Cantt",
            "ABP": "Akbarpur",
            "BSB": "Varanasi",
            "DDU": "Pt. DD Upadhyaya",
            "BXR": "Buxar",
            "PNBE": "Patna",
            "NBJU": "New Barauni",
            "BGS": "Begusarai",
            "KGG": "Khagaria",
            "KIR": "Katihar",
            "NJP": "New Jalpaiguri"
        }
    },
    {
        "train_no": "22436",
        "train_name": "Varanasi Vande Bharat Express",
        "date": date,
        "route": [
            "New Delhi",
            "Kanpur Central",
            "Prayagraj ",
            "Varanasi "
        ],
        "route_code": {
            "NDLS": "New Delhi",
            "CNB": "Kanpur Central",
            "PRYJ": "Prayagraj",
            "BSB": "Varanasi"
        }
    },
    {
        "train_no": "22437",
        "train_name": "Varanasi Vande Bharat Express",
        "date": date,
        "route": [
            "Varanasi",
            "Prayagraj ",
            "Kanpur Central",
            "New Delhi"
        ],
        "route_code": {
            "BSB": "Varanasi",
            "PRYJ": "Prayagraj",
            "CNB": "Kanpur Central",
            "NDLS": "New Delhi"
        }
    },
    {
        "train_no": "22438",
        "train_name": "Patna Vande Bharat Express",
        "date": date,
        "route": [
            "New Delhi",
            "Patna"
        ],
        "route_code": {
            "NDLS": "New Delhi",
            "PNBE": "Patna"
        }
    },
    {
        "train_no": "22439",
        "train_name": "Patna Vande Bharat Express",
        "date": date,
        "route": [
            "Patna",
            "New Delhi"
        ],
        "route_code": {
            "PNBE": "Patna",
            "NDLS": "New Delhi"
        }
    }
]
# get train schedule based on departure, arrival, and date
# Returns a list of trains that match the criteria

def get_train_schedule(departure, arrival, date):
    available_trains = []
    train_schedule = getAllTrains(date)
    trains = [train for train in train_schedule if train["date"] == date]
    for train in trains:
        # Build sets for easier matching
        route_names = set(train["route"])
        code_to_name = train["route_code"]
        name_to_code = {v: k for k, v in code_to_name.items()}

        # Normalize input: allow user to enter code or name
        dep_name = departure
        arr_name = arrival
        # If input is a code, convert to name
        if departure.upper() in code_to_name:
            dep_name = code_to_name[departure.upper()]
        if arrival.upper() in code_to_name:
            arr_name = code_to_name[arrival.upper()]

        # If input is a name but not in route, try to convert to code and back
        if dep_name not in route_names and departure.title() in name_to_code:
            dep_name = departure.title()
        if arr_name not in route_names and arrival.title() in name_to_code:
            arr_name = arrival.title()

        # Now check if both stations are in the route and in correct order
        if dep_name in train["route"] and arr_name in train["route"]:
            dep_index = train["route"].index(dep_name)
            arr_index = train["route"].index(arr_name)
            if dep_index < arr_index:
                available_trains.append(train)

    return available_trains

def display_available_trains(trains, source, destination):
    if trains:
        print(f"\nAvailable Trains from {source} to {destination}:")
        for idx, train in enumerate(trains, 1):
            print(f"{idx}. {train['train_name']} ({train['train_no']})")
    else:
        print(f"No trains found from {source} to {destination}.")

def select_train(trains):
    if not trains:
        return None
    while True:
        choice = input("Select a serial number: ").strip()
        for idx, train in enumerate(trains, 1):
            if choice == str(idx):
                print(f"Selected: {train['train_name']} ({train['train_no']})")
                print("Route:" + " → ".join(train["route"]))
                return train
        print("Invalid selection. Try again.")

def get_no_of_passenger():
    while True:
        try:
            num = int(input("Enter number of passengers: "))
            if num > 0:
                return num
            print("Must be at least 1.")
        except ValueError:
            print("Invalid number.")

def get_passenger_details(count):
    passengers = []
    for i in range(count):
        print(f"\nPassenger {i+1}:")
        first = input("First name: ")
        last = input("Last name: ")
        full = f"{first} {last}"
        while True:
            try:
                age = int(input("Age: "))
                if age > 0:
                    break
                print("Age must be positive.")
            except ValueError:
                print("Invalid age.")
        while True:
            g = input("Gender (m/f): ").lower()
            if g in ['m', 'male']:
                gender = "Male"
                break
            elif g in ['f', 'female']:
                gender = "Female"
                break
            print("Invalid gender.")
        passengers.append({"name": full, "age": age, "gender": gender})
    return passengers

def travel_class_menu():
    print("Travel coach options:")
    print("1. Sleeper")
    print("2. AC")
    print("3. General")

# Function to display travel class options
def travel_class():
    print("class options:")
    print("1. first class")
    print("2. second class")
    print("3. third class")



def assign_seats_and_fares(passengers):
    travel_class_menu()
    while True:
        class_input = input("Choose class (1/2/3): ")
        if class_input == "1":
            coach = input("Coach (S1-S6): ").upper()
            seat_range = (1, 72)
            fare = 500
            break
        elif class_input == "2":
            coach_type = input("AC Type (A/B/H): ").upper()
            if coach_type == "A":
                coach = input("Coach (A1-A2): ").upper()
                seat_range = (1, 32)
                fare = 3500
            elif coach_type == "B":
                coach = input("Coach (B1-B5): ").upper()
                seat_range = (1, 72)
                fare = 3200
            elif coach_type == "H":
                coach = "H1"
                seat_range = (1, 24)
                fare = 5800
            else:
                print("Invalid type.")
                continue
            break
        elif class_input == "3":
            coach = input("Coach (G1-G2): ").upper()
            seat_range = (1, 72)
            fare = 50
            break
        else:
            print("Invalid option.")

    valid_coaches = [f"S{i}" for i in range(1, 7)] + [f"A{i}" for i in range(1, 3)] + \
                    [f"B{i}" for i in range(1, 6)] + ["H1"] + [f"G{i}" for i in range(1, 3)]

    if coach not in valid_coaches:
        print("Invalid coach selection.")
        return passengers

    print(f"Selected Coach: {coach} | Fare: ₹{fare} | Seat Range: {seat_range[0]}-{seat_range[1]}")
    print("Assigning seats and fares:")

    child_free_given = False
    assigned_seats = set()

    for p in passengers:
        if p["age"] <= 10:
            if not child_free_given:
                p["fare"] = 0
                p["seat_no"] = "N/A"
                p["coach"] = "N/A"
                child_free_given = True
                print(f"{p['name']} gets free travel (first child under 10).")
                continue
            else:
                print(f"{p['name']} (additional child under 10) gets 1/4 fare and seat assignment.")

        while True:
            seat = input(f"Seat for {p['name']} ({seat_range[0]}-{seat_range[1]}): ")
            if seat.isdigit() and seat_range[0] <= int(seat) <= seat_range[1]:
                seat_num = int(seat)
                if seat_num in assigned_seats:
                    print("Seat already assigned. Choose another seat.")
                    continue
                p["seat_no"] = seat_num
                p["coach"] = coach
                assigned_seats.add(seat_num)
                if p["gender"] == "Male" and p["age"] >= 65:
                    p["fare"] = int(fare * 0.4)
                elif p["gender"] == "Female" and p["age"] >= 60:
                    p["fare"] = int(fare * 0.3)
                elif 11 <= p["age"] < 18:
                    p["fare"] = int(fare / 2)
                elif p["age"] <= 10:
                    p["fare"] = int(fare / 4)
                else:
                    p["fare"] = fare
                break
            else:
                print("Invalid seat.")
    return passengers


def Eop():
    print("============= END OF PROGRAM ====================")


def trainJourney():
    welcome()
    
    underline(45)

    # Get travel date ONCE
    date = disDate()
    all_trains = getAllTrains(date)

    # Then get station input
    departure, arrival, _ = getJourneyDetails(all_trains)
    trains = get_train_schedule(departure, arrival, date)

    underline(40)
    display_available_trains(trains, departure, arrival)
    underline()
    selected_train = select_train(trains)
    if not selected_train:
        print("No valid train selected.")
        return []
    underline()
    count = get_no_of_passenger()
    passengers = get_passenger_details(count)
    underline()
    print("\nPassenger Info:")
    for p in passengers:
        print(f"{p['name']} | Age: {p['age']} | Gender: {p['gender']}")

    passengers = assign_seats_and_fares(passengers)

    # Add journey and train info to each passenger for later use
    for p in passengers:
        p.setdefault("coach", "N/A")
        p.setdefault("seat_no", "N/A")
        p["destination"] = arrival
        p["date"] = date
        p["train_name"] = selected_train['train_name']
        p["train_no"] = selected_train['train_no']

    underline()
    print("Final Ticket:")
    # Ensure all passengers have a numeric fare
    for p in passengers:
        if "fare" not in p or not isinstance(p["fare"], (int, float)):
            p["fare"] = 0
        print(f"{p['name']} | Age: {p['age']} | Coach: {p['coach']} | Seat: {p['seat_no']} | Fare: ₹{p['fare']} | destination: {arrival} | date: {date} | train: {selected_train['train_name']} ({selected_train['train_no']})")
    total = sum(p["fare"] for p in passengers if isinstance(p["fare"], (int, float)))
    tax = total * 0.02
    sum_total = total + tax
    underline()
    print(f"\nTrain: {selected_train['train_name']} ({selected_train['train_no']})")
    print(f"From: {departure} → {arrival} on {date}")
    print("Total fare:", total)
    print("Tax:", round(tax, 2))
    print(f"Total Fare (with 2% tax): ₹{round(sum_total, 2)}")
    underline()

    import os
    if os.path.exists("trainTicket.txt"):
        with open("trainTicket.txt", "r") as trainTicketFile:
            print(trainTicketFile.read())
    else:
        print("trainTicket.txt not found. Skipping file display.")

    # select a passenger for booking cancel per passenger
    if not confirm_booking(passengers):
        print("Booking cancelled. No tickets booked.")
        Eop()
        return []

    print("Thank you for using our service!")
    Eop()
    return passengers

def select_passenger_for_cancel(passengers, date, selected_train, arrival):
    print("\nSelect a passenger to cancel booking:")
    for idx, p in enumerate(passengers, 1):
        print(f" {idx}. {p['name']} | Age: {p['age']} | Coach: {p['coach']} | Seat: {p['seat_no']} | Fare: ₹{p['fare']} | destination: {arrival} | date: {date} | train: {selected_train['train_name']} ({selected_train['train_no']})")
    while True:
        try:
            choice = int(input("Enter the serial number of the passenger to cancel: "))
            if 1 <= choice <= len(passengers):
                return passengers[choice - 1]
            print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def list_of_passenger(passengers):
    if not passengers:
        print("No passengers booked yet.")
        return
    print("\nList of Booked Passengers:")
    for idx, p in enumerate(passengers, 1):
        print(f"{idx}. {p['name']} | Age: {p['age']} | Coach: {p.get('coach', 'N/A')} | Seat: {p.get('seat_no', 'N/A')} | Fare: ₹{p.get('fare', 0)} | destination: {p.get('destination', '')} | date: {p.get('date', '')} | train: {p.get('train_name', '')} ({p.get('train_no', '')})")

def confirm_booking(passengers):
    print("1 => Ticket Book")
    print("2 => Exit")
    try:
        ticket_booking = int(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

    if ticket_booking == 1:
        save_data(passengers)
        print("Ticket Booked")
        return True
    elif ticket_booking == 2:
        print("Exit the program.")
        Eop()
        return False
    else:
        print("Invalid choice. Booking Cancelled.")
        return False
    
def show_ticket_and_payment(passengers):
    if not passengers:
        print("No passengers booked yet.")
        return
def show_ticket_and_payment(passengers):
    if not passengers:
        print("No passengers booked yet.")
        return
    print("\nSelect a passenger to view ticket and payment details:")
    for idx, p in enumerate(passengers, 1):
        print(f"{idx}. {p['name']} | Age: {p['age']} | Coach: {p.get('coach', 'N/A')} | Seat: {p.get('seat_no', 'N/A')} | Fare: ₹{p.get('fare', 0)} | destination: {p.get('destination', '')} | date: {p.get('date', '')} | train: {p.get('train_name', '')} ({p.get('train_no', '')})")
    try:
        choice = int(input("Enter the serial number of the passenger to view details: "))
        if 1 <= choice <= len(passengers):
            p = passengers[choice - 1]
            underline()
            print(f"Ticket for {p['name']}:")
            print(f"Age: {p['age']} | Coach: {p.get('coach', 'N/A')} | Seat: {p.get('seat_no', 'N/A')} | Fare: ₹{p.get('fare', 0)}")
            print(f"Destination: {p.get('destination', '')} | Date: {p.get('date', '')} | Train: {p.get('train_name', '')} ({p.get('train_no', '')})")
            underline() 
            print("Payment Details:")
            total = p.get('fare', 0)
            tax = total * 0.02
            sum_total = total + tax
            print(f"Total fare: ₹{total}")
            print(f"Tax (2%): ₹{round(tax, 2)}")
            print(f"Total Fare (with tax): ₹{round(sum_total, 2)}")
            underline()
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    passengers = load_data()
    while True:
        print("1. Ticket Booking")
        print("2. List of Ticket Booking")
        print("3. Show a Ticket and Payment details")
        print("4. Cancel a Ticket Booked")
        print("5. Exit")
        try:
            user_choice = int(input("Enter the choice number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        underline(40)
        if user_choice == 1:
            # Book ticket and save to file
            new_passengers = trainJourney()
            if new_passengers:
                passengers = new_passengers
                save_data(passengers)
        elif user_choice == 2:
            list_of_passenger(passengers)
        elif user_choice == 3:
            show_ticket_and_payment(passengers)
        elif user_choice == 4:
            # Cancel a ticket
            if not passengers:
                print("No passengers booked yet.")
            else:
                print("\nSelect a passenger to cancel booking:")
                for idx, p in enumerate(passengers, 1):
                    print(f"{idx}. {p['name']} | Age: {p['age']} | Coach: {p.get('coach', 'N/A')} | Seat: {p.get('seat_no', 'N/A')} | Fare: ₹{p.get('fare', 0)} | destination: {p.get('destination', '')} | date: {p.get('date', '')} | train: {p.get('train_name', '')} ({p.get('train_no', '')})")
                try:
                    choice = int(input("Enter the serial number of the passenger to cancel: "))
                    if 1 <= choice <= len(passengers):
                        cancelled = passengers.pop(choice - 1)
                        save_data(passengers)
                        print(f"Cancelled booking for {cancelled['name']}.")
                        print("Return fare")
                        print("0 => today")
                        print("1 => yesterday")
                        print("2 => 2 days")
                        print("3 => 3 days")
                        print("4 => 4 days")
                        print("5 => 5 days")
                        try:
                            day = int(input("enter number of days after booking: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue
                        fare = cancelled.get("fare", 0)
                        if day == 0:
                            print("refund 100%: ", fare)
                        elif day == 1:
                            print("refund 75%: ", fare * 0.75)
                        elif day == 2:
                            print("refund 50%: ", fare * 0.5)
                        elif day == 3:
                            print("refund 25%: ", fare * 0.25)
                        elif day == 4:
                            print("refund 5%: ", fare * 0.05)
                        elif day == 5:
                            print("refund 0%: ", 0)
                        else:
                            print("Invalid day selection.")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif user_choice == 5:
            print("Exit the program.")
            Eop()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


