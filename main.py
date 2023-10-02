# Import necessary libraries and modules
import numpy as np

import streamlit as st

condition_and_maintenance = {
    'inspection_report': 'Good condition with recent maintenance.',
    'maintenance_history': 'Regular maintenance and no major repairs.'
}

market_data = {
    'current_market_conditions': 'Stable with moderate demand for container ships.',
    'historical_sales_data': [75000000, 70000000, 72000000, 68000000, 71000000],
    'market_trends': 'Container shipping rates have been steady.'
}

geographic_location = {
    'location': 'Port of Los Angeles, USA'
}

economic_factors = {
    'economic_indicators': 'Stable economy with low inflation and interest rates.'
}

regulatory_compliance = {
    'compliance_status': 'Fully compliant with international regulations.'
}

special_features = {
    'advanced_navigational_system': True,
    'eco_friendly_equipment': False
}

ownership_history = {
    'previous_owners': ['ABC Shipping Co.', 'XYZ Maritime Ltd.'],
    'notable_events': 'No major incidents in the ship’s history.'
}


# # Define valuation methodology and weights
# valuation_weights = {
#     'age_weight': 0.0001,
#     'size_weight': 0.0001,
#     'condition_weight': 0.0001,
#     'market_data_weight': 0.00015,
#     'location_weight': 0.0005,
#     'economic_factors_weight': 0.0005,
#     'compliance_weight': 0.0005,
#     'special_features_weight': 0.0001,
#     'ownership_history_weight': 0.0001,
#     'risk_assessment_weight': 0.0001,
#     'discount_rate': 0.0008  # Used for discounted cash flow (DCF) valuation
# }
#

# Define valuation algorithm
def value_ship(ship_characteristics, condition_and_maintenance, market_data,
               geographic_location, economic_factors, regulatory_compliance,
               special_features, ownership_history, valuation_weights):
    # Calculate age-based valuation
    age_valuation = (1 - (ship_characteristics['age_years'] / 30)) * valuation_weights['age_weight']

    # Calculate size-based valuation
    size_valuation = (ship_characteristics['gross_tonnage'] / 100000) * valuation_weights['size_weight']

    # Calculate condition-based valuation (subjective assessment)
    condition_valuation = valuation_weights['condition_weight']

    # Calculate market data-based valuation (based on historical sales data)
    average_sale_price = np.mean(market_data['historical_sales_data'])
    market_valuation = (ship_characteristics['cargo_capacity_tons'] / 1000) * (
            ship_characteristics['engine_power_hp'] / 10000) * (average_sale_price / 1000000) * valuation_weights[
                           'market_data_weight']

    # Calculate location-based valuation (simple geographic factor)
    location_valuation = valuation_weights['location_weight']

    # Calculate economic factors-based valuation (simple economic stability factor)
    economic_valuation = valuation_weights['economic_factors_weight']

    # Calculate compliance-based valuation (simple compliance factor)
    compliance_valuation = valuation_weights['compliance_weight']

    # Calculate special features-based valuation (subjective assessment)
    special_features_valuation = valuation_weights['special_features_weight']

    # Calculate ownership history-based valuation (subjective assessment)
    ownership_history_valuation = valuation_weights['ownership_history_weight']

    # Total ship valuation
    total_valuation = (age_valuation + size_valuation + condition_valuation + market_valuation +
                       location_valuation + economic_valuation + compliance_valuation +
                       special_features_valuation + ownership_history_valuation)

    return total_valuation


# print(f"The estimated value of the ship is: ${estimated_value:,.2f}")

# Define Streamlit app
def main():
    st.title('Ship Valuation App')

    ship_characteristics = {
        'ship_type': 'Container Ship',
        'age_years': 10,
        'size_meters': {'length': 200, 'width': 30, 'draft': 12},
        'gross_tonnage': 50000,
        'engine_power_hp': 40000,
        'cargo_capacity_tons': 25000
    }

    # Default values for valuation_weights
    valuation_weights = {
        'age_weight': 0.0001,
        'size_weight': 0.0001,
        'condition_weight': 0.0001,
        'market_data_weight': 0.0015,
        'location_weight': 0.0005,
        'economic_factors_weight': 0.0005,
        'compliance_weight': 0.0005,
        'special_features_weight': 0.0003,
        'ownership_history_weight': 0.0004
    }

    # Ship Characteristics Input
    if st.sidebar.checkbox('Ship Characteristics Input', False):
        ship_characteristics['ship_type'] = st.sidebar.selectbox('Ship Type',
                                                                 ['Container Ship', 'Tanker', 'Bulk Carrier',
                                                                  'Fishing Vessel'])
        ship_characteristics['age_years'] = st.sidebar.number_input('Age (years)',
                                                                    value=ship_characteristics['age_years'],
                                                                    min_value=1, step=1)
        ship_characteristics['size_meters']['length'] = st.sidebar.number_input('Length (meters)', value=
        ship_characteristics['size_meters']['length'], min_value=1, step=1)
        ship_characteristics['size_meters']['width'] = st.sidebar.number_input('Width (meters)', value=
        ship_characteristics['size_meters']['width'], min_value=1, step=1)
        ship_characteristics['size_meters']['draft'] = st.sidebar.number_input('Draft (meters)', value=
        ship_characteristics['size_meters']['draft'], min_value=1, step=1)
        ship_characteristics['gross_tonnage'] = st.sidebar.number_input('Gross Tonnage',
                                                                        value=ship_characteristics['gross_tonnage'],
                                                                        min_value=1, step=1)
        ship_characteristics['engine_power_hp'] = st.sidebar.number_input('Engine Power (HP)',
                                                                          value=ship_characteristics['engine_power_hp'],
                                                                          min_value=1, step=1)
        ship_characteristics['cargo_capacity_tons'] = st.sidebar.number_input('Cargo Capacity (tons)',
                                                                              value=ship_characteristics[
                                                                                  'cargo_capacity_tons'], min_value=1,
                                                                              step=1)

    # Valuation Weights Configuration
    if st.sidebar.checkbox('Valuation Weights Configuration', False):
        valuation_weights['age_weight'] = st.sidebar.number_input('Age Weight', value=valuation_weights['age_weight'],
                                                                  min_value=0.0, step=0.0001, format='%f')

        valuation_weights['size_weight'] = st.sidebar.number_input('Size Weight',
                                                                   value=valuation_weights['size_weight'],
                                                                   min_value=0.0, step=0.0001, format='%f')
        valuation_weights['condition_weight'] = st.sidebar.number_input('Condition Weight',
                                                                        value=valuation_weights['condition_weight'],
                                                                        min_value=0.0, step=0.0001, format='%f')
        valuation_weights['market_data_weight'] = st.sidebar.number_input('Market Data Weight',
                                                                          value=valuation_weights['market_data_weight'],
                                                                          min_value=0.0, step=0.0001, format='%f')
        valuation_weights['location_weight'] = st.sidebar.number_input('Location Weight',
                                                                       value=valuation_weights['location_weight'],
                                                                       min_value=0.0, step=0.0001, format='%f')
        valuation_weights['economic_factors_weight'] = st.sidebar.number_input('Economic Factors Weight',
                                                                               value=valuation_weights[
                                                                                   'economic_factors_weight'],
                                                                               min_value=0.0, step=0.0001, format='%f')
        valuation_weights['compliance_weight'] = st.sidebar.number_input('Compliance Weight',
                                                                         value=valuation_weights['compliance_weight'],
                                                                         min_value=0.0, step=0.0001, format='%f')
        valuation_weights['special_features_weight'] = st.sidebar.number_input('Special Features Weight',
                                                                               value=valuation_weights[
                                                                                   'special_features_weight'],
                                                                               min_value=0.0, step=0.0001, format='%f')
        valuation_weights['ownership_history_weight'] = st.sidebar.number_input('Ownership History Weight',
                                                                                value=valuation_weights[
                                                                                    'ownership_history_weight'],
                                                                                min_value=0.0, step=0.0001, format='%f')

    if st.button('Calculate Valuation'):
        ship_valuation = value_ship(ship_characteristics, condition_and_maintenance, market_data,
                                    geographic_location, economic_factors, regulatory_compliance,
                                    special_features, ownership_history, valuation_weights)
        st.success(f"The estimated value of the ship is ${ship_valuation:,.2f} million.")


if __name__ == "__main__":
    main()
