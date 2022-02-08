from classes import Client, ClientState, ClientStatus, Service, LegalStatus, NeedSatisfier
from namespaces import compass, cids, gender_ns, sex_ns, org, ic, time
from datetime import datetime

# Create some Codes on the compass namespace
for code_str in ['broken_home', 'unemployed', 'low_income', 'unable_to_manage_addictions', 'separated',
                 'stay_at_home_parent']:
    cids.Code(code_str, namespace=compass)

# Create a client Jabe Doe
# jd is unemployed and unable to manage addictions
client1 = Client('jd')
client1.givenName = 'Jabe'
client1.familyName = 'Doe'

# Use hasGender property in compass namespace
# compass:client1 compass:hasGender compass_gender:female
compass.hasGender[client1].append(gender_ns.female)

state_unemployed = ClientState('state_unemployed')
state_unemployed.hasCode.append(compass.unemployed)
state_unable_to_manage_addictions = ClientState('state_unable_to_manage_addictions')
state_unable_to_manage_addictions.hasCode.append(compass.unable_to_manage_addictions)

status_unemployed = ClientStatus('status_unemployed')
status_unemployed.hasCode.append(compass.unemployed)

client1.hasClientState.append(state_unemployed)
client1.hasClientState.append(state_unable_to_manage_addictions)
client1.hasClientStatus.append(status_unemployed)


# Create legal status 'charity', it can be accessed as 'compass.charity'
for name in ['charity']:
    LegalStatus(name)

# Create an organization
org1 = org.Organization('org1')
org1.hasLegalStatus.append(compass.charity)

# 14032347388
# 203 15Th Avenue SE, Calgary, AB T2G 1G4, lat: 51.0383902 lng:-114.0603652
address1 = ic.Address('address1')
address1.lat = 51.0383902
address1.lng = -114.0603652
address1.hasPostalCode = 'T2G 1G4'
address1.hasCountry = ic.canada
address1.hasState = ic.alberta
address1.hasStreetType = ic.avenue
address1.hasStreetName = '15TH'
address1.hasStreetNumber = '203'

org1.hasName.append('Calgary Alpha House Society')
org1.hasAddress.append(address1)

# Create two services that provided by 'org1'
service1 = Service('service1')
service1.providedBy.append(org1)
service1.hasName.append('Initial Assessment Service')
service1.hasDescription = "An initial assessment can take place at any time and through any form of communication such as in-person, by phone, or by email."

service2 = Service('service2')
service2.providedBy.append(org1)
service2.hasName.append('Withdrawal Management Service')
service2.hasDescription = "Withdrawal management, which includes detox assessment, nursing and medical assessment, opioid replacement therapies, referrals to long-term treatment centres, and access to our housing team"


# Create a program that provided by 'org1' and hasSercice 'service1'
program1 = cids.Program('program1')
program1.hasName.append('Detox program')
program1.providedBy.append(org1)
program1.hasService.append(service1)

# Create 3 need satisfiers that the above services provide.
ns1 = NeedSatisfier('ns1')
ns1.hasSatisfierType.append('Initial Assessment')

ns2 = NeedSatisfier('ns2')
ns2.hasSatisfierType.append('Detox Assessment')

ns3 = NeedSatisfier('ns3')
ns3.hasSatisfierType.append('Nursing')

service1.providesSatisfier.append(ns1)
service2.providesSatisfier.append(ns2)
service2.providesSatisfier.append(ns3)


# Create time interval: 7:30 AM to 8:00 AM daily.
# 7:30 AM Instant
time_7_30_am = time.Instant('instant1')
time.hour[time_7_30_am].append(7)
time.minute[time_7_30_am].append(30)


# 8 AM Instant
time_8_am = time.Instant('instant1')
time.hour[time_8_am].append(8)

time_interval_7_30_am_8_am = time.DateTimeInterval('DateTimeInterval1')
time.hasBeginning[time_interval_7_30_am_8_am].append(time_7_30_am)
time.hasEnd[time_interval_7_30_am_8_am].append(time_8_am)

cids.hasTimeInterval[service1].append(time_interval_7_30_am_8_am)


# Needs related
import demo

