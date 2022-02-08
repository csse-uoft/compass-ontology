from classes import Client, ClientState, ClientStatus, Service, LegalStatus, NeedSatisfier, DesiredClientState, \
    ActualClientState, ClientNeed
from namespaces import compass, cids, gender_ns, sex_ns, org, ic, time, schema, schema_old
from datetime import datetime
from owlready2 import default_world

client_statuses = []
codes_client_status = [
    'married', 'co_custodial_parent', 'employed_part_time', 'self_employed', 'uninsured', 'low_income'
]
for code_str in codes_client_status:
    code = cids.Code(code_str, namespace=compass)

    status = ClientStatus(f'status_{code_str}')
    status.hasCode.clear()
    status.hasCode.append(code)

    client_statuses.append(status)

# (instance name, description)
codes_client_states = [
    ('co_provider_for_2_dependents', 'is co-provider for two minor dependents'),
    ('low_household_monthly_income', 'has low household monthly income'),
    ('low_yearly_household_income', 'has low yearly household income'),
    ('no_insurance_for_dental', 'has no insurance for dental healthcare'),
    ('low_household_income', 'has low household income'),
]
codes_actual_client_states = [
    ('struggle_to_pay_rent', 'is struggling to pay rent'),
    ('family_struggles_to_maintain_nutrition',
     'is struggling to maintain adequate nutrition for all family members'),
    ('unable_to_pay_dental', 'is unable to pay for dental treatments'),
    ('has_dental_issues', 'has dental issues'),
    ('unaware_financial_support', 'is unaware of available financial benefits/supports'),
    ('unaware_affordable_dental', 'is unaware of affordable options for dental treatment'),
    ('unable_to_find_financial_support',
     'is unaware/unable of how to find information about available financial benefits/supports'),
    ('unable_to_find_affordable_dental',
     'is unaware/unable of how to find information about affordable options for dental work'),
]
codes_desired_client_states = [
    ('able_to_pay_rent', 'is able to pay rent'),
    ('family_is_able_to_maintain_nutrition',
     'is able to maintain adequate nutrition for all family members'),
    ('able_to_pay_dental', 'is able to pay for dental treatments'),
    ('no_dental_issues', 'does not have dental issue'),
    ('aware_financial_support', 'is aware of available financial benefits/supports'),
    ('aware_affordable_dental', 'is aware of affordable options for dental treatment'),
    ('able_to_find_financial_support',
     'is able to find information about available financial benefits/supports'),
    ('able_to_find_affordable_dental',
     'is able to find information about affordable options for dental work'),
]

for code_str, desc in [*codes_client_states, *codes_desired_client_states, *codes_actual_client_states]:
    code = cids.Code(code_str, namespace=compass)
    schema_old.description[code].append(desc)

    state = ClientState(f'state_{code_str}')
    state.hasCode.clear()
    state.hasCode.append(code)

# Create a client Shawna
# jd is unemployed and unable to manage addictions
client_shawna = Client('client_shawna')
client_shawna.givenName = 'Shawna'

address2 = ic.Address('address2')
address2.lat = 51.0383902
address2.long = -114.0603652
address2.hasPostalCode = 'T2G 1G4'
address2.hasCountry = ic.canada
address2.hasState = ic.alberta
address2.hasStreetType = ic.Avenue
address2.hasCityS = 'Calgary'
address2.hasStreet = '15TH'
address2.hasStreetNumber = '203'

# Use hasGender property in compass namespace
# compass:client1 compass:hasGender compass_gender:female
compass.hasGender[client_shawna].append(gender_ns.female)

client_shawna.hasClientStatus.clear()
for client_status in client_statuses:
    client_shawna.hasClientStatus.append(client_status)

for client_state_str, _ in [*codes_client_states, *codes_actual_client_states]:
    client_shawna.hasClientState.append(compass[f'state_{client_state_str}'])

# Add Need satisfier
satisfier_financial_help = NeedSatisfier('satisfier_financial_help')
satisfier_dental_treatment = NeedSatisfier('satisfier_dental_treatment')
satisfier_food = NeedSatisfier('satisfier_food')
satisfier_info_financial_support = NeedSatisfier('satisfier_info_financial_support')
satisfier_info_affordable_dental = NeedSatisfier('satisfier_info_affordable_dental')
satisfier_service_suggestion = NeedSatisfier('satisfier_service_suggestion')

# Add client needs (need type, description, satisfiers)
needs_data = [
    ('pay_rent', 'Improve ability to pay rent', [satisfier_financial_help]),
    ('family_maintains_nutrition', 'Improve ability to maintain adequate nutrition for all family members',
     [satisfier_financial_help, satisfier_food]),
    ('pay_dental', 'Improve ability to pay for dental treatments', [satisfier_financial_help]),
    ('dental_health', 'Improve dental health', [satisfier_dental_treatment]),
    ('financial_support', 'Improve awareness of available financial benefits/supports',
     [satisfier_info_financial_support]),
    ('affordable_dental', 'Improve awareness of affordable options for dental treatment',
     [satisfier_info_affordable_dental]),
    ('find_financial_support', 'Improve ability to find information about available financial benefits/supports',
     [satisfier_service_suggestion]),
    ('find_affordable_dental', 'Improve ability to find information about affordable options for dental work',
     [satisfier_service_suggestion]),
]

for need_type, desc, satisfiers in needs_data:
    need = ClientNeed(f'need_{need_type}')
    schema_old.description[need].append(desc)
    need.hasNeedType.append(need_type)
    need.ofClient.append(client_shawna)
    client_shawna.hasNeed.append(need)

    # Assign need satisfier to client needs
    for satisfier in satisfiers:
        need.hasNeedSatisfier.append(satisfier)

the_mustard_seed_calgary = cids.Organization('the_mustard_seed_calgary')
government_of_alberta = cids.Organization('government_of_alberta')
government_of_alberta.hasAddress.append(address2)
government_of_alberta.description.append('Government of Alberta')
tummy_tamers = cids.Organization('tummy_tamers')
tummy_tamers.description.append('Tummy Tamers')
helper_seeker = cids.Organization('HelperSeeker')

income_assistance_program = Service('income_assistance_program')
low_income_benefit_program = Service('low_income_benefit_program')
alberta_direct_to_tenant_tent_supplement = Service('alberta_direct_to_tenant_tent_supplement')
alberta_direct_to_tenant_tent_supplement.description.append(
    'Rent supplement programs help households find affordable rental accommodation')

community_kitchen_program = Service('community_kitchen_program')
community_kitchen_program.description.append(
    'Tummy Tamers provides a feeding program specifically designed for children from ages 5-12 in low-income communities')

alberta_child_health_benefit = Service('alberta_child_health_benefit')
alberta_child_health_benefit.description.append(
    'immediate financial relief to Albertan families and vulnerable Alberta')

alberta_emergency_financial_assistance = Service('alberta_emergency_financial_assistance')
alberta_emergency_financial_assistance.description.append(
    'Financial assistance for unexpected emergencies is available through the Emergency Needs Allowance')

recommendation_service = Service('recommendation_service')

income_assistance_program.providedBy.append(the_mustard_seed_calgary)
income_assistance_program.providesSatisfier.append(satisfier_financial_help)

alberta_direct_to_tenant_tent_supplement.providedBy.append(government_of_alberta)
alberta_direct_to_tenant_tent_supplement.providesSatisfier.append(satisfier_financial_help)

low_income_benefit_program.providedBy.append(government_of_alberta)
low_income_benefit_program.providesSatisfier.append(satisfier_financial_help)

community_kitchen_program.providedBy.append(tummy_tamers)
community_kitchen_program.providesSatisfier.append(satisfier_food)

alberta_child_health_benefit.providedBy.append(government_of_alberta)
alberta_child_health_benefit.providesSatisfier.append(satisfier_financial_help)
alberta_emergency_financial_assistance.providedBy.append(government_of_alberta)
alberta_emergency_financial_assistance.providesSatisfier.append(satisfier_financial_help)

recommendation_service.providedBy.append(helper_seeker)
recommendation_service.providesSatisfier.append(satisfier_service_suggestion)
recommendation_service.providesSatisfier.append(satisfier_info_affordable_dental)
recommendation_service.providesSatisfier.append(satisfier_info_financial_support)

# Lunch Service Representation
youth_centers_of_calgary = cids.Organization('youth_centers_of_calgary')
lunch_service = Service('lunch_service')
lunch_service.providedBy.append(youth_centers_of_calgary)
lunch_service.description.append('FREE contactless lunches from 11:00 am to 1:00 pm No registration required')
lunch_service.hasCost.append(100)

# Create time interval: 11:00 AM to 1:00 PM weekdays.
for dayOfWeek in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    start_time = time.GeneralDateTimeDescription(f'instant_{dayOfWeek}_11am')
    time.hour[start_time].append(11)
    start_time.dayOfWeek.append(time[dayOfWeek])

    end_time = time.GeneralDateTimeDescription(f'instant_{dayOfWeek}_1pm')
    time.hour[end_time].append(13)
    end_time.dayOfWeek.append(time[dayOfWeek])

    time_interval = time.DateTimeInterval(f'interval_{dayOfWeek}_11am_1pm')
    time_interval.hasDateTimeDescription.append(start_time)
    time_interval.hasDateTimeDescription.append(end_time)

    # Append to lunch service
    lunch_service.hasTime.append(time_interval)

# --- SPARQL ---
# Client needs: What do I need?
result = default_world.sparql('''
PREFIX comp: <http://compass#>
SELECT ?needs WHERE {
    comp:client_shawna comp:hasNeed ?needs
}
''')
# [[compass.need_pay_rent], [compass.need_family_maintains_nutrition], [compass.need_pay_dental], [compass.need_dental_health], [compass.need_financial_support], [compass.need_affordable_dental], [compass.need_find_financial_support], [compass.need_find_affordable_dental]]
# print('\nClient needs: ', list(result))

# Service location: Where do I go to get this service?
result = default_world.sparql('''
PREFIX comp: <http://compass#>
PREFIX ic: <http://ontology.eil.utoronto.ca/tove/icontact#>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
SELECT * WHERE {
    comp:low_income_benefit_program comp:providedBy ?org.
    ?org ic:hasAddress ?addr.
    ?addr geo:lat ?lat;
          geo:long ?lng;
          ic:hasPostalCode ?postal_code;
          ic:hasCountry ?country;
          ic:hasState ?state;
          ic:hasStreetType ?street_type;
          ic:hasStreet ?street_name;
          ic:hasStreetNumber ?street_number
}
''')

# [[compass.government_of_alberta, compass.address2, 51.0383902, -114.0603652, 'T2G 1G4', icontact.canada, icontact.alberta, icontact.Avenue, '15TH', '203']]
# print('\nService location: ', list(result))

# Service description
result = default_world.sparql('''
PREFIX comp: <http://compass#>
SELECT * WHERE {
    comp:lunch_service <http://schema.org/description> ?desc.
}
''')

# [['FREE contactless lunches from 11:00 am to 1:00 pm No registration required']]
# print('\nService description: ', list(result))

# Service operating hours
result = default_world.sparql('''
PREFIX comp: <http://compass#>
PREFIX time: <http://www.w3.org/2006/time#>
SELECT * WHERE {
    comp:lunch_service time:hasTime ?timeInterval.
}
''')

# [[compass.interval_Monday_11am_1pm], [compass.interval_Tuesday_11am_1pm], [compass.interval_Wednesday_11am_1pm], [compass.interval_Thursday_11am_1pm], [compass.interval_Friday_11am_1pm]]
# print('\nService operating hours: ', list(result))

# Service Cost
result = default_world.sparql('''
PREFIX comp: <http://compass#>
SELECT * WHERE {
    comp:lunch_service comp:hasCost ?cost.
}
''')

# [[100]]
# print('\nService operating hours: ', list(result))

# Find service that provides a specific need satisfier (financial help)
result = default_world.sparql('''
PREFIX comp: <http://compass#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT * WHERE {
    ?service rdf:type comp:Service.
    ?service comp:providesSatisfier comp:satisfier_financial_help.
}
''')

# [[compass.income_assistance_program], [compass.low_income_benefit_program], [compass.alberta_direct_to_tenant_tent_supplement], [compass.alberta_child_health_benefit], [compass.alberta_emergency_financial_assistance]]
# print('\nService provides financial help: ', list(result))

# Find service that match my need
result = default_world.sparql('''
PREFIX comp: <http://compass#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT DISTINCT ?service WHERE {
    comp:client_shawna comp:hasNeed ?client_need.
    ?client_need comp:hasNeedSatisfier ?satisfier.
    
    ?service rdf:type comp:Service.
    ?service comp:providesSatisfier ?satisfier.
}
''')

# [[compass.income_assistance_program], [compass.low_income_benefit_program], [compass.alberta_direct_to_tenant_tent_supplement], [compass.alberta_child_health_benefit], [compass.alberta_emergency_financial_assistance], [compass.community_kitchen_program], [compass.recommendation_service]]
# print('\nService match my needs: ', list(result))
