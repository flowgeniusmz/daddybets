import streamlit as st
from enum import Enum

class Regions_simple(Enum):
    AL = "Alabama"
    AK = "Alaska"
    AS = "American Samoa"
    AZ = "Arizona"
    AR = "Arkansas"
    AA = "Armed Forces - Americas"
    AE = "Armed Forces - Europe"
    AP = "Armed Forces - Pacific"
    CA = "California"
    CO = "Colorado"
    CT = "Connecticut"
    DE = "Delaware"
    DC = "District of Columbia"
    FM = "Federated States of Micronesia"
    FL = "Florida"
    GA = "Georgia"
    GU = "Guam"
    HI = "Hawaii"
    ID = "Idaho"
    IL = "Illinois"
    IN = "Indiana"
    IA = "Iowa"
    KS = "Kansas"
    KY = "Kentucky"
    LA = "Louisiana"
    ME = "Maine"
    MH = "Marshall Islands"
    MD = "Maryland"
    MA = "Massachusetts"
    MI = "Michigan"
    MN = "Minnesota"
    MS = "Mississippi"
    MO = "Missouri"
    MT = "Montana"
    NE = "Nebraska"
    NV = "Nevada"
    NH = "New Hampshire"
    NJ = "New Jersey"
    NM = "New Mexico"
    NY = "New York"
    NC = "North Carolina"
    ND = "North Dakota"
    MP = "Northern Mariana Islands"
    OH = "Ohio"
    OK = "Oklahoma"
    OR = "Oregon"
    PW = "Palau"
    PA = "Pennsylvania"
    PR = "Puerto Rico"
    RI = "Rhode Island"
    SC = "South Carolina"
    SD = "South Dakota"
    TN = "Tennessee"
    TX = "Texas"
    UT = "Utah"
    VT = "Vermont"
    VI = "Virgin Islands"
    VA = "Virginia"
    WA = "Washington"
    WV = "West Virginia"
    WI = "Wisconsin"
    WY = "Wyoming"

class Region(Enum):
    AL = {'countryCode': 'US', 'regionCode': 'AL', 'isoRegionCode': 'US-AL', 'name': 'Alabama', 'URLValue': 'US-AL-SB'}
    AK = {'countryCode': 'US', 'regionCode': 'AK', 'isoRegionCode': 'US-AK', 'name': 'Alaska', 'URLValue': 'US-AK-SB'}
    AS = {'countryCode': 'US', 'regionCode': 'AS', 'isoRegionCode': 'US-AS', 'name': 'American Samoa', 'URLValue': 'US-AS-SB'}
    AZ = {'countryCode': 'US', 'regionCode': 'AZ', 'isoRegionCode': 'US-AZ', 'name': 'Arizona', 'URLValue': 'US-AZ-SB'}
    AR = {'countryCode': 'US', 'regionCode': 'AR', 'isoRegionCode': 'US-AR', 'name': 'Arkansas', 'URLValue': 'US-AR-SB'}
    AA = {'countryCode': 'US', 'regionCode': 'AA', 'isoRegionCode': 'US-AA', 'name': 'Armed Forces - Americas', 'URLValue': 'US-AA-SB'}
    AE = {'countryCode': 'US', 'regionCode': 'AE', 'isoRegionCode': 'US-AE', 'name': 'Armed Forces - Europe', 'URLValue': 'US-AE-SB'}
    AP = {'countryCode': 'US', 'regionCode': 'AP', 'isoRegionCode': 'US-AP', 'name': 'Armed Forces - Pacific', 'URLValue': 'US-AP-SB'}
    CA = {'countryCode': 'US', 'regionCode': 'CA', 'isoRegionCode': 'US-CA', 'name': 'California', 'URLValue': 'US-CA-SB'}
    CO = {'countryCode': 'US', 'regionCode': 'CO', 'isoRegionCode': 'US-CO', 'name': 'Colorado', 'URLValue': 'US-CO-SB'}
    CT = {'countryCode': 'US', 'regionCode': 'CT', 'isoRegionCode': 'US-CT', 'name': 'Connecticut', 'URLValue': 'US-CT-SB'}
    DE = {'countryCode': 'US', 'regionCode': 'DE', 'isoRegionCode': 'US-DE', 'name': 'Deleware', 'URLValue': 'US-DE-SB'}
    DC = {'countryCode': 'US', 'regionCode': 'DC', 'isoRegionCode': 'US-DC', 'name': 'District of Columbia', 'URLValue': 'US-DC-SB'}
    FM = {'countryCode': 'US', 'regionCode': 'FM', 'isoRegionCode': 'US-FM', 'name': 'Federated States of Micronesia', 'URLValue': 'US-FM-SB'}
    FL = {'countryCode': 'US', 'regionCode': 'FL', 'isoRegionCode': 'US-FL', 'name': 'Florida', 'URLValue': 'US-FL-SB'}
    GA = {'countryCode': 'US', 'regionCode': 'GA', 'isoRegionCode': 'US-GA', 'name': 'Georgia', 'URLValue': 'US-GA-SB'}
    GU = {'countryCode': 'US', 'regionCode': 'GU', 'isoRegionCode': 'US-GU', 'name': 'Guam', 'URLValue': 'US-GU-SB'}
    HI = {'countryCode': 'US', 'regionCode': 'HI', 'isoRegionCode': 'US-HI', 'name': 'Hawaii', 'URLValue': 'US-HI-SB'}
    ID = {'countryCode': 'US', 'regionCode': 'ID', 'isoRegionCode': 'US-ID', 'name': 'Idaho', 'URLValue': 'US-ID-SB'}
    IL = {'countryCode': 'US', 'regionCode': 'IL', 'isoRegionCode': 'US-IL', 'name': 'Illinois', 'URLValue': 'US-IL-SB'}
    IN = {'countryCode': 'US', 'regionCode': 'IN', 'isoRegionCode': 'US-IN', 'name': 'Indiana', 'URLValue': 'US-IN-SB'}
    IA = {'countryCode': 'US', 'regionCode': 'IA', 'isoRegionCode': 'US-IA', 'name': 'Iowa', 'URLValue': 'US-IA-SB'}
    KS = {'countryCode': 'US', 'regionCode': 'KS', 'isoRegionCode': 'US-KS', 'name': 'Kansas', 'URLValue': 'US-KS-SB'}
    KY = {'countryCode': 'US', 'regionCode': 'KY', 'isoRegionCode': 'US-KY', 'name': 'Kentucky', 'URLValue': 'US-KY-SB'}
    LA = {'countryCode': 'US', 'regionCode': 'LA', 'isoRegionCode': 'US-LA', 'name': 'Louisiana', 'URLValue': 'US-LA-SB'}
    ME = {'countryCode': 'US', 'regionCode': 'ME', 'isoRegionCode': 'US-ME', 'name': 'Maine', 'URLValue': 'US-ME-SB'}
    MH = {'countryCode': 'US', 'regionCode': 'MH', 'isoRegionCode': 'US-MH', 'name': 'Marshall Islands', 'URLValue': 'US-MH-SB'}
    MD = {'countryCode': 'US', 'regionCode': 'MD', 'isoRegionCode': 'US-MD', 'name': 'Maryland', 'URLValue': 'US-MD-SB'}
    MA = {'countryCode': 'US', 'regionCode': 'MA', 'isoRegionCode': 'US-MA', 'name': 'Massachusetts', 'URLValue': 'US-MA-SB'}
    MI = {'countryCode': 'US', 'regionCode': 'MI', 'isoRegionCode': 'US-MI', 'name': 'Michigan', 'URLValue': 'US-MI-SB'}
    MN = {'countryCode': 'US', 'regionCode': 'MN', 'isoRegionCode': 'US-MN', 'name': 'Minnesota', 'URLValue': 'US-MN-SB'}
    MS = {'countryCode': 'US', 'regionCode': 'MS', 'isoRegionCode': 'US-MS', 'name': 'Mississippi', 'URLValue': 'US-MS-SB'}
    MO = {'countryCode': 'US', 'regionCode': 'MO', 'isoRegionCode': 'US-MO', 'name': 'Missouri', 'URLValue': 'US-MO-SB'}
    MT = {'countryCode': 'US', 'regionCode': 'MT', 'isoRegionCode': 'US-MT', 'name': 'Montana', 'URLValue': 'US-MT-SB'}
    NE = {'countryCode': 'US', 'regionCode': 'NE', 'isoRegionCode': 'US-NE', 'name': 'Nebraska', 'URLValue': 'US-NE-SB'}
    NV = {'countryCode': 'US', 'regionCode': 'NV', 'isoRegionCode': 'US-NV', 'name': 'Nevada', 'URLValue': 'US-NV-SB'}
    NH = {'countryCode': 'US', 'regionCode': 'NH', 'isoRegionCode': 'US-NH', 'name': 'New Hampshire', 'URLValue': 'US-NH-SB'}
    NJ = {'countryCode': 'US', 'regionCode': 'NJ', 'isoRegionCode': 'US-NJ', 'name': 'New Jersey', 'URLValue': 'US-NJ-SB'}
    NM = {'countryCode': 'US', 'regionCode': 'NM', 'isoRegionCode': 'US-NM', 'name': 'New Mexico', 'URLValue': 'US-NM-SB'}
    NY = {'countryCode': 'US', 'regionCode': 'NY', 'isoRegionCode': 'US-NY', 'name': 'New York', 'URLValue': 'US-NY-SB'}
    NC = {'countryCode': 'US', 'regionCode': 'NC', 'isoRegionCode': 'US-NC', 'name': 'North Carolina', 'URLValue': 'US-NC-SB'}
    ND = {'countryCode': 'US', 'regionCode': 'ND', 'isoRegionCode': 'US-ND', 'name': 'North Dakota', 'URLValue': 'US-ND-SB'}
    MP = {'countryCode': 'US', 'regionCode': 'MP', 'isoRegionCode': 'US-MP', 'name': 'Northern Mariana Islands', 'URLValue': 'US-MP-SB'}
    OH = {'countryCode': 'US', 'regionCode': 'OH', 'isoRegionCode': 'US-OH', 'name': 'Ohio', 'URLValue': 'US-OH-SB'}
    OK = {'countryCode': 'US', 'regionCode': 'OK', 'isoRegionCode': 'US-OK', 'name': 'Oklahoma', 'URLValue': 'US-OK-SB'}
    OR = {'countryCode': 'US', 'regionCode': 'OR', 'isoRegionCode': 'US-OR', 'name': 'Oregon', 'URLValue': 'US-OR-SB'}
    PW = {'countryCode': 'US', 'regionCode': 'PW', 'isoRegionCode': 'US-PW', 'name': 'Palau', 'URLValue': 'US-PW-SB'}
    PA = {'countryCode': 'US', 'regionCode': 'PA', 'isoRegionCode': 'US-PA', 'name': 'Pennsylvania', 'URLValue': 'US-PA-SB'}
    PR = {'countryCode': 'US', 'regionCode': 'PR', 'isoRegionCode': 'US-PR', 'name': 'Puerto Rico', 'URLValue': 'US-PR-SB'}
    RI = {'countryCode': 'US', 'regionCode': 'RI', 'isoRegionCode': 'US-RI', 'name': 'Rhode Island', 'URLValue': 'US-RI-SB'}
    SC = {'countryCode': 'US', 'regionCode': 'SC', 'isoRegionCode': 'US-SC', 'name': 'South Carolina', 'URLValue': 'US-SC-SB'}
    SD = {'countryCode': 'US', 'regionCode': 'SD', 'isoRegionCode': 'US-SD', 'name': 'South Dakota', 'URLValue': 'US-SD-SB'}
    TN = {'countryCode': 'US', 'regionCode': 'TN', 'isoRegionCode': 'US-TN', 'name': 'Tennessee', 'URLValue': 'US-TN-SB'}
    TX = {'countryCode': 'US', 'regionCode': 'TX', 'isoRegionCode': 'US-TX', 'name': 'Texas', 'URLValue': 'US-TX-SB'}
    UT = {'countryCode': 'US', 'regionCode': 'UT', 'isoRegionCode': 'US-UT', 'name': 'Utah', 'URLValue': 'US-UT-SB'}
    VT = {'countryCode': 'US', 'regionCode': 'VT', 'isoRegionCode': 'US-VT', 'name': 'Vermont', 'URLValue': 'US-VT-SB'}
    VI = {'countryCode': 'US', 'regionCode': 'VI', 'isoRegionCode': 'US-VI', 'name': 'Virgin Islands', 'URLValue': 'US-VI-SB'}
    VA = {'countryCode': 'US', 'regionCode': 'VA', 'isoRegionCode': 'US-VA', 'name': 'Virginia', 'URLValue': 'US-VA-SB'}
    WA = {'countryCode': 'US', 'regionCode': 'WA', 'isoRegionCode': 'US-WA', 'name': 'Washington', 'URLValue': 'US-WA-SB'}
    WV = {'countryCode': 'US', 'regionCode': 'WV', 'isoRegionCode': 'US-WV', 'name': 'West Virginia', 'URLValue': 'US-WV-SB'}
    WI = {'countryCode': 'US', 'regionCode': 'WI', 'isoRegionCode': 'US-WI', 'name': 'Wisconsin', 'URLValue': 'US-WI-SB'}
    WY = {'countryCode': 'US', 'regionCode': 'WY', 'isoRegionCode': 'US-WY', 'name': 'Wyoming', 'URLValue': 'US-WY-SB'}

# Access example
#print(Regions.AL.value)  # Outputs: Alabama
    
#region_info = Regions.AL.value
#print(f"Name: {region_info['name']}, URLValue: {region_info['URLValue']}")
    
def get_region_url(user_selected_region_label):
    # Find the Regions enum member based on the user-selected label
    selected_region = None
    for region in Region:
        if region.name == user_selected_region_label:
            selected_region = region
            break
    
    if selected_region is None:
        return "Invalid region selected"
    
    # Get the URLValue from the selected Regions enum member
    region_info = selected_region.value
    url_value = region_info.get('URLValue', 'URL details not found')
    
    return url_value

# Example usage
#user_selected_region_label = 'NV'  # This would be dynamically obtained from a user selection in practice
#url_value = get_region_url(user_selected_region_label)
#print(url_value)  # Outputs the URLValue for the selected region